import datetime
import datetime
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from timeoftone.models import DateHistory
from django.db import models
import dateparser


def index(request):
    check_for_updates()

    #context = DateHistory.objects.filter(asOfDate= datetime.date(2006,10,6)).first()
    context = DateHistory.objects.order_by('-asOfDate').first()

    return render(request, "index.html", {"data" : context})






def check_for_updates():
    # run scrapy to discover change
    res = requests.get("https://www.analogman.com/kotdelay.htm")
    soup = BeautifulSoup(res.text, 'html.parser')

    temp = soup.find("b")
    shippingDate = temp.contents.pop()
    tempshipdate = dateparser.parse(shippingDate)

    dateCheck = date(tempshipdate.year)


    temp = soup.findAll("p")
    tempContents = temp[00].contents[1]

    dateAttempt = tempContents.split()

    # check if it's a real update
    DateHistory.objects.filter(asOfDate=datetime.date(2006, 10, 6)).first()
