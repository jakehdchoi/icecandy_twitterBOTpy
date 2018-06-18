
import json

# json.dump writes to a file or file-like object, whereas json.dumps returns a string
# if saved with string, it's hard to load

# save
with open('database_json/example.json', 'w') as f:
    json.dump(data, f)

# read
with open('database_json/example.json', 'r') as f:
    fileData = json.load(f)


'r' : use for reading
'w' : use for writing
'x' : use for creating and writing to a new file
'a' : use for appending to a file
'r+' : use for reading and writing to the same file
