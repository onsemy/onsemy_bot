# coding: utf-8
import os
import datetime

from errbot import BotPlugin, botcmd

class MessageHook(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """
    _data_list = list()
    _send_group_list = list()

    def nesi_timer(self):
        now = datetime.datetime.now();
        if now.minute == 0:
            if now.hour == 4 or now.hour == 16:
                for data in self._send_group_list:
                    self.send_stream_request(self.build_identifier(data), open(os.getcwd() + '/resources/nesi.jpg', 'rb'), name = 'nesi.jpg', stream_type = 'photo')
            elif now.hour > 6 and now.hour < 23:
                for data in self._send_group_list:
                    self.send(self.build_identifier(data), str(now.hour) + '시에양-!')
        self.log.info('타이머는 돌고있다!')

    def activate(self):
        ### feature - Prepare Politics Talk
        with open('./plugins/err-messagehook/win_whitelist.txt', 'r') as f:
            self._data_list = f.read().splitlines()
            f.close()
        #####

        ### feature - Prepare nesi timer
        with open('./plugins/err-messagehook/nesi_list.txt', 'r') as f:
            self._send_group_list = f.read().splitlines()
            f.close()
        #####

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

        # feature - ~해줘 (feat. 블랙워그레이몬)
        if mess.body.find('해줘') != -1 or mess.body.find('해줭') != -1 or mess.body.find('부탁') != -1:
            self.send_stream_request(send_id, open(os.getcwd() + '/resources/deny_new.jpg', 'rb'), name = 'deny_new.jpg', stream_type = 'photo')
            return

        # feature - 퇴근 (어딜가)
        if mess.body.find('퇴근') != -1 \
                or mess.body.find('자러') != -1 \
                or mess.body.find('자야') != -1 \
                or mess.body.find('잔다') != -1:
            self.send_stream_request(send_id, open(os.getcwd() + '/resources/where_you_go.jpg', 'rb'), name = 'where_you_go.jpg', stream_type = 'photo')
            return

        # feature - 네시 (어딜가)
        if mess.body.find('네시') != -1 or mess.body.find('4시') != -1:
            self.send_stream_request(send_id, open(os.getcwd() + '/resources/nesi.jpg', 'rb'), name = 'nesi.jpg', stream_type = 'photo')
            return

        # feature - 공유
        if mess.body.find('공유') != -1:
            self.send_stream_request(send_id, open(os.getcwd() + '/resources/0u.jpg', 'rb'), name = '0u.jpg', stream_type = 'photo')
            return

        # feature - 지름
        if mess.body.find('질러') != -1 or \
                mess.body.find('지름') != -1:
            self.send_stream_request(send_id, open(os.getcwd() + '/resources/buybuybuy.gif', 'rb'), name = 'buybuybuy.gif', stream_type = 'photo')
            return

        # feature - Politics Talk
        for data in self._data_list:
            if mess.body.find(data) != -1:
                self.send(send_id, "아무나 이겨라")
                return # only once say
