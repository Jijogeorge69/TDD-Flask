from flask import render_template
from flask import request
from bson.json_util import dumps,RELAXED_JSON_OPTIONS
from bson.objectid import ObjectId
import json
from project import mongo

from . import profile_blueprint

################
#### routes ####
################

@profile_blueprint.route('/helloProfile/too', methods=['POST'])
def helloProfile():
    profiledata = request.get_json()
    print(profiledata)
    return profiledata

@profile_blueprint.route('/createProfile', methods=['POST'])
def createProfile():
    profile_data = request.get_json()

    # if user:
    mongo.db.profiles.insert_one(profile_data)
    bs = dumps(profile_data,json_options=RELAXED_JSON_OPTIONS)
    return bs


@profile_blueprint.route('/getProfile', methods=['GET'])
def getProfile():
    print("111111>>>>>>>><<<<<<<<11111111")
    response = mongo.db.profiles.find_one({"_id" : ObjectId("5f833fdcccb862defff89522")})
    print("hello  ",response)
    return response
