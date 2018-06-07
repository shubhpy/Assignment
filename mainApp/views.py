from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django import forms
from django.contrib import messages
from django.core.exceptions import PermissionDenied,ObjectDoesNotExist
from django.core import serializers
from django.db import transaction

from datetime import datetime
import json
import uuid
from bcrypt import hashpw, gensalt
import jwt
import pymongo

from functools import update_wrapper
from functools import wraps

from mainApp.mainbrain import mainMethod

mongo_ip = "localhost"
mongo_port = 27017

databaseName = "sample_database"
bcypt_rounds = 13
jwt_secret = "sample_secret"

# uri = "mongodb://" + mongo_user + ":" + mongo_pass + "@" + mongo_ip + ":" + str(mongo_port)+"/" + databaseName
uri = "mongodb://" + mongo_ip + ":" + str(mongo_port)+"/" + databaseName

client = pymongo.MongoClient(uri)
# connection = Connection()

db = client[databaseName]
users = db['users']

def auth(func):
    @wraps(func) # to preserve name, docstring, etc.
    def decorated(request, *args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            token_json = jwt.decode(token, jwt_secret, algorithms=['HS256'])
            username = token_json['username']            
        except Exception as e:
            print (e.__str__())
            return JsonResponse({"success": False,"message": "Invalid Token","header":False})
        return func(request, *args, **kwargs)
    return decorated

#views here.
def landing(request):
    if request.method == 'GET':
        return JsonResponse({"success":True,"error":False,"status":"Working"})

@auth
def getAddress(request):
    #Authenticated user
    if request.method == 'POST':
        url = request.POST['url']
        try:
            response = mainMethod(url)
            return JsonResponse({"success":True,"error":False,"address_list":response["address_list"],"message":response["message"]})
        except Exception as e:
            return JsonResponse({"success":False,"error":True,"address_list":list(),"message":e.__str__()})

def register(request):
    if request.method=='POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except Exception as e:
            print (e.__str__())
            return JsonResponse({"success":False,"error":True,"message":e.__str__()})

        try:
            user = users.find_one({"username":username})
            if user:
                return JsonResponse({"success":False,"error":False,"message":"Username is taken"})
        except Exception as e:
            print (e.__str__())
            return JsonResponse({"success":False,"error":True,"message":e.__str__()})            
        
        try:
            password = hashpw(password.encode(), gensalt(rounds=bcypt_rounds))
            user_id = uuid.uuid4().hex

            newuser = {
                "username":username,
                "password":password,
                "user_id": user_id
            }

            print (newuser)
            users.save(newuser)

            return JsonResponse({"success":True,"error":False,"message":"User registered","user_id":user_id})
        except Exception as e:
            print (e.__str__())
            return JsonResponse({"success":False,"error":True,"message":e.__str__()})            
    else:
        return JsonResponse({"success":False,"error":False,"message":"Method is POST"})

def authenticate_user(username,password):
    user = users.find_one({"username":username})
    if user:
        return (hashpw(password.encode(), user["password"]) == user["password"])
    return False

"""Func for Login"""
def userLogin(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except Exception as e:
            print (e.__str__())
            return JsonResponse({"success":False,"error":True,"message":e.__str__()})

        try:
            is_valid_user = authenticate_user(username,password)
            print (is_valid_user)
            if is_valid_user:
                print (username + " Authentication done")
                token_json = {
                    'username': username,
                    "random":uuid.uuid4().hex
                    }

                token =  jwt.encode(token_json, jwt_secret, algorithm='HS256')
                return JsonResponse({"success":True,"error":False,"message":username + " is logged in","token":str(token.decode('utf-8'))})                                
            else:
                return JsonResponse({"success":False,"error":False,"message":"Incorrect username or password"})
        except Exception as e:
            print (e.__str__())
            return JsonResponse({"success":False,"error":True,"message":e.__str__()})

    else:
        return JsonResponse({"success":False,"error":False,"message":"Method is POST"})