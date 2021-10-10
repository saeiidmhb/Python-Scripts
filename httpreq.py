import json
import requests



headers = {'Content-Type': 'application/json'}

def req(url):
    x = True
    y = False
    api_url = url
    try:
        response = requests.get(url= api_url, headers= headers)
        code = response.status_code
        if code == 200:
            return bool(x)
        else:
            return bool(y)
    except:
        return bool(y)