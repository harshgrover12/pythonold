'''
protocol : http, https, ftp...
host: en.wikipedia.org
port: http=80, https=443
path: wiki/URL
Querystring: key=value&life=42
fragment: History
200: OK
400: Bad request
403: forbidden
404: not found

'''

# urllib contains 5 modules- request, response, error, parse, robotparser

from urllib import request
print(dir(request))
response = request.urlopen('https://httpbin.org/get')
print(type(response))  # <class 'http.client.HTTPResponse'>
print(dir(response))
print(response.code)  # 200
print(response.peek())
'''
b'{\n  "args": {}, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.7", \n    "X-Amzn-Trace-Id": "Root=1-61f35763-752ad81f6c7262613008fd8c"\n  }, \n  "origin": "122.162.225.74", \n  "url": "https://httpbin.org/get"\n}\n'

'''
print(response.read())
print(response.read())  # b'', as python closes the connection once data is read

from urllib import parse

params = {"v": "EUC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)
print(querystring)  # v=EUC-yVzHhMI&t=5m56s
url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)
print(resp.isclosed())  # False, if connection is not closed.
