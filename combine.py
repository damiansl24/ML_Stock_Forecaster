import os
import pandas as pd
import chardet
import datetime

csv_folder = "/Users/souhoonlee/Desktop/YISS ML/Final assignment/datasets/Data_market"
csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

start_date = "2000-01-03 00:00:00+00:00"
end_date = "2023-01-02 00:00:00+00:00"
columns_to_sum = ["Date","Open", "High", "Low", "Close"]

paths = [os.path.join(csv_folder, f) for f in csv_files]

sum_df = pd.read_csv(paths[0],usecols=columns_to_sum)

sum_df['Date'] = pd.to_datetime(sum_df['Date'], utc = True, format='%Y-%m-%d %H:%M:%S%z')
sum_df["Date"] = sum_df["Date"].dt.normalize()

sum_df = sum_df[(sum_df['Date'] >= start_date) & (sum_df['Date'] <= end_date)]
sum_df.set_index('Date', inplace=True)

for path in paths[1:]:
    df = pd.read_csv(path,usecols=columns_to_sum)
    df['Date'] = pd.to_datetime(df['Date'], utc=True, format='%Y-%m-%d %H:%M:%S%z')
    df["Date"] = df["Date"].dt.normalize()
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df.set_index('Date', inplace=True)
    sum_df = sum_df.add(df, fill_value=0)

sum_df.to_csv("TOTAL_MARKET.csv", index=True)