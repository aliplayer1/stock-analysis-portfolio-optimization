import pandas as pd

def calculate_descriptive_statistics(stock_data):
    """
    Calculate basic descriptive statistics (mean, median, standard deviation, etc.) for stock price data.
    """
    stats = {}
    stats['mean'] = stock_data['Close'].mean()
    stats['median'] = stock_data['Close'].median()
    stats['std_dev'] = stock_data['Close'].std()
    stats['variance'] = stock_data['Close'].var()
    stats['min'] = stock_data['Close'].min()
    stats['max'] = stock_data['Close'].max()

    return stats

def calculate_rolling_statistics(stock_data, window=20):
    """
    Calculate rolling mean and rolling standard deviation over a given window size (default 20 days).
    """
    rolling_stats = pd.DataFrame()
    rolling_stats['Rolling Mean'] = stock_data['Close'].rolling(window=window).mean()
    rolling_stats['Rolling Std Dev'] = stock_data['Close'].rolling(window=window).std()

    return rolling_stats
