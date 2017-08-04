# coding: utf-8
from errbot import BotPlugin, botcmd

class HanRiver(BotPlugin):
    def callback_message(self, mess):
        self.send(mess.to, "아직 준비중이에양...")