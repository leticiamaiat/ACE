print("Hello, world!")
import requests
import pandas as pd
import json

headers = {
    "Authorization": "Bearer test_8ed2827188b363677a14e9717c0409"
}

response = requests.get("https://api.api-futebol.com.br/v1/campeonatos/2/artilharia", headers=headers)

data = response.json()
df = pd.DataFrame(data)
print(df)
