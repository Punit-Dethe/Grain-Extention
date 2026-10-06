"""Fixed provenance checkpoint data, not an author builder or Agent harness.

Uses real author/registry commands without executing extension or build scripts.
Temporary source Git repos have example origins: remote ownership/review is NOT
claimed. Output is public, unsigned test data; no signing key is generated here.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import struct
import subprocess
import tempfile
import zlib


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(args, cwd=None):
    return subprocess.run(
        [str(v) for v in args], cwd=cwd, check=True, capture_output=True,
        text=True, timeout=30, creationflags=0x08000000 if os.name == "nt" else 0,
    ).stdout.strip()


def icon():
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 512, 512, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress((b"\0" + b"\0\0\0\xff" * 512) * 512)) + chunk(b"IEND", b""))


def prepare(kind, root, scratch, author, registry):
    target = root / kind
    target.mkdir()
    working = scratch / kind
    working.mkdir()
    identifier = "com.example.provenance-" + kind
    repo = "https://github.com/example/grain-provenance-" + kind
    args = [author, "init", "Tools", "--id", identifier]
    if kind == "mcp":
        args += ["--mcp-url", "https://tools.example.com/mcp"]
    run(args, working)
    source = working / "tools"
    if kind == "native":
        (source / "icon.png").write_bytes(icon())
        (source / "dist").mkdir()
        (source / "dist/main.js").write_text(
            "grain.actions.register('hello', () => ({ok:{title:'Hello',body:'Provenance fixture'}}));",
            encoding="utf-8",
        )
        # A build that would fail if accidentally invoked. Preparation never runs it.
        (source / "package.json").write_text('{"scripts":{"build":"exit 93"}}', encoding="utf-8")
    run(["git", "init", "--quiet"], source)
    run(["git", "remote", "add", "origin", repo], source)
    run(["git", "add", "."], source)
    fixed_git = ["git", "-c", "user.name=Provenance fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "commit.gpgsign=false", "-c", "tag.gpgsign=false", "-c", "core.hooksPath="]
    run(fixed_git + ["commit", "--quiet", "-m", "Controlled provenance fixture"], source)
    run(fixed_git + ["tag", "-a", "v0.1.0", "-m", "Controlled fixture"], source)
    commit = run(["git", "rev-parse", "HEAD"], source)
    submission_root = target / "submission"
    submission_root.mkdir()
    run([author, "submit", "--registry", submission_root, "--repo", repo,
         "--tag", "v0.1.0", "--commit", commit, "--contact", "fixture@example.invalid"], source)
    submission = submission_root / "extensions" / identifier
    prepared = target / "prepared"
    run([registry, "prepare-artifact", "--submission", submission, "--src", source, "--out", prepared])
    raw_receipt = (prepared / "receipt.json").read_bytes()
    receipt = json.loads(raw_receipt)
    candidate = target / "candidate"
    run([registry, "prepare-catalogue", "--submission", submission, "--prepared", prepared,
         "--receipt-sha256", digest(raw_receipt), "--producer-sha256", receipt["producer_sha256"], "--out", candidate])
    assert receipt["producer_sha256"] == digest(registry.read_bytes())
    return {
        "id": identifier, "receipt_sha256": digest(raw_receipt),
        "submission_sha256": digest(json.dumps(receipt["submission"], ensure_ascii=False, separators=(",", ":")).encode()),
        "candidate_sha256": digest((candidate / "candidate.json").read_bytes()),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry-tool", type=Path, required=True)
    parser.add_argument("--author-tool", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    registry, author = args.registry_tool.resolve(strict=True), args.author_tool.resolve(strict=True)
    root = args.out.resolve()
    root.mkdir()  # Fresh owned directory; never overwrites previous evidence.
    with tempfile.TemporaryDirectory(prefix="grain-ci-source-") as source:
        fixtures = {kind: prepare(kind, root, Path(source), author, registry) for kind in ["native", "mcp"]}
    (root / "producer.json").write_text(json.dumps({
        "schema": 1, "evidence_class": "controlled-ci-fixtures/not-human-reviewed",
        "grain_commit": "1be8a2c0b6f657461aebe5291a20ec379d23135b",
        "producer_sha256": digest(registry.read_bytes()), "fixtures": fixtures,
    }, indent=2) + "\n", encoding="utf-8")
    print("Prepared both controlled fixture candidates; no signing or author execution")


if __name__ == "__main__":
    main()
