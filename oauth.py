import requests
import urllib.parse
f = open('oauth_config.txt')
config = f.read().split('\n')
f.close()
code_challenge = config[0]
oauth_endpoint = "https://accounts.google.com/o/oauth2/v2/auth"
client_id = config[1]
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
response_type = "code"
scopes = "https://www.googleapis.com/auth/youtube https://www.googleapis.com/auth/youtube.upload"
code_challenge_method = "plain"
oauth_payload = "scope={}&response_type={}&redirect_uri={}&client_id={}&code_challenge={}&code_challenge_method={}".format(urllib.parse.quote(scopes),response_type,urllib.parse.quote(redirect_uri),urllib.parse.quote(client_id),urllib.parse.quote(code_challenge),code_challenge_method)
oauth_url = "{}?{}".format(oauth_endpoint, oauth_payload)
print(oauth_url)
oauth_code = input()

token_exchange_endpoint = "https://oauth2.googleapis.com/token"
client_secret = config[2]
grant_type = "authorization_code"
token_payload = {
    'code': oauth_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'grant_type': grant_type,
    'code_verifier': code_challenge
}
r = requests.post(token_exchange_endpoint, data=token_payload)
f = open('token.json','w')
f.write(r.text)