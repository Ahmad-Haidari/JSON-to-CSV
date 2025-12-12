import pandas as pd
import json

with open("data.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)

print("JSON converted to CSV.")
