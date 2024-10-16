import pandas as pd
import numpy as np

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

from modules.inferential_statistics import InferentialStatistics

class StatisticsCalculatorWithInferentialStatistics:
    def __init__(self, returns_data):
        self.returns_data = returns_data
        self.inferential_stats = InferentialStatistics(self.returns_data)
    
    def calculate_basic_statistics(self):
        # Assuming existing statistics calculation
        mean_return = np.mean(self.returns_data)
        std_dev = np.std(self.returns_data)
        
        return {
            'mean': mean_return,
            'std_dev': std_dev
        }
    
    def calculate_inferential_statistics(self):
        # Perform inferential statistics
        ci = self.inferential_stats.confidence_interval()
        t_stat, p_val = self.inferential_stats.t_test_mean()
        return {
            'confidence_interval': ci,
            't_test': {'t_stat': t_stat, 'p_value': p_val}
        }
    
    def generate_statistics_report(self):
        basic_stats = self.calculate_basic_statistics()
        inferential_stats = self.calculate_inferential_statistics()
        
        # Combine basic and inferential statistics
        report = {**basic_stats, **inferential_stats}
        return report
