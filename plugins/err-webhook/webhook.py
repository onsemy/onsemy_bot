# coding: utf-8
import json
import os
from time import sleep
from errbot import BotPlugin, webhook

class WebHook(BotPlugin):
    _is_pushed = False
    _is_started = True

    def refresher(self):
        if self._is_started == True:
            self._is_started = False
            self.send(self.build_identifier(self._user_id), 'Yes, your majesty!')

        if self._is_pushed == True:
            # self.stop_poller(self.refresher)
            self._is_pushed = False
            self._is_started = True
            sleep(3)
            self.send(self.build_identifier(self._user_id), 'Restarting bot!')
            self.send(self.build_identifier(self._user_id), '/restart')

    def activate(self):
        with open('./plugins/err-webhook/settings.json', 'r') as d:
            jsonData = json.load(d)
            self._room_id = jsonData['room_id']
            self._user_id = jsonData['user_id']

        self.send(self.build_identifier(self._user_id), 'Yes, your majesty!')
        # self.start_poller(5, self.refresher)

        super().activate()
        
    @webhook('/github/', form_param = 'payload')
    def notification(self, payload):
        self.send(self.build_identifier(self._user_id), 'Commit on ' + payload['repository']['name'] + ' - ' + payload['compare'] + '\nCurrent Branch: ' + payload['ref'])
        # self.log.info('git pull start=== ' + os.getcwd())
        # os.system('git checkout master')
        os.system('git pull')
        self.send(self.build_identifier(self._user_id), 'Please order to /restart bot!')
        # self._is_pushed = True

    @webhook
    def say(self, request):
        self.log.debug(repr(request))
        self.send(
                self.build_identifier(self._room_id),
                "니들 안녕?",
            )
        return "OK"