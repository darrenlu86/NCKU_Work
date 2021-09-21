#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:34:39 2020

@author: shaomingLu
"""

import requests
import random

# 提醒喝水產生器


def CareWord():
    r = random.randint(0, 9)
    word = ["hohoho,寶貝開喝水摟！不然會變成木乃伊喔",
            "賣偷睏喔～喝杯水打起精神",
            "喝水！不然偶就要餵妳一堆我的口水",
            "寶貝對不起～請妳快喝水～不要讓我傷心",
            "娘娘，您今天喝水了嗎？",
            "公主，您的水在您的水壺裡，記得要喝喔",
            "不要再給我喝茉莉蜜茶了喔！給我喝水",
            "寶貝今天要喝水20公升，不要忘記了喔",
            "我剛剛收集了大概300毫升的口水，您請慢用",
            "今天，妳想來點口對口的餵水嗎？寶貝快喝！",
            ]
    return word[r]

# LineNotify處理


def LineNotify(token, msg, stickerPackageId, stikerId):

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': "\n\n" + msg,
               'stickerPackageId': stickerPackageId, 'stickerId': stikerId}

    po = requests.post("https://notify-api.line.me/api/notify",
                       headers=headers, data=payload)

    print(po.status_code)


thisword = CareWord()
stickerPackageId = 6362
stikerId = 11087927
token = "ITUpAgiirKVK9Ep9tQ4Uno3DrZKNkG7xYaihka4hHaf"

LineNotify(token, thisword, stickerPackageId, stikerId)
