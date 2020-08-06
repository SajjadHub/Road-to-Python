import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from yahooquery import Ticker
from datetime import date, timedelta
import numpy as np


def printActiveInvestmentsRelative(tickers, start):
    # Downloads pandas Dataframe for active tickers from yahoo finance
    activeInvestments = yf.download(tickers, start=start, interval="1h")
    pd.set_option('display.max_rows', activeInvestments.shape[0]+1)
    # print(activeInvestments)

    # Rescalse the close prices of active investments and plots them
    (activeInvestments.Close / activeInvestments.Close.iloc[0] * 100).plot(figsize=(20, 10))
    plt.xlabel("Date")
    plt.ylabel("Adjusted")
    plt.title("Investments")
    plt.show()


def investmentValueChange(tickers):
    """
    Take in tickers and return +/- over the time period
    """
    for tick in tickers:
        print("1 month information for ticker " + tick, end="\n")
        tempInvest = Ticker(tick, country="Canada")
        # print(tempInvest.summary_detail, end="\n")
        print(tempInvest.recommendation_trend, end="\n")
        input("Ready?")


def getSMA(tickers):
    """
    Calculates and graphs the SMA30 and SMA100 of a list of stocks
    """
    # Get historical data
    daysBefore = (date.today() - timedelta(days=365)).isoformat()

    # For each ticker get the information and calculate the SMA's and graph the
    for tick in tickers:
        stock = yf.download(tick, start=daysBefore)['Adj Close'].to_frame()
        SMA30 = stock.rolling(window=30).mean()
        SMA100 = stock.rolling(window=100).mean()

        # Show the averages
        plt.plot(stock, label=tick)
        plt.plot(SMA30, label="SMA30")
        plt.plot(SMA100, label="SMA100")
        plt.title('Stock SMA30 SMA100')
        plt.xlabel('Date')
        plt.ylabel('Adj close/SMA')
        plt.legend(loc='upper left')
        plt.show()
        # pd.set_option('display.max_rows', stock.shape[0]+1)


def buySell(temp):
    """
    Find intersections for MACD
    With intersections either set a buy or sell indicator
    depending on which direction the cross occured
    """
    buy = []
    sell = []
    flag = -1

    for i in range(0, len(temp)):
        if temp['MACD'][i] > temp['signal'][i]:
            sell.append(np.nan)
            if flag != 1:
                buy.append(temp['Close'][i])
                flag = 1
            else:
                buy.append(np.nan)
        elif temp['MACD'][i] < temp['signal'][i]:
            buy.append(np.nan)
            if flag != 0:
                sell.append(temp['Close'][i])
                flag = 0
            else:
                sell.append(np.nan)
        else:
            sell.append(np.nan)
            buy.append(np.nan)
    return buy, sell


def getMACD(tickers):
    """
    Get moving average convergence/divergence
    """
    daysBefore = (date.today() - timedelta(days=100)).isoformat()

    for tick in tickers:
        fullStock = yf.download(tick, start=daysBefore)
        stock = fullStock['Close'].to_frame()

        # Calculate variables
        shortEMA = stock.ewm(span=12, adjust=False).mean()
        longEMA = stock.ewm(span=26, adjust=False).mean()
        MACD = shortEMA - longEMA
        signal = MACD.ewm(span=9, adjust=False).mean()

        # Get intersections and buy/sell indicators
        temp = fullStock
        temp['MACD'] = MACD
        temp['signal'] = signal
        buy, sell = buySell(temp)
        temp["Buy"] = buy
        temp["Sell"] = sell
        plt.scatter(stock.index, temp["Buy"], color='green',
                    label='Buy', marker='^')
        plt.scatter(stock.index, temp["Sell"], color='red',
                    label='Sell', marker='v')

        # Show the averages
        # plt.plot(shortEMA, label="shortEMA")
        # plt.plot(longEMA, label="longEMA")
        # plt.plot(MACD, label="MACD")
        # plt.plot(signal, label="signal")
        plt.plot(stock, label=tick)
        plt.title('Stock')
        plt.xlabel('Date')
        plt.ylabel('Adj close/EMA')
        plt.legend(loc='upper left')
        plt.show()


# Get current date and calculate date 60 days ago
currentDate = date.today().isoformat()
daysBefore = (date.today() - timedelta(days=60)).isoformat()


# My active tickers
# TODO: Add questrade intigration to get my actual tickers
activeTickers = ["ZAG.TO", "BEP-UN.TO", "VFV.TO"]

getSMA(activeTickers)
# getMACD(activeTickers)

# investmentValueChange(activeTickers)
