import requests
from errbot import BotPlugin, botcmd

class Ranking(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    _GOOGLE_TOP_SELL_URL = 'https://play.google.com/store/apps/category/GAME/collection/topgrossing'

    @botcmd  # flags a command
    def rank_and_sell(self, msg, args):  # a command callable with !tryme
        """
        Android Top Selling Rank
        """
        # TODO: http.get
        result = requests.get(url = self._GOOGLE_TOP_SELL_URL)
        content = result.text
        send_content = 'Google Game Top 20\n'

        # TODO: pattern parsing
        for num in range(1, 20):
            content = content[(content.find('<img alt="') + 10):]
            send_content += str(num) + '위 ' + content[:content.find('"')] + '\n'

        # TODO: sort

        # TODO: send
        return send_content
