import json

# Read data from data.json file
with open('data.json', 'r') as file:
    response = json.load(file)

# Convert dictionary to formatted string
response_string = ""
for key, value in response.items():
    response_string += f"{key}: {value}\n"

# Write formatted string to a text file
with open('response.txt', 'w') as file:
    file.write(response_string)