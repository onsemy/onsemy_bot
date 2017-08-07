# coding: utf-8
import json
import os
from errbot import BotPlugin, webhook

class PluginExample(BotPlugin):
    def activate(self):
        with open('./plugins/err-webhook/settings.json', 'r') as d:
            jsonData = json.load(d)
            self._room_id = jsonData['room_id']
            self._user_id = jsonData['user_id']

        super().activate()

    @webhook('/github/', form_param = 'payload')
    def notification(self, payload):
        self.send(self.build_identifier(self._user_id), 'Commit on %s!' % payload['repository']['name'],)
        os.system('git pull')
        self.send(self.bot_identifier(), '/restart')
        # for room in self.bot_config.CHATROOM_PRESENCE:
        #     self.send(
        #         self.build_identifier(room),
        #         'Commit on %s!' % payload['repository']['name'],
        #     )

    @webhook
    def say(self, request):
        self.log.debug(repr(request))
        self.send(
                self.build_identifier(self._room_id),
                "니들 안녕?",
            )
        return "OK"