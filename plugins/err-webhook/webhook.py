# coding: utf-8
import json
from errbot import BotPlugin, webhook

class PluginExample(BotPlugin):
    def activate(self):
        with open('./plugins/err-webhook/settings.json', 'r') as d:
            jsonData = json.load(d)
            self._room_id = jsonData['room_id']

        super().activate()

    @webhook
    def notification(self, payload):
        for room in self.bot_config.CHATROOM_PRESENCE:
            self.send(
                self.build_identifier(room),
                'Commit on %s!' % payload['repository']['name'],
            )

    @webhook
    def say(self, request):
        self.log.debug(repr(request))
        self.send(
                self.build_identifier(self._room_id),
                "니들 안녕?",
            )
        return "OK"