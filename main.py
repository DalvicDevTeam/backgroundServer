from Channel import Channel
import requests
import json
import time


while True:
    print("going..")
    resp = requests.get('http://127.0.0.1:8000/api/channels')
    channels = json.loads(resp.text)
    channels = channels['data']
    print("length: " + str(len(channels)))
    print(channels)
    for channel in channels:
        username = channel['username']
        newchannel = Channel(username)
        if newchannel.title != channel['title'] or newchannel.subscribers_count != channel['members'] :
            newchannel = {
                    'title': newchannel.title,
                    'description': newchannel.description,
                    'members': newchannel.subscribers_count,
                }
            url = 'http://127.0.0.1:8000/api/channel/' + str(channel['id'])
            print(url)
            time.sleep(20)
            resp = requests.put(url, data=newchannel)
            print(resp.status_code)
    time.sleep(3600)

