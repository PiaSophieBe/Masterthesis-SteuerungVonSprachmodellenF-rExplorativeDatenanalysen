import requests
import pandas as pd

url = "https://creativecommons.tankerkoenig.de/json/list.php?lat=52.52099975265203&lng=13.43803882598877&rad=4&sort=price&type=diesel&apikey=09bcd891-16d8-f048-038a-63ccc0e906b0"
response = requests.get(url)
response_json = response.json()
df = pd.DataFrame(response_json)
#print(response_json)
print(df.head())

print(response.status_code)
