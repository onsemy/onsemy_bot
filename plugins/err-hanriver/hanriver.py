# coding: utf-8
from errbot import BotPlugin, botcmd

class HanRiver(BotPlugin):
    def callback_message(self, mess):
        if mess.body.find('한강물') != -1:
            return "아직 준비중이에양..."