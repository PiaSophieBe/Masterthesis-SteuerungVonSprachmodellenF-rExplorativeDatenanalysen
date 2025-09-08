import pandas as pd

#df = pd.read_csv('stations.csv')
#df = df.drop_duplicates(subset='uuid') #60274
#df = df.reset_index(drop=True)
#print(df.info())

#df.to_csv('stations2.csv')

stations = pd.read_csv('Minden.csv')
stations = stations.drop_duplicates(subset='uuid')
stationID = stations['uuid']


prices = pd.read_csv('Dezember/2024-12-31-prices.csv')
#print(prices.info())
df = prices[prices['station_uuid'].isin(stationID)]
