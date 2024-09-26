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
    
    # Drop rows where 'Daily Return' is NaN or infinite
    df.replace([np.inf, -np.inf], np.nan, inplace=True)  # Replace inf values with NaN
    df.dropna(subset=['Daily Return'], inplace=True)  # Drop rows with NaN in 'Daily Return'

    # Ensure we have enough data points
    if df.shape[0] < num_clusters:
        raise ValueError(f"Not enough data points to perform clustering with {num_clusters} clusters.")

    # Apply KMeans clustering
    model = KMeans(n_clusters=num_clusters)
    df['Cluster'] = model.fit_predict(df[['Daily Return']])
    
    return df, model
