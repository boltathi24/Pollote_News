import flask
from flask import  jsonify
from news_service.database import PyMongo





def getcategories():
    try:

        js=PyMongo.getAllData('category')[0]
        # js="ello"
        # for jsnew in js['categoriesList']:
        #     subcategory=jsnew['subcategory']
        #     category=jsnew['category']
        #     for subcat in subcategory:
        #         print("Category:"+category ,"Subcategory:"+subcat)
        return jsonify({"sucess": True}, {"data": js['categoriesList']})
        # return jsonify({"sucess": True}, {"data": js})

    except Exception as e:
        return jsonify({"sucess":False},{"message":"Error Occured "+str(e)}), 400



def insertcategories():
    try:
        PyMongo.insertData('category', flask.request.json)
        return jsonify({"sucess": True}, {"message": "successfully Inserted"}),200
    except Exception as e:
        return jsonify({"sucess":False},{"message":"Error Occured "+str(e)}), 400

