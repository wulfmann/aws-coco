# Contributing to aws-coco

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Pull Requests

We would love your pull requests! If you'd like to propose a change or add a feature, use the following steps:

1. Fork the repo and create your branch from `master`.
2. If you've added code that should be tested, add tests.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

### Any contributions you make will be under the MIT Software License

W you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Bug Reports

We use GitHub issues to track public bugs. Report a bug by [opening a new issue]().

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

## Development

This section contains some guidelines for development.

### Environment

This project uses [Poetry](https://python-poetry.org) for dependency management and publishing.

After installing Poetry, you can install the dependencies with:

```bash
$ poetry install --dev
```

### Tests

This project uses [pytest](https://docs.pytest.org/en/stable/) for tests.

You can run it with the following:

```bash
$ poetry run pytest
```

### Formatting

This project uses [black](https://github.com/psf/black) for code formatting.

You can run it with the following:

```bash
$ poetry run black .
```
