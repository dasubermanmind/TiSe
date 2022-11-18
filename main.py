

"""
    What this repository is about & what it is not.
    
    
    This is an intro repository for Time Series Analysis. 
    Answer: It is a specific way (subjective) way of analyzing a Sequence of 
    data points at consistent intervals over a set period of time. What 
    is slightly different about time series analysis is that it really shows
    changes over time. 
    
    Datasets: What I plan on using within this repo for data sets will be 
    kaggle datasets and any other **interesting** datasets that I find in the internet
    
    What this repository is not: 
    A production ready Time series library. It will over time morph itself into 
    just that, but right now I am using it a playground to see everything that is within
    this space. 
    
"""


import yfinance as finance
import matplotlib.pyplot as plt
import datetime
import pandas as pd


def download_data_set(stock, start, end):
    data = {}
    ticker = finance.download(stock, start,end)
    
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)


def construct_signal(data, short_period, long_period):
    # FInd the SMA for a short time period
    data['Short SMA'] = data['Price'].rolling(window=short_period).mean()
    # Finf the SMA for a longer timer period
    data['Long SMA'] = data['Price'].rolling(window=long_period).mean()
    data = data.dropna()
    print(data)





"""
    Notes: SMA: Unweighted mean of stock price at S(t) where t is time
    Sma k = 1/k sum i = n-k+1 to n S(i)
"""



def plot_data(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Price'], label='Stock Price', color='black')
    plt.plot(data['Short SMA'], label='Short SMA', color='yellow')
    plt.plot(data['Long SMA'], label='Long SMA', color='red')    
    plt.title('Moving Average Indicators')
    plt.show()
    
    
    

# Main starting point
if __name__ == '__main__':
    """
        This main functiuon is repsonsible for Figure 1
    """
    # start times 
    start_date = datetime.datetime(2020, 1,1)
    # end 
    end_date = datetime.datetime(2021, 1,1)
    
    stock_data = download_data_set('IBM', start_date, end_date)
    
    construct_signal(stock_data,30, 200)
    
    plot_data(stock_data)