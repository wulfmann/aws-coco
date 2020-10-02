import sys
import json
import urllib

import requests

from aws_coco.lib.utils import dict_to_querystring


def create_signin_token(session):
    credentials = session.get_credentials()

    if not credentials.token:
        print(
            f"coco does not work without a session token. make sure you are running this from within a temporary session"
        )
        sys.exit(1)

    session_parameters = {
        "sessionId": credentials.access_key,
        "sessionKey": credentials.secret_key,
        "sessionToken": credentials.token,
    }

    response = requests.get(
        "https://signin.aws.amazon.com/federation",
        params={"Action": "getSigninToken", "Session": json.dumps(session_parameters)},
    )

    return response.json().get("SigninToken")


def create_console_url(session, destination=None):
    if destination is None:
        destination = "https://console.aws.amazon.com/"

    signin_token = create_signin_token(session)

    base = "https://signin.aws.amazon.com/federation"
    qs = dict_to_querystring(
        {
            "Action": "login",
            "Issuer": "aws-coco",
            "Destination": urllib.parse.quote_plus(destination),
            "SigninToken": signin_token,
        }
    )

    return f"{base}?{qs}"
