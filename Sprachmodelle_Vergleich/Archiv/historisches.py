import json
import pandas as pd
import glob


csv_files = glob.glob('Dezember/*.csv')
combined_df = pd.DataFrame()
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    combined_df = pd.concat([combined_df, df])
print(combined_df)



