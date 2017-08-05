import requests
from errbot import BotPlugin, botcmd

class Ranking(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    _GOOGLE_TOP_SELL_URL = 'https://play.google.com/store/apps/category/GAME/collection/topgrossing'
    _GOOGLE_TOP_PAID_URL = 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid'
    _GOOGLE_TOP_FREE_URL = 'https://play.google.com/store/apps/category/GAME/collection/topselling_free'

    def content_parse(self, content:str, start_idx:int = 1, end_idx:int = 21):
        send_content = ''

        # TODO: pattern parsing
        for num in range(start_idx, end_idx):
            content = content[(content.find('<img alt="') + 10):]
            send_content += str(num) + '위 ' + content[:content.find('"')] + '\n'

        return send_content

    @botcmd  # flags a command
    def rank_and_sell(self, msg, args):  # a command callable with !tryme
        """
        Android Top Selling Rank
        """
        # TODO: http.get
        result = requests.get(url = self._GOOGLE_TOP_SELL_URL)
        content = result.text
        send_content = 'Google Selling Game Top 20\n'

        # TODO: send
        return self.content_parse(content = content)

    @botcmd  # flags a command
    def rank_and_paid(self, msg, args):  # a command callable with !tryme
        """
        Android Top Paid Rank
        """
        # TODO: http.get
        result = requests.get(url = self._GOOGLE_TOP_PAID_URL)
        content = result.text
        send_content = 'Google Paid Game Top 20\n'

        # TODO: send
        return self.content_parse(content = content)

    @botcmd  # flags a command
    def rank_and_free(self, msg, args):  # a command callable with !tryme
        """
        Android Top Free Rank
        """
        # TODO: http.get
        result = requests.get(url = self._GOOGLE_TOP_FREE_URL)
        content = result.text
        send_content = 'Google Free Game Top 20\n'

        # TODO: send
        return self.content_parse(content = content)
