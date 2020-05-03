import json
import urllib.request

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

invoke('createDeck', deck='test1')
result = invoke('deckNames')
print('got list of decks: {}'.format(result))



# sample = [
#             {
#                 "deckName": "Default",
#                 "modelName": "Basic",
#                 "fields": {
#                     "Front": "front content",
#                     "Back": "back content"
#                 },
#                 "tags": [
#                     "yomichan"
#                 ],
#                 "audio": [{
#                     "url": "https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji=猫&kana=ねこ",
#                     "filename": "yomichan_ねこ_猫.mp3",
#                     "skipHash": "7e2c2f954ef6051373ba916f000168dc",
#                     "fields": [
#                         "Front"
#                     ]
#                 }]
#             }, 
#             {
#                 "deckName": "Default",
#                 "modelName": "Basic",
#                 "fields": {
#                     "Front": "front content1",
#                     "Back": "back content"
#                 },
#                 "tags": [
#                     "yomichan"
#                 ],
#                 "audio": [{
#                     "url": "https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji=猫&kana=ねこ",
#                     "filename": "yomichan_ねこ_猫.mp3",
#                     "skipHash": "7e2c2f954ef6051373ba916f000168dc",
#                     "fields": [
#                         "Front"
#                     ]
#                 }]
#             }
#         ]
# invoke('addNotes', notes=sample)