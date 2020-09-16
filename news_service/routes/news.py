import json


import flask
from flask import Blueprint, jsonify
from news_service.newsactions.FetchNewsApi import FetchNewsApi
from news_service.database import PyMongo


def update_news_to_db():
    try:
        subcategory=flask.request.args.get('subcategory')
        category=flask.request.args.get('category')
        news_api_response=json.loads(FetchNewsApi.getNews(flask.request.args.get('subcategory')))
        print(news_api_response['message'])
        if news_api_response['message']=='success':
            print(news_api_response['news'])
            PyMongo.updateData('news','news',news_api_response['news'],'subcategory',subcategory,'category',category)
            return jsonify({"sucess":True,"message":"sucess"}),200
        else:
            return jsonify(news_api_response),400
    except Exception as e:
        return jsonify({"sucess": False}, {"message": "Error Occured " + str(e)}), 400




def fetchNews():
    try:
        news_api_response=json.loads(FetchNewsApi.getNews(flask.request.args.get('subcategory')))
        print(news_api_response)
        if news_api_response['message']=='sucess':
            return jsonify(news_api_response),200
        else:
            return jsonify(news_api_response),400
    except Exception as e:
        print(e)
        return jsonify({"sucess": False}, {"message": "Error Occured " + str(e)}), 400

def getnews():
    try:
        subcategory = flask.request.args.get('subcategory')
        data = PyMongo.getData('news','subcategory',subcategory)

        return jsonify({"sucess": True}, {"data": data}),200
    except Exception as e:
        return jsonify({"sucess": False}, {"message": "Error Occured " + str(e)}), 400
