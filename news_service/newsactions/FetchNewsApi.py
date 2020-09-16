from news_service.config import CONF
import json
import requests



class FetchNewsApi:

    @classmethod
    def getNews(cls,query):
        try:
            print(CONF.FETCH_NEWS_URI)
            resp = requests.get(CONF.FETCH_NEWS_URI.replace('query',query))

            if resp.status_code != 200:
                return json.dumps({"success":False,"message":"Failed"})
            else:
                return json.dumps({"success": True, "message": "success", "news": resp.json()})
                # return json.dumps({"success": True, "message": "success", "news": "hey"})


        except Exception as e:
            return json.dumps({"success":False,"message":"Exception "+str(e)})

