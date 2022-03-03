import requests

# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r)  # <Response [200]>
# print(r.url)  # https://httpbin.org/get?page=2&count=25
# print(r.text)  # This will give response for the html page requested
# '''
# {
#   "args": {
#     "count": "25",
#     "page": "2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.27.1",
#     "X-Amzn-Trace-Id": "Root=1-61f34c39-7c7efae273a85a7728cdbd06"
#   },
#   "origin": "122.162.225.74",
#   "url": "https://httpbin.org/get?page=2&count=25"
# }
# '''
# print(r.content)  # This prints out the bytes for png file requested in the URL
# with open('comic.png', 'wb') as f:
#     f.write(r.content)  # This will create same png file.
# print(r.status_code)  # 200
# print(r.ok)  # True
# print(r.headers)  # {'Date': 'Fri, 28 Jan 2022 01:47:35 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '9593', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
#
#
# Post requests with some data
payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
r_dict = r.json()
print(r.json())  # this will create Python dictionary from json response.
'''
#  {'args': {}, 'data': '', 'files': {}, 
# 'form': {'password': 'testing', 'username': 'corey'}, 
# 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 
# 'Content-Length': '31', 'Content-Type': 'application/x-www-form-urlencoded', 
# 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.27.1',
# 'X-Amzn-Trace-Id': 'Root=1-61f350b3-5f4fc59e05f175a1076966ed'}, 'json': None, 
# 'origin': '122.162.225.74', 'url': 'https://httpbin.org/post'}
'''
print(r_dict['form'])  #  {'password': 'testing', 'username': 'corey'}


# Put, requests.put

r = requests.get('https://httpbin.org/basic-auth/corey/testing')
r = requests.get('https://httpbin.org/delay/1')

# 401 when wrong creds are passed

'''

If you've used languages other than python, you're probably thinking urllib and urllib2 are easy to use, not much code, and highly capable, that's how I used to think. But the requests package is so unbelievably useful and short that everyone should be using it.

First, it supports a fully restful API, and is as easy as:

import requests

resp = requests.get('http://www.mywebsite.com/user')
resp = requests.post('http://www.mywebsite.com/user')
resp = requests.put('http://www.mywebsite.com/user/put')
resp = requests.delete('http://www.mywebsite.com/user/delete')
Regardless of whether GET / POST, you never have to encode parameters again, it simply takes a dictionary as an argument and is good to go:

userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}
resp = requests.post('http://www.mywebsite.com/user', data=userdata)
Plus it even has a built in JSON decoder (again, I know json.loads() isn't a lot more to write, but this sure is convenient):

resp.json()
Or if your response data is just text, use:

resp.text

urllib and urllib2 are both Python modules that do URL request related stuff but offer different functionalities.

1) urllib2 can accept a Request object to set the headers for a URL request, urllib accepts only a URL.

2) urllib provides the urlencode method which is used for the generation of GET query strings, urllib2 doesn't have such a function. This is one of the reasons why urllib is often used along with urllib2.

Requests - Requests’ is a simple, easy-to-use HTTP library written in Python.

1) Python Requests encodes the parameters automatically so you just pass them as simple arguments, unlike in the case of urllib, where you need to use the method urllib.encode() to encode the parameters before passing them.

2) It automatically decoded the response into Unicode.

3) Requests also has far more convenient error handling.If your authentication failed, urllib2 would raise a urllib2.URLError, while Requests would return a normal response object, as expected. All you have to see if the request was successful by boolean response.ok
'''

