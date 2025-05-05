import pandas as pd
import json

# String JSON
json_data = '''
[
 {"name": "John", "age": 28, "city": "New York"},
 {"name": "Anna", "age": 22, "city": "London"},
 {"name": "Mike", "age": 32, "city": "Chicago"}
]
'''
# Converter string JSON para DataFrame
df = pd.read_json(json_data)
print(df)
