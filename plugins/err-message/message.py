# coding: utf-8
from errbot import BotPlugin, botcmd

class Message(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    dataList = []

    def activate(self):
        with open('./plugins/err-message/win_whitelist.txt', 'r') as f:
            dataList = f.read().splitlines()
        self.log.info(dataList)
        super().activate()

    @botcmd  # flags a command
    def callback_message(self, mess):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        self.log.info(dataList)
        for data in dataList:
            self.log.info('white data: ' + data)
            if mess.body.find(data) != -1:
                self.send(mess.to, "아무나 이겨라")
                return
