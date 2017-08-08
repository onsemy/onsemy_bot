import requests
from errbot import BotPlugin, botcmd

class RuliRight(BotPlugin):
    """
    루리웹 오른쪽
    """


    @botcmd
    def ruliweb_right(self, msg, args):
        """루리웹 오른쪽 베스트 20개"""
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
            
            self.send(send_id, title + ' - ' + link)
