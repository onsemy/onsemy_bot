# coding: utf-8

import requests
import json
from errbot import BotPlugin, botcmd

class NaverHotKeyword(BotPlugin):    
    SEARCH_START = 'oRTK : '
    SEARCH_END = '}\n]\n}'
    RANK_URL = 'https://m.naver.com'

    def temp_request(self):
        result = requests.get(self.RANK_URL)
        content = result.text

        find_start_idx = content.find(self.SEARCH_START) + len(self.SEARCH_START)
        find_end_idx = content.find(self.SEARCH_END) + len(self.SEARCH_END)
        search_result = content[find_start_idx:find_end_idx]

        jsondata = json.loads(search_result)
        
        rank = 0
        rankText = ''
        for data in jsondata['d']:
            rank += 1
            rankText += '%d위 %s\n' % (rank, data['k'])

        return rankText

    def callback_message(self, mess):
        if mess.body.find('네이버실시간') != -1:
            result = self.temp_request()

            target = mess.to
            if mess.to == self.bot_identifier:
               target = mess.frm

            self.send(target, result)