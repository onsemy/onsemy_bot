# coding: utf-8
import os
import datetime
import random
import json

from errbot import BotPlugin, botcmd

class MessageHook(BotPlugin):
    """
    메시지에서 적절한 짤방을 생산한다
    """
    _data_list = list()
    _send_group_list = list()

    def nesi_timer(self):
        now = datetime.datetime.now();
        
        ### 정각 알림은 임시로 봉인
        # if now.minute == 0:
        #     if now.hour != 16 and now.hour > 6 and now.hour < 23:
        #         for data in self._send_group_list:
        #             self.send(self.build_identifier(data), str(now.hour) + '시에양-!')

        if now.minute == 4:
            for data in self._data["nesi_timer"]:
                if data["hour"] == now.hour % 12:
                    file_count = len(data["file_name"])
                    file_name = data["file_name"][random.randrange(0, file_count)]
                    for group in self._data["group_list"]:
                        self.send_stream_request(self.build_identifier(group), open(os.getcwd() + '/resources/' + file_name, 'rb'), name = file_name, stream_type = 'photo')
                    
            # if now.hour == 4 or now.hour == 16:
            #     for data in self._send_group_list:
            #         if random.random() < 0.5:
            #             self.send_stream_request(self.build_identifier(data), open(os.getcwd() + '/resources/nesi.jpg', 'rb'), name = 'nesi.jpg', stream_type = 'photo')
            #         else:
            #             self.send_stream_request(self.build_identifier(data), open(os.getcwd() + '/resources/naesi.jpeg', 'rb'), name = 'naesi.jpg', stream_type = 'photo')
            # if now.hour == 2 or now.hour == 14:
            #     for data in self._send_group_list:
            #         self.send_stream_request(self.build_identifier(data), open(os.getcwd() + '/resources/doosi.jpeg', 'rb'), name = 'doosi.jpg', stream_type = 'photo')

        self.log.info('타이머는 돌고있다!')

    def message_filter(self, send_id, mess, func_name:str, stream_type:str = 'photo'):
        """
        특정 키워드를 판별하여 적절한 짤을 보내는 함수
        정의는 filter.json 에 되어있음
        """
        data = self._data[func_name]
        for word in data["filter"]:
            if mess.body.find(word) != -1:
                file_count = len(data["file_name"])
                file_name = data["file_name"][random.randrange(0, file_count)]                    
                self.send_stream_request(send_id, open(os.getcwd() + '/resources/' + file_name, 'rb'), name = file_name, stream_type = stream_type)
                return True

        return False

    def activate(self):
        ### feature - filter load
        with open('./plugins/err-messagehook/filter.json') as data_file:
            self._data = json.load(data_file)
            self.log.info(self._data)
            data_file.close()

        # ### feature - Prepare Politics Talk
        # with open('./plugins/err-messagehook/win_whitelist.txt', 'r') as f:
        #     self._data_list = f.read().splitlines()
        #     f.close()
        # #####

        # ### feature - Prepare nesi timer
        # with open('./plugins/err-messagehook/nesi_list.txt', 'r') as f:
        #     self._send_group_list = f.read().splitlines()
        #     f.close()
        # #####

        self.start_poller(60, self.nesi_timer)

        super().activate()

    def callback_message(self, mess):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """

        # set send target
        send_id = mess.to
        if mess.to == self.bot_identifier:
            send_id = mess.frm

        for filter in self._data["message_filter"]:
            if self.message_filter(send_id, mess, filter["filter_name"]) == True:
                return

        # feature - Politics Talk
        for data in self._data['win_whitelist']:
            if mess.body.find(data) != -1:
                self.send(send_id, "아무나 이겨라")
                return # only once say
