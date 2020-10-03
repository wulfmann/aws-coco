# AWS coco (console container)

Easily manage AWS Console Sessions

## Quickstart

Install

```bash
$ pip install aws-coco
```

Usage

```bash
$ coco
```

You should now have a new browser tab with your aws session!

Continue reading for a more in-depth walkthrough of the setup.

If `coco` is too generic, this package also exposes `aws_coco`.

## Requirements

There are two different modes for `coco`. Normal and Firefox Containers.

### Container Mode (default)

- [Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [Firefox Multi-Account Containers](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/)
- [Open URL in Container Extension](https://addons.mozilla.org/en-US/firefox/addon/open-url-in-container/)

If you don't wish to install the extension through the marketplace, you can install from source [here](https://github.com/honsiorovskyi/open-url-in-container).

### Normal Mode

- Any browser supported by [webbrowser](https://docs.python.org/3.8/library/webbrowser.html#webbrowser.get)
- [Python >= 3.7](http://python.org/)

If you do not wish to use containers, make sure to specify the `--no-container` flag.

## Installation

```bash
$ pip install aws-coco
```

## Usage

This section explains how to use `coco` and covers some of the options available to you.

### Basic Usage

#### Container Mode Example

```bash
$ coco --color green --icon fingerprint --name test
```

This will open the url in a `green` firefox container tab named `test` with a `fingerprint` icon.

This can be annoying to type, so it's recommended to build aliases for your accounts.

Example alias:

```bash
alias coco-test=coco --color green --icon fingerprint --name test
```

Now you can just run:

```bash
$ coco-test
```

#### Normal Mode Example

```bash
$ coco
```

This will open your session in your default browser.

### Credential Resolution

This project uses [boto3](https://github.com/boto/boto3). You can learn more about how `boto3` resolves credentials [here](https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/configuration.html#configuring-credentials).

If you specify the `--profile` flag, `coco` will pass that value into the `boto3` session and it will attempt to use the corresponding section in the `~/.aws/credentials` file for the session.

### Options

This section contains a description of the various options available to you. You can also pass the `-h` flag to print the help.

|Flag|Description|Default|Required|
|----|-----------|-------|--------|
|`--color`, `-c`|The container tab's color||false|
|`--container`, `--no-container`|Determines if the url should be opened in a firefox container||true|
|`--destination`, `-d`|The destination URL to open in the AWS console||false|
|`--icon`, `-i`|The container tab's icon||false|
|`--name`, `-n`|The container tab's name|The profile name if passed|false|
|`--open`, `--no-open`|Determines if the url should be automatically opened in the browser||true|
|`--profile`, `-p`|The AWS profile to use||false|

### Available Colors

|value|
|-----|
|blue|
|turquoise|
|green|
|yellow|
|orange|
|red|
|pink|
|purple|

### Available Icons

|value|
|-----|
|fingerprint|
|briefcase|
|dollar|
|cart|
|vacation|
|gift|
|food|
|fruit|
|pet|
|tree|
|chill|
|circle|
|fence|

## Contributing

For more information on contributing, check out the [doc](/CONTRIBUTING.md)
