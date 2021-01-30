# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
#url = 'https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&limit=5'
url='https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&q=2019'
result = requests.get(url).json()
# Try out the following codes
# Try to understand the result and figure out how is the data
#stored in json.
print(result.keys())
print(result['result'])

#url='https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&q=jones'

import pandas as pd
### Replace the highlighted part with json data containing the data records.
df = pd.DataFrame(result["result"]["records"])

print(df[(df.level_1=="Total Residents")&(df.level_2=="90 Years & Over")])

