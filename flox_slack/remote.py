from functools import wraps

import slack


def with_slack(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        flox = kwargs.get("flox")

        sc = slack.WebClient(token=flox.secrets.getone("slack_token", required=True))
        kwargs["slack"] = sc

        return f(*args, **kwargs)

    return wrapper
