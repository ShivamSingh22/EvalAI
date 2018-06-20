import os
import json

from click import echo
from evalai.utils.config import AUTH_TOKEN_PATH


def get_token():
    """
    Loads token to be used for sending requests.
    """
    if os.path.exists(AUTH_TOKEN_PATH):
        with open(str(AUTH_TOKEN_PATH), 'r') as TokenObj:
            try:
                data = TokenObj.read()
            except (OSError, IOError) as e:
                echo(e)
        data = json.loads(data)
        token = data["token"]
        return token
    else:
        echo("\nYour token file doesn't exists.")
        echo("\nIt should be present at ~/.evalai/token.json\n")
        return None


def get_headers():
    """
    Returns token formatted in header for sending requests.
    """
    headers = {
            "Authorization": "Token {}".format(get_token()),
    }

    return headers
