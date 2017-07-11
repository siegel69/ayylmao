import requests
import json

def main():
    print("hello")

    """
    '{"bot": { "name": "new test bot", "group_id": "32008860"}"}'
    https://api.groupme.com/v3/bots?token=6G8SBZocwVRrTSZ300Qe4YIiaEqcGALKSDAlZW4c
    """

    #r = requests.post('http://httpbin.org/post', data = {'key':'value'})

    token = "6G8SBZocwVRrTSZ300Qe4YIiaEqcGALKSDAlZW4c"

    url = "https://api.groupme.com/v3/bots"

    name = "Tim4"

    groupID = "32008860"

    cbURL = ""
    
    dest = "/destroy"

    data2 = {"bot":{"name": name, "group_id": groupID, "callback_url": cbURL}}

    r = requests.post(url + "?token=" + token, data = json.dumps(data2), headers={'content-type': 'application/json'})
    
    print(r.text)    

    print(r.status_code, r.reason)
    
    data = r.json()
    
    tokenShit = '?token='
    
    #botID is really important for everything
    #print( data['payload'])
    print(data)
    botID = data['response']["bot"]["bot_id"]
    
    '''
    https://api.groupme.com/v3/groups/:32008860/messages?token=6G8SBZocwVRrTSZ300Qe4YIiaEqcGALKSDAlZW4c
    '''
    
    
    #post shit
    post = '/post'
    text = 'ayy lmao'
    r3 = requests.post(url+post+'?token='+token, params = {'bot_id': botID, 'text': text})
    print(r3.text)
    
    #deletes bot immediately
    r2 = requests.post(url+dest+'?token='+token, params = {'bot_id': botID})
    print(r2.text)

main()