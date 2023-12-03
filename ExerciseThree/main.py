import json
from pathlib import Path

data_file_path = Path(__file__).parent / "body.json" 
file = open(data_file_path, encoding="utf8")
students = json.load(file)

result = {}

for key, item in students.items():
    if int(item) < 60:
        result[key] = "Fail"
    else:
        result[key] = "Pass" 

result_file_path = Path(__file__).parent / "result.json"
with open(result_file_path, 'w', encoding='utf8') as object:
    json.dump(result, object, ensure_ascii = False, indent = 2)
    
