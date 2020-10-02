# AWS coco (console container)

This tool allows you to manage AWS Console Sessions with Firefox Containers

## Quickstart

Ensure you've  met the [requirements](#requirements).

```bash
$ pip install aws_coco
```

Usage

```bash
$ coco -c green -i fingerprint
```

You should now have a new browser tab with your aws session!

Continue reading for a more in-depth walkthrough of the setup.

## Requirements

- [Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [Firefox Multi-Account Containers](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/)
- [Open URL in Container Extension](https://addons.mozilla.org/en-US/firefox/addon/open-url-in-container/)
- [Python >= 3.7](http://python.org/)

If you don't wish to install the extension through the marketplace, the source for the extension can be found [here](https://github.com/honsiorovskyi/open-url-in-container).

## Installation

```bash
$ pip install aws_coco
```

## Usage

```bash
$ coco 
```

## Development

```bash
$ git clone https://github.com/wulfmann/aws-coco.git
$ git clone git@github.com:wulfmann/aws-coco.git
```

Install Dependencies

```bash
$ poetry install
```

Run the command

```bash
$ poetry run coco -c green -i fingerprint
```

Run tests

```bash
$ poetry run pytest
```
