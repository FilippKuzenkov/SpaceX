import requests
import pandas as pd
"""
response = requests.get('https://api.spacexdata.com/v4/launches')
data = response.json()
df = pd.DataFrame(data)
print(df.head(5))
"""
url = 'https://api.spacexdata.com/v4/launches'
df = pd.read_json(url)
print(df.head())
print(df.columns)
print(df.types)