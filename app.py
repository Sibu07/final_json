import json
import requests

url = input("Enter the URL of the JSON data: ")
response = requests.get(url)

data = json.loads(response.content.decode("utf-8"))

chunk_size = 20 # Set the number of records you want in each file
num_chunks = len(data) // chunk_size + (len(data) % chunk_size != 0) # Calculate the number of chunks needed

prefix = input("Enter the file name prefix: ")

for i in range(num_chunks):
    start_index = i * chunk_size
    end_index = min((i + 1) * chunk_size, len(data))

    chunk = data[start_index:end_index]

    filename = f"{prefix}_{i+1}.json" # Name the file based on the current chunk number and prefix, with an underscore in between
    with open(filename, "w") as f:
        json.dump(chunk, f)
