# coding: utf-8

import bot_define

from errbot import BotPlugin, botcmd

class HanRiver(BotPlugin):
    def callback_message(self, mess):
        if mess.body.find('한강물') != -1:
            if mess.to != self._bot:
                self.send(mess.to, "아직 준비중이에양...")