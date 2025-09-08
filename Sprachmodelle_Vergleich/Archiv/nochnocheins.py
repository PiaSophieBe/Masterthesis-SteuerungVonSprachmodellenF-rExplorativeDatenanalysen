import pandas as pd

df = pd.read_csv('wichtig_joined.csv', parse_dates=['date'], dayfirst=True)  # ggf. dayfirst anpassen

#print(df['date'])
#print(df.info())

df['date'] = pd.to_datetime(df['date'], errors='coerce')
print(df['date'].dtype)  # Muss datetime64[ns] sein
print(df['date'].isna().sum())  # Anzahl nicht-konvertierbarer Werte

df['hour'] = df['date'].dt.floor('H')  # Rundung auf volle Stunde

# Berechnung des Stundenmittelwerts pro Tankstelle
df_hourly = df.groupby(['station_uuid', 'hour'])[['diesel', 'e5', 'e10']].mean().reset_index()
df_hourly.to_csv('qwertz')
print(df_hourly)