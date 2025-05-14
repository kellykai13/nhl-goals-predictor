import requests
import json
import pandas as pd
import re

url = "https://api-web.nhle.com/v1/standings/now"
response = requests.get(url)

if response.status_code == 200:
    standings_data = response.json()
    ##print(standings_data)  # Check out the keys for the standings
else:
    print("Error:", response.status_code)


df = pd.json_normalize(standings_data['standings'], sep='_')

df.columns = [re.sub(r'(?<!^)(?=[A-Z])', '_', col).lower() for col in df.columns]
standings_df = df.drop(columns=['team_name_fr', 'team_common_name_fr', 'place_name_fr'])