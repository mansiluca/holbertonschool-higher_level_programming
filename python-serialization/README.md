# Python Serialization

## Overview
This project covers the concepts of serialization and deserialization in Python. Serialization is the process of converting a data structure or object into a format that can be easily stored or transmitted, and deserialization is the reverse process.

## Learning Objectives
- Understand the purpose of serialization and deserialization
- Learn how to use Python's built-in `pickle` module
- Explore JSON serialization with the `json` module
- Handle custom serialization for complex objects

## Requirements
- Python 3.x
- Basic knowledge of Python programming

## Modules Covered
- `pickle`
- `json`

## Usage
### Pickle Example
```python
import pickle

# Serialize data
data = {'key': 'value'}
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize data
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print(loaded_data)
```

### JSON Example
```python
import json

# Serialize data
data = {'key': 'value'}
with open('data.json', 'w') as file:
    json.dump(data, file)

# Deserialize data
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
print(loaded_data)
```

## Author
Luca

## License
This project is licensed under the MIT License.