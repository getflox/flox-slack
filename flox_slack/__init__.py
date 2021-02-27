from flox_slack.configure import SlackConfiguration
from flox_slack.project import create_channel, create_user_group, set_channel_topic
from floxcore.command import Stage
from floxcore.context import Flox
from floxcore.plugin import Plugin


class SlackPlugin(Plugin):
    def configuration(self):
        return SlackConfiguration()

    def handle_project(self, flox: Flox):
        return [
            Stage(create_channel, require=["slack.create_channel"]),
            Stage(set_channel_topic, require=["slack.create_channel"]),
            Stage(create_user_group, require=["slack.create_group"])
        ]


def plugin():
    return SlackPlugin()
