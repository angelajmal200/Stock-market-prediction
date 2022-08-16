from contextlib import redirect_stderr
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

from gnewsclient import gnewsclient

import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from plotly import graph_objs as go
from plotly.offline import plot
import plotly.express as px
import kaleido
from matplotlib import pyplot as plt
import pandas as pd
import json

# Create your views here.
def home(request):



    name="Big Bull"
    content={'name':name}
    return render(request,"base\home1.html",content)

def chart(request):

    #stock data retriving

    marketinfo = yf.Ticker("SBIN.NS")
    longBusinessSummary=marketinfo.info['longBusinessSummary']
    website=marketinfo.info['website']
    logo_url=marketinfo.info['logo_url']
    currentPrice=marketinfo.info['currentPrice']
    longName=marketinfo.info['longName']
    previousClose=marketinfo.info['previousClose']
    changeinper=((currentPrice-previousClose)/previousClose)*100
    changeinper="{:.2f}".format(changeinper)

    #stock data in table format
    profitMargins=marketinfo.info['profitMargins']
    revenueGrowth=marketinfo.info['revenueGrowth']
    operatingMargins=marketinfo.info['operatingMargins']
    targetLowPrice=marketinfo.info['targetLowPrice']
    recommendationKey=marketinfo.info['recommendationKey']
    grossProfits=marketinfo.info['grossProfits']
    targetMedianPrice=marketinfo.info['targetMedianPrice']
    targetMeanPrice=marketinfo.info['targetMeanPrice']
    returnOnEquity=marketinfo.info['returnOnEquity']
    targetHighPrice=marketinfo.info['targetHighPrice']
    totalCash=marketinfo.info['totalCash']
    totalDebt=marketinfo.info['totalDebt']
    totalRevenue=marketinfo.info['totalRevenue']
    totalCashPerShare=marketinfo.info['totalCashPerShare']
    revenuePerShare=marketinfo.info['revenuePerShare']
    recommendationMean=marketinfo.info['recommendationMean']
    enterpriseToRevenue=marketinfo.info['enterpriseToRevenue']
    FWeekChange=marketinfo.info['52WeekChange']
    forwardEps=marketinfo.info['forwardEps']
    sharesOutstanding=marketinfo.info['sharesOutstanding']
    bookValue=marketinfo.info['bookValue']
    lastFiscalYearEnd=marketinfo.info['lastFiscalYearEnd']
    heldPercentInstitutions=marketinfo.info['heldPercentInstitutions']
    netIncomeToCommon=marketinfo.info['netIncomeToCommon']
    trailingEps=marketinfo.info['trailingEps']
    lastDividendValue=marketinfo.info['lastDividendValue']
    SandP52WeekChange=marketinfo.info['SandP52WeekChange']
    priceToBook=marketinfo.info['priceToBook']
    earningsQuarterlyGrowth=marketinfo.info['earningsQuarterlyGrowth']
    priceToSalesTrailing12Months=marketinfo.info['priceToSalesTrailing12Months']
    pegRatio=marketinfo.info['pegRatio']
    forwardPE=marketinfo.info['forwardPE']
    regularMarketOpen=marketinfo.info['regularMarketOpen']
    twoHundredDayAverage=marketinfo.info['twoHundredDayAverage']
    payoutRatio=marketinfo.info['payoutRatio']
    regularMarketDayHigh=marketinfo.info['regularMarketDayHigh']
    averageDailyVolume10Day=marketinfo.info['averageDailyVolume10Day']
    regularMarketPreviousClose=marketinfo.info['regularMarketPreviousClose']
    fiftyDayAverage=marketinfo.info['fiftyDayAverage']
    open=marketinfo.info['open']
    averageVolume10days=marketinfo.info['averageVolume10days']
    dividendRate=marketinfo.info['dividendRate']
    regularMarketDayLow=marketinfo.info['regularMarketDayLow']
    trailingPE=marketinfo.info['trailingPE']
    regularMarketVolume=marketinfo.info['regularMarketVolume']
    marketCap=marketinfo.info['marketCap']
    fiftyTwoWeekHigh=marketinfo.info['fiftyTwoWeekHigh']
    fiftyTwoWeekLow=marketinfo.info['fiftyTwoWeekLow']
    dayLow=marketinfo.info['dayLow']
    dayHigh=marketinfo.info['dayHigh']
    regularMarketPrice=marketinfo.info['regularMarketPrice']


    datas=[['profitMargins',profitMargins],
    ['revenueGrowth',revenueGrowth],
    ['operatingMargins',operatingMargins],
    ['targetLowPrice',targetLowPrice],
    ['recommendationKey',recommendationKey],
    ['grossProfits',grossProfits],
    ['targetMedianPrice',targetMedianPrice],
    ['targetMeanPrice',targetMeanPrice],
    ['returnOnEquity',returnOnEquity],
    ['targetHighPrice',targetHighPrice],
    ['totalCash',totalCash],
    ['totalDebt',totalDebt],
    ['totalRevenue',totalRevenue],
    ['totalCashPerShare',totalCashPerShare],
    ['revenuePerShare',revenuePerShare],
    ['recommendationMean',recommendationMean],
    ['enterpriseToRevenue',enterpriseToRevenue],
    ['52WeekChange',FWeekChange],
    ['forwardEps',forwardEps],
    ['sharesOutstanding',sharesOutstanding],
    ['bookValue',bookValue],
    ['lastFiscalYearEnd',lastFiscalYearEnd],
    ['heldPercentInstitutions',heldPercentInstitutions],
    ['netIncomeToCommon',netIncomeToCommon],
    ['trailingEps',trailingEps],
    ['lastDividendValue',lastDividendValue],
    ['SandP52WeekChange',SandP52WeekChange],
    ['priceToBook',priceToBook],
    ['earningsQuarterlyGrowth',earningsQuarterlyGrowth],
    ['priceToSalesTrailing12Months',priceToSalesTrailing12Months],
    ['pegRatio',pegRatio],
    ['forwardPE',forwardPE],
    ['regularMarketOpen',regularMarketOpen],
    ['twoHundredDayAverage',twoHundredDayAverage],
    ['payoutRatio',payoutRatio],
    ['regularMarketDayHigh',regularMarketDayHigh],
    ['averageDailyVolume10Day',averageDailyVolume10Day],
    ['regularMarketPreviousClose',regularMarketPreviousClose],
    ['fiftyDayAverage',fiftyDayAverage],
    ['open',open],
    ['averageVolume10days',averageVolume10days],
    ['dividendRate',dividendRate],
    ['regularMarketDayLow',regularMarketDayLow],
    ['trailingPE',trailingPE],
    ['regularMarketVolume',regularMarketVolume],
    ['marketCap',marketCap],
    ['fiftyTwoWeekHigh',fiftyTwoWeekHigh],
    ['fiftyTwoWeekLow',fiftyTwoWeekLow],
    ['dayLow',dayLow],
    ['dayHigh',dayHigh],
    ['regularMarketPrice',regularMarketPrice],]

    market = pd.DataFrame(datas, columns=['Name', 'Value'])
    market.to_csv('static/files/file2.csv')
    market = pd.read_csv("static/files/file2.csv")

    # parsing the DataFrame in json format.
    json_records = market.reset_index().to_json(orient ='records')
    market = []
    market= json.loads(json_records)


  


    START="2015-01-01"
    TODAY=date.today().strftime("%Y-%m-%d")

    stocks="SBIN.NS"
    selected_stocks=stocks

    period=4*365

    def load_data(ticker):
        data=yf.download(ticker,START,TODAY)
        data.reset_index(inplace=True)
        return data

    data=load_data(selected_stocks)

    #fig=px.line(x=data['Date'],y=data['Open'])
    #fig.add_trace(go.Scatter(x=data['Date'],y=data['Close']))
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name='stock_open'))
    fig.layout.update(title_text="time series data",xaxis_rangeslider_visible=True)
    #fig.show()
    chart=fig.to_html()
    fig.write_image("static/images/fig2.png")
    print("imaged added")
    


    #forcasting

    df_train=data[['Date','Close']]
    df_train=df_train.rename(columns={"Date":"ds","Close":"y"})
    m=Prophet()
    m.fit(df_train)
    future=m.make_future_dataframe(periods=period)
    forecast=m.predict(future)

    fig1=plot_plotly(m,forecast)
    fig1.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name='stock_open'))
    #fig1.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name='stock_open'))
    #fig1.show()
    chart1=fig1.to_html()
    fig1.write_image("static/images/fig1.png")
    print("imaged added")
    

    fig2=m.plot_components(forecast)
    fig2.show()
    print("imaged added")
    plt.savefig('static/images/fig3.png')

    ds=forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(1)
    ds=ds.reset_index(drop=True)
    lvalue=ds['yhat']

    print("d value")
    print(lvalue)

    value=data['Open'].tail(1)
    print("original value")
    print(value)

    percentage=((int(lvalue)-int(value))/int(lvalue))*100
    percentage="{:.2f}".format(percentage)

    context={'chart':chart,'chart1':chart1,'percentage1':percentage,
    'd': market,
    'longBusinessSummary':longBusinessSummary,
    'website':website,
    'logo_url':logo_url,
    'currentPrice':currentPrice,
    'longName':longName,
    'previousClose':previousClose,
    'changeinper':changeinper
    }

    return render(request,'base/chart.html',context)
    
def dashboard(request):
    
    START="2015-01-01"
    TODAY=date.today().strftime("%Y-%m-%d")

    stocks="SBIN.NS"
    selected_stocks=stocks

    period=4*365

    def load_data(ticker):
        data=yf.download(ticker,START,TODAY)
        data.reset_index(inplace=True)
        return data

    data=load_data(selected_stocks)
    print(data)

    def plot_raw_data():
        fig=go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name='stock_open'))
        fig.layout.update(title_text="time series data",xaxis_rangeslider_visible=True)
        return fig.show()
        
    fig=plot_raw_data()


    #forcasting

    df_train=data[['Date','Close']]
    df_train=df_train.rename(columns={"Date":"ds","Close":"y"})
    m=Prophet()
    m.fit(df_train)
    future=m.make_future_dataframe(periods=period)
    forecast=m.predict(future)
    forecast.tail()

    fig1=plot_plotly(m,forecast)
    fig1.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name='stock_open'))
    fig1.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name='stock_open'))
    fig1.show()


    fig2=m.plot_components(forecast)
    fig2.show()
    chart1=fig.to_html()
    chart2=fig1.to_html()
    chart3=fig2.to_html()
    context={'chart1':chart1,'chart2':chart2,'chart3':chart3}
    return render(request,"base\dashboard.html",context)

def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=name).exists():
            messages.info(request,"username taken")
            return render(request,"base\index.html")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email alredy exist")
            return render(request,"base\index.html")
        else:
            user=User.objects.create_user(username=name,password=password,email=email)
            user.save()
            print("user created")
            messages.info(request,"Thank You For Registration ❤️")
            return render(request,"base\index.html")
    else:
        return render(request,"base\index.html")

def login(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        print(name)
        print(password)
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            print("login sucess")
            return redirect('dashboard')
        else:
            messages.info(request,"credentials invalid")
            print("credentials invalid")
            return render(request,"base\index.html")
    else:
        return render(request,"base\index.html")


def logout(request):
    auth.logout(request)
    return render(request,'base\home1.html')

def header(request):
    return render(request,'header.html')

def snews(request):
    client = client = gnewsclient.NewsClient(language='english', location='india', topic='Buisness', use_opengraph=True, max_results=25)
    news_list = client.get_news()
    content={'news_list':news_list}
    return render(request,"base\snews.html",content)