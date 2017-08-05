from errbot import BotPlugin, botcmd


class Ranking(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def rank_and_sell(self, msg, args):  # a command callable with !tryme
        """
        Android Top Selling Rank
        """
        # TODO: http.get

        # TODO: pattern parsing

        # TODO: sort

        # TODO: send
        return 'It *works* !'  # This string format is markdown.
