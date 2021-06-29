from django.shortcuts import render
from django.http import HttpResponse

import datetime

from validate.models import Request
# Create your views here.


def home(request):
    return render(request, 'home.html', {"name": 'Krishna'})


def uinput(request):
    firstname = request.GET['fname']
    middlename = request.GET['mname']
    lastname = request.GET['lname']
    dob = request.GET['dob']
    gender = request.GET['gender']
    nationality = request.GET['nation']
    city = request.GET['city']
    state = request.GET['state']
    pincode = request.GET['pincode']
    qualification = request.GET['qualification']
    salary = int(request.GET['salary'])
    pan = request.GET['pan']

    try:

        try:
            reqid = 1
            if len(firstname) == 0 or len(firstname) < 3:
                raise Exception

        except:
            raise Exception

        try:
            if len(lastname) == 0 or len(lastname) < 3:
                raise Exception

        except:
            raise Exception

        try:
            if len(lastname) == 0 or len(lastname) < 3:
                raise Exception

        except:
            raise Exception

        try:
            datetime.datetime.strptime(dob, '%Y-%m-%d')

        except ValueError:
            raise Exception

        try:
            if gender not in 'male' == True or gender not in 'female' == True:
                raise Exception
        except:
            raise Exception

        try:
            if nationality not in 'indian' == True or nationality not in 'american' == True:
                raise Exception
        except:
            raise Exception

        try:
            if len(city) == 0 or len(city) < 2:
                raise Exception
        except:
            raise Exception

        try:
            if len(state) == 0 or len(state) < 3:
                raise Exception
        except:
            raise Exception

        try:
            if len(pincode) < 5 or len(pincode) > 7:
                raise Exception
        except:
            raise Exception

        try:
            if len(qualification) < 2:
                raise Exception
        except:
            raise Exception

        try:
            if salary < 1000:
                raise Exception
        except:
            raise Exception

        try:
            if len(pan) < 10:
                raise Exception
        except:
            raise Exception
        b = Request(reqid=reqid, firstname=firstname, lastname=lastname, dob=dob, gender=gender, nationality=nationality,
                    state=state, city=city, pincode=pincode, qualification=qualification, salary=salary, pannumber=pan)
        b.save()
        reqid = reqid + 1
        return render(request, 'result.html', {'operation': 'success'})

    except:
        return render(request, 'result.html', {'operation': 'reject'})
