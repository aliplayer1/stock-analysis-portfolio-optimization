import numpy as np
from sklearn.cluster import KMeans
from modules.data_preprocessing import preprocess_stock_data

def apply_kmeans(df, num_clusters):
    """
    Apply K-Means clustering to the stock data, handling infinities and NaNs.
    """
    # Ensure 'Daily Return' is calculated
    if 'Daily Return' not in df.columns:
        df['Daily Return'] = df['Close'].pct_change()
    
    # Replace inf values with NaN and drop them
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(subset=['Daily Return'], inplace=True)
    
    # Ensure we have enough data points
    if df.shape[0] < num_clusters:
        raise ValueError(f"Not enough data points to perform clustering with {num_clusters} clusters.")
    
    # Apply KMeans clustering with a fixed random state
    model = KMeans(n_clusters=num_clusters, random_state=42)
    df['Cluster'] = model.fit_predict(df[['Daily Return']])
    
    return df, model
