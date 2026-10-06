"""Trusted data preparation on a fresh runner; never builds/executes author files."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    for name in ["tool", "tool-sha256", "submission", "source", "out", "grain-commit"]:
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--native-result")
    args = parser.parse_args()
    tool = Path(args.tool)
    if tool.is_symlink() or not tool.is_file() or tool.stat().st_size > 128 * 1024 * 1024:
        raise ValueError("Unsupported downloaded tool")
    tool = tool.resolve(strict=True)
    if digest(tool.read_bytes()) != args.tool_sha256:
        raise ValueError("Downloaded tool differs from trusted request job output")
    tool.chmod(0o700)
    source, submission = Path(args.source).resolve(strict=True), Path(args.submission).resolve(strict=True)
    out = Path(args.out).resolve()
    out.mkdir()  # No overwrite, outside source/submission; CI supplies owned scratch.
    if args.native_result:
        manifest = json.loads((source / "manifest.json").read_bytes())
        if manifest.get("entry") != "dist/main.js":
            raise ValueError("Current isolated build profile requires dist/main.js")
        built = Path(args.native_result) / "main.js"
        if built.is_symlink() or not built.is_file() or not 0 < built.stat().st_size <= 4 * 1024 * 1024:
            raise ValueError("Unsupported native build result")
        dist = source / "dist"
        # Refuse tracked/preexisting output dirs rather than following author symlinks.
        dist.mkdir()
        shutil.copyfile(built, dist / "main.js")
    def run(command):
        subprocess.run([str(v) for v in command], check=True, stdin=subprocess.DEVNULL, timeout=90)
    run([tool, "prepare-artifact", "--submission", submission, "--src", source, "--out", out / "prepared"])
    raw = (out / "prepared/receipt.json").read_bytes()
    receipt = json.loads(raw)
    if receipt["producer_sha256"] != args.tool_sha256:
        raise ValueError("Producer pin mismatch")
    run([tool, "prepare-catalogue", "--submission", submission, "--prepared", out / "prepared",
         "--receipt-sha256", digest(raw), "--producer-sha256", args.tool_sha256, "--out", out / "candidate"])
    shutil.copytree(submission, out / "submission" / receipt["submission"]["id"])
    (out / "producer.json").write_text(json.dumps({
        "schema": 1, "evidence_class": "pinned-remote-source-build/not-human-approved",
        "grain_commit": args.grain_commit, "producer_sha256": args.tool_sha256,
        "receipt_sha256": digest(raw), "submission_sha256": receipt["submission_sha256"],
        "candidate_sha256": digest((out / "candidate/candidate.json").read_bytes()),
    }, indent=2) + "\n")
    print("Pinned remote source candidate prepared; no author execution or signing in this job")


if __name__ == "__main__":
    main()
