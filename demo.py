import requests
r = requests.get('http://www.baidu.com')

r.encoding = r.apparent_encoding

print(r.apparent_encoding)
print(r.text)
print(r.encoding)

print(r.content)

