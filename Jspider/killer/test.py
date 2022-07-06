import  requests,pprint

payload = {
    'username': 'byby',
    'password': '88888888'
}
response = requests.post('http://localhost/killer/signin',
              data=payload)
pprint.pprint(response.json())
# response = requests.get('http://localhost/killer/test')
#
# pprint.pprint(response.json())