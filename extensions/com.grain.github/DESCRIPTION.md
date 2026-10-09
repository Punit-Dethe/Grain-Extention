# GitHub

Bring your repositories, issues and pull requests into conversations with Grain.
This integration uses GitHub's official hosted MCP server.

## What you can do

- Find repositories and search code you have permission to access.
- Read issues and pull requests, and help draft issue updates or comments.
- Create or update issues and work with pull requests when your account permits it.
- Inspect workflow runs and investigate failed jobs using the available tools.

Try asking:

> Show the open issues in my test repository.

> Summarize this pull request and its checks.

> Create a test issue describing the bug we just discussed.

Available actions depend on GitHub's enabled tools and your account permissions.
Review Grain's requested action before approving a change.

## Account access

A GitHub account and authorization are required. You can access only resources
your account is permitted to use; organizations may require administrator
approval or additional sign-in. Disconnecting in Grain removes its stored account
access; GitHub app authorization can also be revoked in your GitHub settings.

Tool requests go to GitHub's server. Information returned by tools is processed
by the model you configured for Grain's Agent. This extension does not get access
to your screen, dictation history, selected text or prompt settings.

Maintained by Grain using GitHub's official MCP server. GitHub's name and artwork
identify the integration and do not imply endorsement.
