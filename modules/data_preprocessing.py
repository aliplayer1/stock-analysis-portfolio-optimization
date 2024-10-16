import pandas as pd
from modules.inferential_statistics import InferentialStatistics

def handle_missing_data(df):
    """
    Fill or drop missing data in the stock DataFrame.
    """
    df.ffill(inplace=True)
    df.dropna(inplace=True)
    return df

def normalize_data(df, columns):
    """
    Normalize specific columns in the DataFrame using min-max scaling.
    """
    df[columns] = (df[columns] - df[columns].min()) / (df[columns].max() - df[columns].min())
    return df

def preprocess_stock_data(df):
    """
    Apply a series of preprocessing steps to stock data.
    """
    df = handle_missing_data(df)
    df = normalize_data(df, ['Close', 'Volume'])  # Example columns
    return df

def create_price_movement_labels(df):
    """
    Create a binary label where 1 indicates the price increased, and 0 indicates it decreased or stayed the same.
    """
    df['Price Movement'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    df.dropna(inplace=True)  # Drop rows with NaN values resulting from shift
    return df

class DataPreprocessorWithInferentialStatistics:
    def __init__(self, stock_data):
        self.stock_data = stock_data
        self.inferential_stats = None

    def preprocess_data(self):
        # Assuming existing preprocessing code
        preprocessed_data = self.stock_data  # Placeholder for actual preprocessing
        return preprocessed_data
    
    def add_inferential_statistics(self):
        returns_data = self.preprocess_data()
        self.inferential_stats = InferentialStatistics(returns_data)
        
        # Example of using inferential statistics
        ci = self.inferential_stats.confidence_interval()
        t_stat, p_val = self.inferential_stats.t_test_mean()
        
        return {
            'confidence_interval': ci,
            't_test': {'t_stat': t_stat, 'p_value': p_val}
        }
