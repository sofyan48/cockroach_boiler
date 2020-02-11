from flask_restful import Resource, reqparse, fields
from app.helpers.rest import *
from app.helpers.memcache import *
import datetime
from app.models import model as db


class UserdataResource(Resource):
    def get(self):
        obj_userdata = list()
        results = db.get_all("userdata")
        data = {
            "userdata_id": "001",
            "email" : "meongbego@gmail.com"
        }
        obj_userdata.append(data)
        return response(200, data=obj_userdata)


class UserdataResourceById(Resource):
    def get(self, userdata_id):
        obj_userdata = []
        data = {
            "userdata_id": "001",
            "email" : "meongbego@gmail.com"
        }
        obj_userdata.append(data)
        return response(200, data=obj_userdata)


class UserdataInsert(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('location', type=str, required=True)
        parser.add_argument('city', type=str, required=True)
        parser.add_argument('province', type=str, required=True)
        args = parser.parse_args()

        data_insert = {
            "email" : args['email'],
            "first_name" : args['first_name'],
            "last_name" : args['last_name'],
            "location" : args['location'],
            "city" : args['city'],
            "province" : args['province']
        }
        try:
            print(data_insert)
        except Exception as e:
            message = {
                "status": False,
                "error": str(e)
            }
        else:
            message = {
                "status": True,
                "data": data_insert
            }
        finally:
            return response(200, message=message)