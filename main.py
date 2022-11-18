

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
    plt.plot(stock_data)
    plt.show()
    
    download_data_set()