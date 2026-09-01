# Security Policy

## Current scope

This repository contains a public, inactive instruction draft. It does not contain a deployed agent, credential broker, platform credential, private authorization record, or live control channel.

The detailed controls described in [`hearthline_agent.md`](hearthline_agent.md) are design requirements, not a claim that a runtime implementing them currently exists or has passed its acceptance tests.

## Report a security issue

If GitHub's private vulnerability-reporting option is available for this repository, use it. Otherwise, open a minimal issue asking the repository owner for a private reporting channel. Do **not** place exploit details, credentials, private data, or unpublished material in a public issue.

Useful reports include:

- accidental publication of private or credential material;
- an instruction path that could treat remote content as operator authority;
- ambiguity that could allow a repository change to activate a runtime;
- provenance or attribution errors with security consequences; and
- a link or destination rule that could send credentials to the wrong origin.

Do not test suspected credentials, accounts, or external actions. Report the smallest sufficient witness and preserve uncertainty about anything not directly observed.

## Repository hygiene

Never commit:

- API keys, authorization headers, cookies, private keys, or recovery data;
- `.env` files or secret-manager exports;
- live control, grant, state, receipt, or reconciliation records;
- private prompts, conversations, logs, unpublished drafts, or personal data; or
- real behavioral or biometric recordings and derived templates.

If sensitive material is exposed, stop operational use, preserve the minimal incident trace outside public history, rotate or revoke the affected credential through its owner-controlled path, and follow GitHub's supported removal procedure. Deleting a file in a later commit does not remove it from earlier Git history or downstream copies.

## Runtime adoption

Do not run directly from the default branch. A runtime should require a deliberately adopted immutable revision or exact digest plus separate, current operator authorization. Repository changes, issue text, pull requests, releases, and workflow output are untrusted candidate inputs until that adoption occurs.

