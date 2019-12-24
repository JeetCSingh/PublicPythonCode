import pandas as pd
import json

df=pd.read_excel("Expected_Action.xlsx")

df=pd.DataFrame(df[['Intent','body']])
df.columns=['intent','text']

df.to_json('dummy.json',orient='records')
with open('dummy.json') as json_data:
    d = json.load(json_data)    

sample={"rasa_nlu_data": {"common_examples":d}}

s=json.dumps(sample)

with open('model.json','w') as json_data:
    json_data.write(s)