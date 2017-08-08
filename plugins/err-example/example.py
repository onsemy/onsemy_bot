import requests
from errbot import BotPlugin, botcmd


class Example(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def tryme(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        return 'It *works* !'  # This string format is markdown.

    @botcmd
    def hello_card(self, msg, args):
        """Say a card in the chatroom."""
        result = requests.get(url = 'http://web.ruliweb.com/best/hit_history.htm')
        context = result.text
        context = context[context.find('right_best_list'):]
        link_begin_templ = "<a class='txt_link' href='"
        link_end_templ = "'>"
        strong_begin_templ = "<strong>"
        strong_end_templ = "</strong>"
        a_tag_end_templ = "</a>"

        # set send target
        send_id = msg.to
        if msg.to == self.bot_identifier:
            send_id = msg.frm

        for best in range(1, 20):
            title = ""
            context = context[context.find(link_begin_templ) + len(link_begin_templ):]
            link = context[:context.find(link_end_templ)]
            if context[:context.find(link_begin_templ)].find('<strong>') != -1:
                title = context[context.find(strong_begin_templ) + len(strong_begin_templ):context.find(strong_end_templ)]
            else:
                title = context[context.find(link_end_templ) + len(link_end_templ):context.find(a_tag_end_templ)]
            
                self.send_card(title=title,
                                link=link,
                                to=send_id)
