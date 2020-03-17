from locust import HttpLocust, TaskSet
from uuid import uuid4
import json
import requests
from datetime import datetime
import random

bearer_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJTS1QiLCJhZ2VuY3lJZCI6InNrdGFnZW5jeSIsInNjb3BlcyI6IlJPTEVTX0FHRU5DWSIsImV4cCI6MTU5OTY0ODM0Mn0.Hpktkgug-sqOE0kv37sHKP39O4ZzCmidnkZpRav-xD4'
def get_access_token(l):
    payload = "{\n  \"clientId\": \"%s\",\n  \"clientSecret\": \"%s\",\n  \"grantType\": \"clientCredentials\"\n}" % ("sktagency", "2c112d50d61e47505ea1016e8d2f47e7d12de08746cb4b5b4fc00d9c0469428e")
    resp = l.client.post("/ag/1.1/token", headers={'Content-Type': "application/json"}, data=payload)
    print(resp.json())
    bearer_token = resp.json()['data']['tokenInfo']['accessToken']

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

def get_header():
    return {
        "Authorization": "Bearer " + bearer_token,
        "Content-Type": "application/json"
    }

def send_sms(l):
    resp = l.client.post('/ag/1.1/message',
    headers=get_header(),
    data=json.dumps({
      'clientMsgId': uuid4().hex,
      'chatbotId': '18994029',
      'userContact': '+23000011',
      'expiryOption': 1,
      'groupId': 'groupid!!!!!!!!!!!',
      'header': 0,
      'footer': '010-6444-0681',
      'messagebaseId': 'mb_test_sms',
      'productCode': 'sms',
      'agencyId': 'skt_reseller_test',
      'body': {
          'description': '[oms1226] 안녕하세요? 스트레스 테스트입니다 ' + uuid4().hex
      },
    }))
    print(resp.json())

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

class UserBehavior(TaskSet):
    tasks = {send_sms: 1, send_lms: 0, send_mms: 0, send_bulk: 0, send_file: 0, sqs_perf_test:0}

    def on_start(self):
        get_access_token(self)

    def on_stop(self):
        pass #logout(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000

if __name__ == '__main__':
    for i in range(0, 10):
        c = get_rand_contact_num()
        print(c)
