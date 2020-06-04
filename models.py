import json
class Book(object): 
    def __init__(self,title, author,tags):
        self.title = title
        self.author = author
        self.tags = tags 

class Card(object): 

    def __init__(self,deck,front,back,tags):
        self.deck = deck
        self.front = front
        self.back = back
        self.tags = tags

    def anki_jsonify(self):
        return {
                "deckName": self.deck,
                "modelName": "Basic",
                "fields": {
                    "Front": self.front,
                    "Back": self.back
                },
                "options":{
                    "allowDuplicate":False,
                    "duplicateScope":"deck"
                },
                "tags": self.tags
            }
# Include the dump and loads, but not working
    def anki_jsonify_2(self): 
        return json.dumps({
                "deckName": self.deck,
                "modelName": "Basic",
                "fields": {
                    "Front": self.front,
                    "Back": self.back
                },
                "options":{
                    "allowDuplicate":False,
                    "duplicateScope":self.deck
                },
                "tags": [
                    self.tags
                ]
            })
        