from typing import Tuple

from floxcore.config import Configuration, ParamDefinition


class SlackConfiguration(Configuration):
    def parameters(self) -> Tuple[ParamDefinition, ...]:
        return (
            ParamDefinition("create_channel", "Creates channel for project", boolean=True, default=True),
            ParamDefinition("private_channel", "Should newly created channel be private?", boolean=True, default=False),
            ParamDefinition("create_group", "Should user group be created?", boolean=True, default=True),
            ParamDefinition("prefix", "Prefix used for channel/user group name", default=""),
            ParamDefinition("name", "Fixed name for channel/user group", default=""),
        )

    def secrets(self) -> Tuple[ParamDefinition, ...]:
        return (
            ParamDefinition("token", "Slack Access Token", secret=True),
        )

    def schema(self):
        pass
