# coding: utf-8
from errbot import BotPlugin, botcmd

class MessageHook(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """
    _data_list = list()

    def activate(self):
        with open('./plugins/err-messagehook/win_whitelist.txt', 'r') as f:
            self._data_list = f.read().splitlines()
            f.close()
        self.log.info(self._data_list)
        super().activate()

    def callback_message(self, mess):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        self.log.info('it is work?')
        self.log.info(self._data_list)
        for data in self._data_list:
            self.log.info('white data: ' + data)
            if mess.body.find(data) != -1:
                self.send(mess.to, "아무나 이겨라")
                return
