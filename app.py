from flask import Flask






from news_service.routes import categories
from news_service.routes import news



application=Flask(__name__)

@application.route("/news/getcategories",methods=['GET'])
def req_getcategories():
    return categories.getcategories()

@application.route("/news/insertcategories",methods=['POST'])
def req_insertcategories():
    return categories.insertcategories()

@application.route("/news/getnews",methods=['GET'])
def req_getnews():
    return news.getnews()

@application.route("/news/fetchnews",methods=['GET'])
def req_fetchnews():
    return news.fetchNews()

@application.route("/news/updatenews",methods=['GET'])
def req_updatenews():
    return news.update_news_to_db()

@application.before_request
def before_req_check():
    print("You will be validated")


if __name__ == '__main__':
    application.run(host='127.0.0.1',port=8080,debug=True)

