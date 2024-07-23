import pandas as pd
import numpy as np
from twstock import Stock

def calculate_moving_averages(data, window_size):
    """Calculates Simple, Exponential, and Weighted Moving Averages.

    Args:
        data (pd.Series): Time-series data (e.g., stock prices).
        window_size (int): Number of periods for the moving average.

    Returns:
        pd.DataFrame: DataFrame containing the original data, SMA, EMA, and WMA.
    """

    # Simple Moving Average (SMA)
    sma = data.rolling(window=window_size).mean()

    # Exponential Moving Average (EMA)
    ema = data.ewm(span=window_size, adjust=False).mean()

    # Weighted Moving Average (WMA)
    weights = np.arange(1, window_size + 1)  # Create weights (1, 2, 3... window_size)
    wma = data.rolling(window=window_size).apply(lambda x: np.dot(x, weights)/weights.sum(), raw=True)

    # Create DataFrame to store all results
    df = pd.DataFrame({
        'Original Data': data,
        'SMA': sma,
        'EMA': ema,
        'WMA': wma
    })

    return df

# Example usage with sample data
data = pd.Series([22, 24, 25, 23, 26, 28, 27, 29, 30, 28])
window_size = 5

stock = Stock('2330')
tprice = stock.price
print(tprice)
t_data = pd.Series(tprice)

result_df = calculate_moving_averages(t_data, window_size)
print(result_df)
