import requests
import json
import os
endpoint="https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status,contentDetails,id"
filename = input("Please input the filename you wish to upload as the first part of the video")
f = open(filename,'rb')
chunksize = 262144
token_file = open('token.json')
token_data = json.load(token_file)
token_file.close()
file_size = os.path.getsize('replace_before.mpg')
headers = {
    'Authorization': 'Bearer {}'.format(token_data['access_token']),
    'X-Upload-Content-Length': str(file_size),
    'X-Upload-Content-Type': 'application/octet-stream'
}
video_data = {
    "snippet": {
        "title": "This video has its own URL in it",
        "description": "this is a test"
    },
    "status": {
        "privacyStatus": "private",
        "embeddable": True,
        "license": "youtube"
    }
}
r = requests.post(endpoint, headers=headers, json=video_data)
if(r.status_code == 401):
    print("Acesss token has expired, please run oauth_refresh.py to regenerate the token.")
print(r.text)
print(r.status_code)
video_upload_endpoint = r.headers["Location"]
binary_data = f.read(chunksize)
curbyte = 0
while binary_data:
    upload_headers = {
        'Authorization': 'Bearer {}'.format(token_data['access_token']),
        'Content-Length': str(len(binary_data)),
        'Content-Range': "bytes {}-{}/{}".format(curbyte,curbyte+len(binary_data)-1,file_size),
        'Content-Type': 'application/octet-stream'
    }
    print("{}-{}/{}".format(curbyte,curbyte+len(binary_data)-1,file_size))
    r = requests.put(video_upload_endpoint, headers=upload_headers, data=binary_data)
    print(r.text)
    if(curbyte == 0):
        interrupt = input("Please input the filename of the second video you wish to combine with the first one.")
        f.close()
        f = open(interrupt,'rb')
        binary_data = f.read(chunksize)
    curbyte += len(binary_data)
    binary_data = f.read(chunksize)