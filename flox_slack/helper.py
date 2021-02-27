from functools import wraps

from slack.errors import SlackApiError

from floxcore.exceptions import PluginException


def handle_exceptions(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except SlackApiError as e:
            raise PluginException(f'[Slack API]{e.response}.')

    return wrapper
