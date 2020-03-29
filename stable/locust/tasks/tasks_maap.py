#!/usr/local/bin/python
#-*- coding: utf-8 -*-
import sys
from time import time
from datetime import date
import datetime as pydatetime
from locust import HttpLocust, TaskSet
from uuid import uuid4
import json
import requests
from datetime import datetime
import random
import socket


# def logout(l):
#     l.client.post("/logout", {"username":"ellen_key", "password":"education"})

def get_rand_contact_num():
    cluster = random.randint(0, 1)
    if cluster == 0:
        r = random.randint(821700000000, 821700500000)
    else:
        r = random.randint(821701000000, 821701500000)
    return "+%d" % (r)
    # return '+821020953338'


def send_lms(l):
    l.client.post("/v1/messages/",
        headers=get_header(),
        data=json.dumps({
        'agcMsgId': uuid4().hex,
        'body': {
            'title': '성능테스트 title',
            'description': 'SKT 실패_테스트 ' + uuid4().hex
        },
        'chatbotId': 'skt_a2p_test',
        'userContact': get_rand_contact_num(),
        'expiryOption': 1,
        'footer': '실패테스트',
        'groupId': 't1_sms_fail',
        'header': 'header',
        'messagebaseId': 'fmt.l.002',
        'productCode': 'tmplt',
        'agencyId': 'samsung'
    }))

def send_mms(l):
    l.client.post("/ag/1.1/message",
        headers=get_header(),
        data=json.dumps({
        'clientMsgId': uuid4().hex,
        'body': {
            "title1": "tttt223",
            "image1": "maapfile://skt_img_43",
          	"description2": "dddddddd",
          	"title2": "tttt",
            "image2": "maapfile://skt_img_43",
          	"description3": "dddddddd",
          	"title3": "tttt",
            "image3": "maapfile://skt_img_43"
        },
        'chatbotId': '18994030',
        'userContact': '+2300000011',
        'expiryOption': 1,
        'footer': '성능테스트중입니다',
        'groupId': 'locust',
        'header': 0,
        'footer': '1555-1111',
        'messagebaseId': 'mb_test_mms_145',
        'productCode': 'mms',
        'agencyId': 'skt_reseller_test',
        "buttons": [
            {
              "suggestions": [
                {
                  "action": {
                    "urlAction": {
                      "openUrl": {
                        "url": "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=P&cardWcd=ME2&eventCode=CHT03"
                      }
                    },

                    "displayText": "자세히 보기"
                  }
                }
              ]
            },
            {
              "suggestions": [
                {
                  "action": {
                    "urlAction": {
                      "openUrl": {
                        "url": "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=P&cardWcd=MPE2&eventCode=CHT03"
                      }
                    },
                    "displayText": "자세히 보기"
                  }
                },
                {
                  "action": {
                    "mapAction": {
                        "showLocation": {
        	              "location": {
        	                "query": "SK텔레콤"
                          },
                        "fallbackUrl": "https://www.google.com/maps/search/SK텔레콤"
                      }
                    },
                    "displayText": "지도에서 상호 찾기",
                    "postback": {
                      "data": "set_by_chatbot_search_location_test_smsmo_true"
                    }
                  }
                }
              ]
            },
            {
              "suggestions": [
                {
                  "action": {
                    "urlAction": {
                      "openUrl": {
                        "url": "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=C&cardWcd=XE2&eventCode=CHT03"
                      }
                    },
                    "displayText": "자세히 보기",
                    "postback": {
                      "data": "set_by_chatbot_open_url"
                    }
                  }
                }
              ]
            }
        ]
    }))


def send_bulk(l):
    r = l.client.post("/perf/10x",
        headers=get_header(),
        data=json.dumps({
        'clientMsgId': '',
        'body': {
            "title1": "tttt223",
            "image1": "maapfile://skt_img_43",
          	"description2": "dddddddd",
          	"title2": "tttt",
            "image2": "maapfile://skt_img_43",
          	"description3": "dddddddd",
          	"title3": "tttt",
            "image3": "maapfile://skt_img_43"
        },
        'chatbotId': '18994030',
        'userContact': '+2300000011',
        'expiryOption': 1,
        'footer': '성능테스트중입니다',
        'groupId': 'locust',
        'header': 0,
        'footer': '1555-1111',
        'messagebaseId': 'mb_test_mms_145',
        'productCode': 'mms',
        'agencyId': 'skt_reseller_test',
        "buttons": [
            {
              "suggestions": [
                {
                  "action": {
                    "urlAction": {
                      "openUrl": {
                        "url": "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=P&cardWcd=ME2&eventCode=CHT03"
                      }
                    },

                    "displayText": "자세히 보기"
                  }
                }
              ]
            },
            {
              "suggestions": [
                {
                  "action": {
                    "urlAction": {
                      "openUrl": {
                        "url": "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=P&cardWcd=MPE2&eventCode=CHT03"
                      }
                    },
                    "displayText": "자세히 보기"
                  }
                },
                {
                  "action": {
                    "mapAction": {
                        "showLocation": {
        	              "location": {
        	                "query": "SK텔레콤"
                          },
                        "fallbackUrl": "https://www.google.com/maps/search/SK텔레콤"
                      }
                    },
                    "displayText": "지도에서 상호 찾기",
                    "postback": {
                      "data": "set_by_chatbot_search_location_test_smsmo_true"
                    }
                  }
                }
              ]
            },
            {
              "suggestions": [
                {
                  "action": {
                    "urlAction": {
                      "openUrl": {
                        "url": "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=C&cardWcd=XE2&eventCode=CHT03"
                      }
                    },
                    "displayText": "자세히 보기",
                    "postback": {
                      "data": "set_by_chatbot_open_url"
                    }
                  }
                }
              ]
            }
        ]
    }))
    print(r)


def query_capa(l):
    params = {'userContact': '%2B8210209708351'}
    l.client.get("/v1/capability",
                 headers=get_header(), params=params)



def sqs_perf_test(l):
    l.client.get("/api/health/stress/queue")


def query_capa(l):
    params = {'userContact': '%2B8210209708351'}
    l.client.get("/v1/capability",
        headers=get_header(), params=params)

def send_file(l):
    l.client.post("/v1/file/",
        headers={
            "Authorization": "Bearer " + bearer_token,
            "Content-Type": "multipart/form-data"
        },
        files={'file': open('./test.png', 'rb')},
    )

Envs = {
    "dev":[
        {'agency_id': 'sktperf',
            'secret_key': '2c112d50d61e47505ea1016e8d2f47e7d12de08746cb4b5b4fc00d9c0469428e',
            'chatbot_id': '15812347',
            'userContact': '+23000011',
            'groupId': 'skt.mlt',
            'agencyId': 'skt_reseller_test',
            'messagebaseId.sms': 'mb_test_sms',
         },
    ],
    "stg": [
        {'agency_id': 'sktstgperf',
         'secret_key': '68453eba23fb4c98a0a71d462ec14b222c952ee78ae24159abd0becd73af4cb7',
         'chatbot_id': '99991235',
         'userContact': '+23000011',
         'groupId': 'skt.mlt',
         'agencyId': 'skt_reseller_test',
         'messagebaseId.sms': 'mb_test_sms_968',
         'messagebaseId.SS': 'SS000000',
         },
    ],
}

DEBUG = False
Curent_Env = None
# bearer_token = None
bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJTS1QiLCJhZ2VuY3lJZCI6InNrdHN0Z3BlcmYiLCJzY29wZXMiOiJST0xFU19BR0VOQ1kiLCJleHAiOjE1ODUzNjU0MDN9.9TBI-jxaokUoGcCN27ZkCVwGmTun_-ljl4INqw9zqSw"
def get_access_token(l):
    payload = "{\n  \"clientId\": \"%s\",\n  \"clientSecret\": \"%s\",\n  \"grantType\": \"clientCredentials\"\n}"\
              % (Curent_Env['agency_id'],\
              Curent_Env['secret_key'])
    resp = l.client.post("/ag/1.1/token", headers={'Content-Type': "application/json"}, data=payload)
    printf(resp.json())
    global bearer_token
    bearer_token = resp.json()['data']['tokenInfo']['accessToken']


def getClientMsgId():
    # return "%s_%s_%s" % (socket.gethostname(), time(), uuid4().hex)
    # return "%s%s" % (date.today().strftime("%y%m%d"), uuid4().hex)
    return "%s%s" % (pydatetime.datetime.now().strftime("%H%M%S"), uuid4().hex)

def get_header():
    return {
        "Authorization": "Bearer " + bearer_token,
        "Content-Type": "application/json"
    }

def send_sms(l):
    resp = l.client.post('/ag/1.1/message',
    headers=get_header(),
    data=json.dumps({
      'clientMsgId': getClientMsgId(),
      'chatbotId': Curent_Env['chatbot_id'],
      'userContact': Curent_Env['userContact'],
      'expiryOption': 1,
      'groupId': Curent_Env['groupId'],
      'header': 0,
      'footer': '010-6444-0681',
      'messagebaseId': Curent_Env['messagebaseId.sms'],
      'productCode': 'sms',
      'agencyId': Curent_Env['agencyId'],
      'body': {
          'description': '[oms1226] 안녕하세요? 스트레스 테스트 메시지 발송시간: ' + str(pydatetime.datetime.now())
      },
    }))
    printf(resp.json())


def send_SS(l):
    resp = l.client.post('/ag/1.1/message',
    headers=get_header(),
    data=json.dumps({
        'clientMsgId': getClientMsgId(),
        'chatbotId': Curent_Env['chatbot_id'],
        'userContact': Curent_Env['userContact'],
        'expiryOption': 1,
        'groupId': Curent_Env['groupId'],
        'header': 0,
        'footer': '010-6444-0681',
        'messagebaseId': Curent_Env['messagebaseId.SS'],
        'agencyId': Curent_Env['agencyId'],
        "body": {
            "description": '[oms1226] 안녕하세요? 스트레스 테스트 메시지 발송시간: ' + str(pydatetime.datetime.now()),
        },
        "buttons": [
            {
                "suggestions": [
                    {
                        "action": {
                            "urlAction": {
                                "openUrl": {
                                    "url": "https://play.google.com/store/apps/details?id=com.starbucks.co&hl=ko"
                                }
                            },
                            "displayText": "스타벅스 앱",
                            "postback": {
                                "data": "set_by_chatbot_open_url"
                            }
                        }
                    }
                ]
            }
        ],
    }))
    printf(resp.json())


class UserBehavior(TaskSet):
    # tasks = {send_sms: 1, send_lms: 0, send_mms: 0, send_bulk: 0, send_file: 0, sqs_perf_test:0}
    tasks = {send_SS: 1}

    def on_start(self):
        global Curent_Env
        if 'dev' in self.client.base_url:
            Curent_Env = random.sample(Envs["dev"], 1)[0]
        elif 'stg' in self.client.base_url:
            Curent_Env = random.sample(Envs["stg"], 1)[0]

        # Curent_Env['groupId'] = Curent_Env['groupId'] + ("_%s%s" % (date.today().strftime("%y%m%d"), pydatetime.datetime.now().strftime("%H%M")))
        Curent_Env['groupId'] = Curent_Env['groupId'] + ("_%s" % (date.today().strftime("%y%m%d")))
        # get_access_token(self)

    def on_stop(self):
        pass #logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000
    #[2020-03-20 11:55:13,384] locust-1584705092-master-65c7764b5-67w59/ERROR/stderr: No module named 'between'
    # wait_time = between(5, 15)

def printf(str):
    if DEBUG:
        print(str)

if __name__ == '__main__':
    for i in range(0, 10):
        c = get_rand_contact_num()
        printf(c)

    while len(sys.argv) > 1:
        sys.argv.pop(1)
        pass
    printf(socket.gethostname())
    printf(getClientMsgId())
    printf(time())
    printf(pydatetime.datetime.now())
    Curent_Env = random.sample(Envs["dev"], 1)[0]
    printf(Curent_Env['agency_id'])