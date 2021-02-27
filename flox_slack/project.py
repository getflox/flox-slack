from slack import WebClient
from slack.errors import SlackApiError
from slugify import slugify

from flox_slack.helper import handle_exceptions
from flox_slack.remote import with_slack
from floxcore.context import Flox


def _name(flox: Flox):
    name = flox.id
    if flox.settings.slack.name:
        name = flox.settings.slack.name
    if flox.settings.slack.prefix:
        name = flox.settings.slack.prefix + name

    return name


@handle_exceptions
@with_slack
def create_channel(flox: Flox, slack: WebClient, out, **kwargs):
    """Creates slack channel"""
    name = slugify(_name(flox))
    try:
        slack.conversations_create(name=name, is_private=flox.settings.slack.private_channel)
        out.success(f'Channel "#{name}" created')
    except SlackApiError as e:
        if e.response.get("error") == "name_taken":
            out.info(f'Channel "#{name}" already created')
        else:
            raise


@handle_exceptions
@with_slack
def set_channel_topic(flox: Flox, slack: WebClient, out, **kwargs):
    response = slack.conversations_list(limit=1000)
    name = slugify(_name(flox))
    for channel in [ch for ch in response.get("channels") if ch["name"] == name]:
        slack.conversations_setTopic(channel=channel["id"], topic=flox.meta.description)


@handle_exceptions
@with_slack
def create_user_group(flox: Flox, slack: WebClient, out, **kwargs):
    """Creates user group"""
    name = _name(flox)
    try:
        slack.usergroups_create(name=name, handle=slugify(name))
        out.success(f'User group "#{name}" created')
    except SlackApiError as e:
        if e.response.get("error") == "name_taken":
            out.info(f'User group "#{name}" already created')
        else:
            raise
