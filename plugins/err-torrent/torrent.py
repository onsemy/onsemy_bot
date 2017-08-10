# coding: utf-8

import os
import requests
import bot_define
from errbot import BotPlugin, botcmd


class Torrent(BotPlugin):
    """
    Torrent Job only oNsemy
    """

    @botcmd  # flags a command
    def torrent(self, msg, args):  # a command callable with !tryme
        """
        url or magnet add (one by one)
        """
        send_id = msg.to
        if msg.to == self.bot_identifier:
            send_id = msg.frm

        if msg.frm != self.build_identifier(bot_define.BOT_ADMIN_ID):
            # deny!
            stream = self.send_stream_request(send_id, open(os.getcwd() + '/resources/deny_new.jpg', 'rb'), name = 'deny_new.jpg', stream_type = 'photo')
            return

        self.log.info('args: ' + args)
        validations = ['http://', 'magnet:', 'https://', 'bc://bt/']
        if all(not (val in args) for val in validations):
            stream = self.send_stream_request(send_id, open(os.getcwd() + '/resources/nooo.gif', 'rb'), name = 'nooo.gif', stream_type = 'document')
            return

        yield "Request Login"
        params = {'username':bot_define.TORRENT_USER_NAME, 'password':bot_define.TORRENT_PASSWORD}
        result = requests.post(bot_define.TORRENT_URL + 'login', params)
        if not result:
            yield "Failed to Login"
            return

        params = {'urls':args}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        yield "Request Torrent Job!"

        result = requests.post(bot_define.TORRENT_URL + 'command/download', params, headers = headers)

        if not result:
            yield "Something has wrong!"
            return

        yield "Result: " + result.status_code + " - " + result.reason
