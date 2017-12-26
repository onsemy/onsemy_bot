# coding: utf-8

import requests
import json
from errbot import BotPlugin, botcmd

class HanRiver(BotPlugin):
    HANRIVER_URL = 'http://hangang.dkserver.wo.tc'
    def temp_request(self):
        result = requests.get(url = self.HANRIVER_URL)
        content = json.loads(result.text)
        
        return content['temp']

    def callback_message(self, mess):
        if mess.body.find('한강') != -1 or \
                mess.body.find('자살') != -1 or \
                mess.body.find('주식') != -1 or \
                mess.body.find('부동산') != -1 or \
                mess.body.find('코인') != -1:
            result = self.temp_request()

            target = mess.to
            if mess.to == self.bot_identifier:
                target = mess.frm

            self.send(target, "지금 한강물 " + result + "도야")
