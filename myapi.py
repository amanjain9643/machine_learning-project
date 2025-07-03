import nlpcloud
class API:
    def __init__(self):
        # self.client = nlpcloud.Client("finetuned-llama-3-70b", "21a3ec6faf8314861819adf5683f2621b1b1150b", gpu=True)
        self.client = nlpcloud.Client("finetuned-llama-3-70b", "c50d91132bef85f1b550b2440348fd95888cbb6c", gpu=True)
    def sentiment_analysis(self,text):
        response=self.client.sentiment(
        text,
        target="NLP Cloud"
        )
        return response
    
    def ner_analysis(self,text,entity):
        # response =self.client.entities(text,entity)
        # return response['entities']
        return {'entities': [{'start': 26, 'end': 36, 'type': 'programming languages', 'text': 'Javascript'}, {'start': 102, 'end': 108, 'type': 'programming languages', 'text': 'Python'}, {'start': 165, 'end': 167, 'type': 'programming languages', 'text': 'Go'}]}


        