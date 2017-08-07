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

## filter.txt (in `$BOT_HOME_DIR/plugins/err-messagehook`)

```json
{
    "nesi_timer":[
        {
            "hour":2,
            "file_name":[
                "doosi.jpeg"
            ]
        },
        {
            "hour":4,
            "file_name":[
                "nesi.jpg",
                "naesi.jpeg"
            ]
        }
    ],
    "win_whitelist":[
        "문",
        "안",
        "홍",
        "유",
        "심",
        "박",
        "이",
        ...
    ],
    "group_list":[
        CHATROOM_ID1,
        CHATROOM_ID2,
        ...
    ],
    "message_filter":[
        {
            "filter_name":"FILTER_NAME",  
            "file_name":[
                "WANT_TO_SEND_FILE_NAME1",
                "WANT_TO_SEND_FILE_NAME2",
                ...
            ],
            "stream_type":"TELEGRAM_STREAM_TYPE",
            "filter":[
                "FILTER_WORD1",
                "FILTER_WORD2",
                ...
            ]
        },
        ...
    ]
}
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
* Android Game Ranking

# Working Features

* iOS Game Ranking
* Hidden Func...?
* Misc.
