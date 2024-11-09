import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def preprocess_network_data(df):
    """
    Preprocess network traffic data to transform it into standardized features

    Parameters:
    df (pandas.DataFrame): Raw network traffic data

    Returns:
    pandas.DataFrame: Preprocessed data with new features
    """
    # Create new DataFrame for processed features
    processed_df = pd.DataFrame()

    # Calculate speed from source IP (using pktcount and dur)
    processed_df['speed_src_ip'] = df['pktcount'] / df['dur']

    # Standardize number of packets
    scaler = StandardScaler()
    processed_df['std_n_packets'] = scaler.fit_transform(df[['pktcount']])

    # Standardize bytes
    processed_df['std_bytes'] = scaler.fit_transform(df[['bytecount']])

    # Calculate bytes per flow
    processed_df['bytes_per_flow'] = df['bytecount'] / df['flows']

    # Calculate normalized internal flows
    processed_df['n_int_flows'] = df['flows'] / df['pktcount']

    # Copy the label column
    processed_df['class'] = df['label']

    return processed_df

# Example usage:
raw_data = pd.read_csv('app/training/classifier/dataset_sdn.csv')
processed_data = preprocess_network_data(raw_data)
# Lưu dữ liệu đã xử lý vào tệp CSV
processed_data.to_csv('processed_network_data.csv', index=False)