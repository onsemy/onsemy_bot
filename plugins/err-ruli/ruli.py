import requests
from errbot import BotPlugin, botcmd

class Ruli(BotPlugin):
    """
    루리웹 각종 정보
    """

    @botcmd
    def ruliweb_news(self, msg, args):
        """루리웹 뉴스"""
        result = requests.get(url = 'http://bbs.ruliweb.com/news')
        context = result.text
        context = context[context.find('best_news_tab'):]
        outer_tag = 'list tab_box_page dot'
        item_start_tag = 'http://'
        item_end_tag = '">'
        title_end_tag = '</a>'
        main_title = {0:'PC/온라인', 1:'콘솔', 2:'모바일'}

        # set send target
        send_id = msg.to
        if msg.to == self.bot_identifier:
            send_id = msg.frm

        send_content = ''
        for best in range(1, 31):
            if best % 10 == 1:
                send_content += '[' + main_title[(int)(best / 10)] + ']\n\n'

            context = context[context.find(item_start_tag):]
            link = context[context.find(item_start_tag):context.find(item_end_tag)]
            sub_title = context[context.find(item_end_tag) + len(item_end_tag):context.find(title_end_tag)]
            context = context[context.find(title_end_tag):]

            send_content += '- ' + sub_title + ' - ' + link + '\n'
            if best % 10 == 0:
                self.send(send_id, send_content)                
                send_content = ''

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

        send_content = "[근근웹 오른쪽 베스트 20]\n"
        for best in range(1, 20):
            title = ""
            context = context[context.find(link_begin_templ) + len(link_begin_templ):]
            link = context[:context.find(link_end_templ)]
            if context[:context.find(link_begin_templ)].find('<strong>') != -1:
                title = context[context.find(strong_begin_templ) + len(strong_begin_templ):context.find(strong_end_templ)]
            else:
                title = context[context.find(link_end_templ) + len(link_end_templ):context.find(a_tag_end_templ)]
            
            send_content += '- ' + title + ' - ' + link + '\n'

            if best % 10 == 9: # 두번에 걸쳐서 보내도록...
                self.send(send_id, send_content)
                send_content = ''
            
        # self.send(send_id, send_content)
