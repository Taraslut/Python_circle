import os

import requests

url = 'https://api.vkino.com.ua/posters/b8/b8a4d362c276acd06d09f999e3cae5faa3e42e40.C180x260.jpg'

response = requests.get(url, stream=True)
extension = url.split(".")[-1]

file_name = "one."+extension
base_path = os.path.dirname(__file__)

file_name_path = os.path.join(base_path, file_name)
with open(file_name_path, "bw") as f:
    f.write(response.content)