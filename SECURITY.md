# Security Policy

## Scope

This repository contains educational deep learning notebooks. It does not
ship credentials, private datasets, or production services.

## No-secrets policy

- No API keys, access tokens, passwords, private keys, or personal data are
  committed to this repository.
- `.env` is ignored by Git. Use `.env.example` as the template if you add an
  optional integration later.
- The notebooks download only public datasets from their canonical URLs.
- Models and experiment outputs are written to ignored `outputs/` folders.

## Reporting a problem

If you find a leaked credential, private artifact, or another security issue,
please open a private security advisory on GitHub or contact the repository
owner through GitHub. Do not open a public issue containing the sensitive
value.

If a credential is ever committed by mistake, revoke it immediately and
rewrite the affected Git history before making the repository public again.

## Contributor checklist

1. Run `python scripts/check_for_secrets.py` before committing.
2. Run `python scripts/validate_notebooks.py` before committing.
3. Never commit `.env`, downloaded datasets, model weights, or notebook
   outputs.
4. Keep dataset access public and URL-based; do not add authenticated
   downloads.

## Data and privacy

The notebooks use public benchmark data (MNIST, CIFAR-10, IMDB) and a public
Iris CSV. Review each dataset's original license and usage terms before
redistributing derived data. No personal or confidential data is used.
