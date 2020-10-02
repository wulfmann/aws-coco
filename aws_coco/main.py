import argparse
import webbrowser

import boto3

from aws_coco.lib.firefox import colors
from aws_coco.lib.firefox import icons
from aws_coco.lib.firefox import format_for_container
from aws_coco.lib.aws import create_console_url
from aws_coco.lib.utils import NegateAction


def construct_parser():
    parser = argparse.ArgumentParser(
        description="A utility for managing AWS Console Sessions"
    )

    parser.add_argument('--version', action='version', version='%(prog)s 0.1.3')

    parser.add_argument("--profile", "-p", help="The AWS profile to use", default=None)

    parser.add_argument(
        "--container",
        "--no-container",
        dest="container",
        action=NegateAction,
        help="Open URL in Firefox container",
        default=True,
        nargs=0,
    )

    parser.add_argument(
        "--open",
        "--no-open",
        dest="open",
        action=NegateAction,
        help="Open URL automatically",
        default=True,
        nargs=0,
    )

    parser.add_argument("--name", "-n", help="The container tab name")
    parser.add_argument("--color", "-c", choices=colors, help="The container tab color")
    parser.add_argument("--icon", "-i", choices=icons, help="The container tab icon")
    parser.add_argument(
        "--destination",
        "-d",
        choices=icons,
        help="The destination URL in the AWS console",
        default=None,
    )

    return parser


def validate_args(args):
    if args.container:
        if not args.color:
            raise Exception(f"--color is required if --container is passed")
        if not args.icon:
            raise Exception(f"--icon is required if --container is passed")


def main(args):
    validate_args(args)

    session = boto3.session.Session(profile_name=args.profile)
    url = create_console_url(session, args.destination)

    if args.container:
        firefox = webbrowser.get("firefox")

        if firefox is None:
            raise Exception(f"firefox is required if --container is passed")

        container_name = args.profile
        if args.name:
            container_name = args.name

        url = format_for_container(url, container_name, args.color, args.icon)

        if args.open:
            firefox.open_new_tab(url)
        else:
            print(url)
    else:
        if args.open:
            webbrowser.open_new(url)
        else:
            print(url)


def run():
    parser = construct_parser()
    args = parser.parse_args()
    main(args)
