# coding: utf-8

import os
import requests
import bot_define
from errbot import BotPlugin, botcmd
from qbittorrent import Client


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

        qb = Client(bot_define.TORRENT_URL)

        yield "Request Login"

        res = qb.login(bot_define.TORRENT_USER_NAME, bot_define.TORRENT_PASSWORD)

        if not res:
            yield "Failed to Login"
            return

        yield "Request Torrent Job!"

        res = qb.download_from_link(args)
        
        if not res:
            yield "Something has wrong!"
            return

        stream = self.send_stream_request(send_id, open(os.getcwd() + '/resources/sloth.gif', 'rb'), name = 'sloth.gif', stream_type = 'document')
        yield "Request Done."
        qb.logout()
