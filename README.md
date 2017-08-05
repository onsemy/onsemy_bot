oNsemy Bot
===========
Telegram Bot for oNsemy

# Requirements

* python 3.x+
* pyenv + pyenv-virtualenv
* errbot
* python-telegram-bot
* requests

# Settings

## bot_define.py (in `$BOT_HOME_DIR`)

```python
TELEGRAM_BOT_TOKEN = '012345678:AA..' # Telegram Bot Token
BOT_HOME_DIR = r'/path/to/ERRBOT_ROOT' # Must Input Full Path

BOT_ADMIN_ID = 123456789 # Your Telegram ID(num) -> /whoami
```

## win_whitelist.txt (in `$BOT_HOME_DIR/plugins/err-messagehook`)

```
WANT_POLITICS_KEYWORD1
WANT_POLITICS_KEYWORD2
...
```

## nesi_list.txt (in `$BOT_HOME_DIR/plugins/err-messagehook`)

cause group(rooms) is not supported in errbot-telegram (...)

```
CHATROOM_ID1
CHATROOM_ID2
...
```

# Features

* '아무나 이겨라' (talking about Politics)
* HanRiver Temperature
* '~해줘' (feat. 블랙워그레이몬)
* '공유' (feat. 공유)
* '퇴근하게?' (feat. 코딩해야지?)
* Clock Notification (+Do not disturb)
* 지름 응원 기능
* 포돌이

# Working Features

* Android/iOS Game Ranking
* Hidden Func...?
* Misc.
