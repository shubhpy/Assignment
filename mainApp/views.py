from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django import forms
from django.contrib import messages
from django.core.exceptions import PermissionDenied,ObjectDoesNotExist
from django.core import serializers
from django.db import transaction

# from mainApp.models import Employee,Action
# from mainApp.forms import EmployeeNewForm

from datetime import datetime
import json
import uuid
import pymongo

client = pymongo.MongoClient()
databaseName = "sample_database"
# connection = Connection()

db = client[databaseName]
employees = db['employees']

#Create your views here.
def landing(request):
    if request.method == 'GET':
        return JsonResponse({"success":True,"error":False,"status":"Working"})

@login_required
def getAddress(request):
    #Authenticate user
    if request.method == 'POST':
        url = request.POST['url']
        print (url)
        return {"success":True,"error":False,"data":[]}

def register(request):
    if request.method=='POST':
        # form = EmployeeNewForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            newuser = {
                "username":username,
                "password":password,
                "user_id":uuid.uuid4().hex
            }

            print (newuser)
            employees.save(newuser)

            JsonResponse({"saved":True})
            # employee=Employee.objects.filter().get(username=username)
            # messages.success(request,'username already exits, choose a new one')
            # return redirect(reverse('edit_employee',args=(employee.pk,)))
        except Exception as e:
            print (e.__str__())
            # if form.is_valid():
            #     new_employee = form.save()
            #     note="Adding new Employee"
            #     action=Action(note=note)
            #     action.save()
            #     messages.success(request,'New Employee is going to be added')
            #     # return redirect(reverse('action',args=(action.pk,)))
            # else:
            #     messages.error(request,'Please correct,Incorrect fields')
            #     context['form']=form
        # return redirect(request,'leave/new_employee.html',context)
    else:
        # context['form']=EmployeeNewForm()
        return JsonResponse({"error":"method is POST"})

"""Func for Logout"""
def logout(request):
    logout(request)
    return redirect('login')

"""Func for Login"""
def login(request):
    login(request)
    return redirect('login')