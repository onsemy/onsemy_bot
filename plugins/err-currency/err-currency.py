import requests
import json
from datetime import date
from errbot import BotPlugin, botcmd

class Currency(BotPlugin):
    """
    환율
    """

    @botcmd
    def currency(self, msg, args):
        """모든 코인정보"""
        result = requests.get(url = 'https://api.bithumb.com/public/ticker/ALL')
        jsonObj = json.loads(result.text)
        data = jsonObj['data']
        main_title = date.fromtimestamp(data['date']).isoformat() + ' = 가상화폐 현황 =\n'

        # set send target
        send_id = msg.to
        if msg.to == self.bot_identifier:
            send_id = msg.frm

        send_content = main_title
        send_content += '\n[BTC]\n'
        send_content += '시작가격: ' + data['BTC']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['BTC']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['BTC']['min_price'] + '\n'
        send_content += '최고가격: ' + data['BTC']['max_price'] + '\n'
        send_content += '살때가격: ' + data['BTC']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['BTC']['sell_price'] + '\n'
        
        send_content += '\n[ETH]\n'
        send_content += '시작가격: ' + data['ETH']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['ETH']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['ETH']['min_price'] + '\n'
        send_content += '최고가격: ' + data['ETH']['max_price'] + '\n'
        send_content += '살때가격: ' + data['ETH']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['ETH']['sell_price'] + '\n'
        
        send_content += '\n[DASH]\n'
        send_content += '시작가격: ' + data['DASH']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['DASH']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['DASH']['min_price'] + '\n'
        send_content += '최고가격: ' + data['DASH']['max_price'] + '\n'
        send_content += '살때가격: ' + data['DASH']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['DASH']['sell_price'] + '\n'
        
        send_content += '\n[LTC]\n'
        send_content += '시작가격: ' + data['LTC']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['LTC']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['LTC']['min_price'] + '\n'
        send_content += '최고가격: ' + data['LTC']['max_price'] + '\n'
        send_content += '살때가격: ' + data['LTC']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['LTC']['sell_price'] + '\n'
        
        send_content += '\n[ETC]\n'
        send_content += '시작가격: ' + data['ETC']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['ETC']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['ETC']['min_price'] + '\n'
        send_content += '최고가격: ' + data['ETC']['max_price'] + '\n'
        send_content += '살때가격: ' + data['ETC']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['ETC']['sell_price'] + '\n'
        
        send_content += '\n[XRP]\n'
        send_content += '시작가격: ' + data['XRP']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['XRP']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['XRP']['min_price'] + '\n'
        send_content += '최고가격: ' + data['XRP']['max_price'] + '\n'
        send_content += '살때가격: ' + data['XRP']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['XRP']['sell_price'] + '\n'
        
        send_content += '\n[BCH]\n'
        send_content += '시작가격: ' + data['BCH']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['BCH']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['BCH']['min_price'] + '\n'
        send_content += '최고가격: ' + data['BCH']['max_price'] + '\n'
        send_content += '살때가격: ' + data['BCH']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['BCH']['sell_price'] + '\n'
        
        send_content += '\n[XMR]\n'
        send_content += '시작가격: ' + data['XMR']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['XMR']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['XMR']['min_price'] + '\n'
        send_content += '최고가격: ' + data['XMR']['max_price'] + '\n'
        send_content += '살때가격: ' + data['XMR']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['XMR']['sell_price'] + '\n'
        
        send_content += '\n[ZEC]\n'
        send_content += '시작가격: ' + data['ZEC']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['ZEC']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['ZEC']['min_price'] + '\n'
        send_content += '최고가격: ' + data['ZEC']['max_price'] + '\n'
        send_content += '살때가격: ' + data['ZEC']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['ZEC']['sell_price'] + '\n'
        
        send_content += '\n[QTUM]\n'
        send_content += '시작가격: ' + data['QTUM']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['QTUM']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['QTUM']['min_price'] + '\n'
        send_content += '최고가격: ' + data['QTUM']['max_price'] + '\n'
        send_content += '살때가격: ' + data['QTUM']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['QTUM']['sell_price'] + '\n'
        
        send_content += '\n[BTG]\n'
        send_content += '시작가격: ' + data['BTG']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['BTG']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['BTG']['min_price'] + '\n'
        send_content += '최고가격: ' + data['BTG']['max_price'] + '\n'
        send_content += '살때가격: ' + data['BTG']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['BTG']['sell_price'] + '\n'
        
        send_content += '\n[EOS]\n'
        send_content += '시작가격: ' + data['EOS']['opening_price'] + '\n'
        send_content += '마감가격: ' + data['EOS']['closing_price'] + '\n'
        send_content += '최저가격: ' + data['EOS']['min_price'] + '\n'
        send_content += '최고가격: ' + data['EOS']['max_price'] + '\n'
        send_content += '살때가격: ' + data['EOS']['buy_price'] + '\n'
        send_content += '팔때가격: ' + data['EOS']['sell_price'] + '\n'
        
        self.send(send_id, send_content)
        
