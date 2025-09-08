import pandas as pd
import glob

csv_files = glob.glob('Stationen2024/**/*.csv')
print(csv_files)
combined_df = pd.DataFrame()
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    combined_df = pd.concat([combined_df, df])
    combined_df = combined_df.drop_duplicates().reset_index(drop=True)

stations = combined_df
station_minden = stations[stations['city'] == 'Minden']
stationen_minden = station_minden.drop_duplicates(subset='uuid')
stationen_minden = stationen_minden.rename(columns={'uuid': 'station_uuid'})
#joined = pd.merge(station_minden, prices, on='station_uuid', how='inner')
#joined.to_csv('df_tank.csv')
station_minden.to_csv('Minden.csv')
