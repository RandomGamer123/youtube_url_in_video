import json
import requests
f = open('token_backup.json')
data = json.load(f)
refresh_token = data["refresh_token"]
f.close()
f = open('oauth_config.txt')
config = f.read().split('\n')
client_id = config[1]
client_secret = config[2]
grant_type = "refresh_token"
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token,
    'grant_type': grant_type
}
endpoint = "https://oauth2.googleapis.com/token"
r = requests.post(endpoint, data=payload)
f = open('token.json','w')
f.write(r.text)