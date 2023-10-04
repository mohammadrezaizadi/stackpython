from django.shortcuts import render
import json
import os
from . import tradeHelper as th
from datetime import timedelta , datetime , date
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.






def index(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    t = th.Getsymbols("EURUSD_i")

    today = datetime.combine(date.today(), datetime.min.time())
    th.login()
    st = today + timedelta(days=-5)
    c = th.GetCandels(t[0].name, st, today, 'h1')
    th.shotdown()
    b = "["
    for i in c:
        b+= "{" +'"date":"' + str(pd.to_datetime(str(i['time']),unit='s')) + '", "open":' + str(i['open']) + ', "close":'+  str(i['close']) +', "high":'+str(i['high'])+', "low":' + str(i['low']) +"},"
    b = b[:-1]
    b+= "]"

    # data = open(dir_path + "/static/btc-usd-data.json").read()

    btc_usd_data = b
    return render(request, "index.html", {"btc_usd_data": btc_usd_data})



@api_view(['get'])
def MyTime(request,timeframe,symbolname):
    t = th.Getsymbols(symbolname)
    today = datetime.combine(date.today(), datetime.min.time())
    th.login()
    st = today + timedelta(days=-5)
    c = th.GetCandels(t[0].name, st, today, timeframe)
    th.shotdown()
    b = "["
    for i in c:
        b += "{" + '"date":"' + str(pd.to_datetime(str(i['time']), unit='s')) + '", "open":' + str(
            i['open']) + ', "close":' + str(i['close']) + ', "high":' + str(i['high']) + ', "low":' + str(
            i['low']) + "},"
    b = b[:-1]
    b += "]"
    return Response(b)


@api_view(['get'])
def GetSymbols(request):
    t = th.Getsymbols("")
    names = list(o.name for o in t if "USD" in o.name or "EUR" in o.name)
    print(names)

    return Response(names)