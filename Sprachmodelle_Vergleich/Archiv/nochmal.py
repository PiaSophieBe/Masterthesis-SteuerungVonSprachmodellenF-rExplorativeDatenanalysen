import pandas as pd
import glob
import weiteres


stationID = weiteres.stationID
stations = weiteres.stations
stations = stations.rename(columns={'uuid': 'station_uuid'})
csv_files = glob.glob('Preise2024/**/*.csv')

combined_df = pd.DataFrame()
count = 0
for csv_file in csv_files:
    count += 1
    df = pd.read_csv(csv_file)
    print(csv_file)
    print(count)
    df = df[df['station_uuid'].isin(stationID)]
    combined_df = pd.concat([combined_df, df])
    combined_df = combined_df.drop_duplicates().reset_index(drop=True)

joined = pd.merge(stations, combined_df, on='station_uuid', how='inner')
joined.to_csv('wichtig_joined.csv')