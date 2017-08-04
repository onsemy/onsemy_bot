# coding: utf-8

import requests

from errbot import BotPlugin, botcmd

class HanRiver(BotPlugin):
    HANRIVER_URL = 'http://water.nier.go.kr/main/mainContent.do'
    def temp_request(self):
        result = requests.get(url = self.HANRIVER_URL)
        content = result.text
        find_idx = content.find('map_tit">노량진')
        content = content[find_idx:]
        find_idx = content.find('<th>수온(℃)</th>')
        content = content[find_idx:]
        find_idx = content.find('<td>')
        content = content[find_idx:]
        find_idx = content.find('</td>')
        content = content[4:find_idx].strip()

        return content

    def callback_message(self, mess):
        if mess.body.find('한강물') != -1:
            result = self.temp_request()

            target = mess.to
            if mess.to == self.bot_identifier:
                target = mess.frm

            self.send(mess.to, "지금 한강물 " + result + "도야")                