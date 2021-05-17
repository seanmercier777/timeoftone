import datetime
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from timeoftone.models import DateHistory
import dateparser
from django.views.generic import ListView

def index(request):
    #check_for_updates()

    #context = DateHistory.objects.filter(asOfDate= datetime.date(2006,10,6)).first()
    context = DateHistory.objects.order_by('-asOfDate').first()

    table_data = []
    table_labels = []
    for dates in DateHistory.objects.order_by('shippingDate'):
        table_labels.append(str(dates.shippingDate))
        table_data.append(dates.waitInDays)

    return render(request, "index.html", {"data" : context, "query_results": DateHistory.objects.order_by('-asOfDate')[:15], "list_query": list(DateHistory.objects.all()), "table_data": table_data, "table_labels" : table_labels })

def check_for_updates():
    monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    res = requests.get("https://www.analogman.com/kotdelay.htm")
    soup = BeautifulSoup(res.text, 'html.parser')

    #Get Shipping Date Information
    temp = soup.find("b")
    rawShippingDate = temp.contents.pop()
    tempshipdate = dateparser.parse(rawShippingDate)
    ###

    temp = soup.findAll("p")
    tempContents = temp[00].contents[1]
    dateAttempt = tempContents.split()

    for i in range(0, len(dateAttempt)):
        if dateAttempt[i] in monthList:
            date2 = dateAttempt[i] + " " + dateAttempt[i+1] + dateAttempt[i+2]
            break
    tempGetDate = dateparser.parse(date2)

    shippingDate = datetime.date(tempshipdate.year, tempshipdate.month, tempshipdate.day)
    asOfDate = datetime.date(tempGetDate.year, tempGetDate.month, tempGetDate.day)

    # check if new update
    returnedDateHistory = DateHistory.objects.filter(asOfDate=asOfDate).first()

    if returnedDateHistory == None:
        newDateHistory = DateHistory.create_history(asOfDate, shippingDate)
        newDateHistory.save()
    else:
        return

def generate_tables():
    return

class DateHistoryListView(ListView):
    model = DateHistory
    template_name = 'date_history.html'

def line_graph(request):
    labels = []
    data = []

    queryset = DateHistory.objects.order_by('-asOfDate')[:10]
    for history in queryset:
        labels.append(history.asOfDate)
        data.append(history.waitingInDays)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })