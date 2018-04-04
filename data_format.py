import pandas as pd
import numpy as np
# def get_columns(csv_filename):
#     df = pd.read_csv(csv_filename)


df = pd.read_csv('a4424.csv')

# print(df['used_power'])



used_power = df['used_power'].tolist()

print(used_power)

datetime = df['datetime'].tolist()
# print(datetime)
