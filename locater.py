from requests import get

ip = get('https://api.ipify.org').text
data = get(f'http://ip-api.com/json/{ip}')
info = data.json()

#print(info)

print(f"Status : {info['status']}")
print(f"Country : {info['country']}")
