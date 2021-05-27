#Requests : send http requests easily

import requests

#URL= "https://httpbin.org/post"

#print(requests.__version__)

#GET REQUESTS : get data from the server and save the output in response object

"""parameters = {'key1' : 'value1'}

response = requests.get("https://httpbin.org/get" , params = parameters)

print(response.url)
"""

#POST request : send data to the server to process for example

"""payload = {'key1' : 'value1'}

response = requests.post(URL , data = payload)

print(response.json())"""


"""parameters = {'key1' : 'value1'}
mycookies = {"k1" : "v1"}

response = requests.get("https://httpbin.org/get" ,cookies= mycookies)

print(response.text)"""

#print(response.headers)

"""with open("extracted_image.png" , "wb") as file :

    file.write(response.content)"""


"""url = "https://httpbin.org/post"

parameters = {}

parameters["uname"]  = "Soorya"
parameters["passwd"]  = 10

response = requests.post(url= url , data = parameters)

print(response.json())"""


url = "https://httpbin.org/delay/1"


response = requests.get(url , auth = ("soorya","testing") , timeout= 3)

print(response.ok)