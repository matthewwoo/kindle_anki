class Note(object): 

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
                    "allowDuplicate":false,
                    "duplicateScope":self.deck
                },
                "tags": [
                    self.tags
                ]
            }


