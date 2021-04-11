import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

def chatbot(question):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('intents.json', 'r',encoding="utf8") as json_data:
        intents = json.load(json_data)

    FILE = "data.pth"
    data = torch.load(FILE,map_location='cpu')

    input_size = data["input_size"]
    hidden_size00 = data["hidden_size00"]
    hidden_size01 = data["hidden_size01"]
    hidden_size02 = data["hidden_size02"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size00, hidden_size01, hidden_size02, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()
    
    while True:
        # sentence = "do you use credit cards?"
        sentence = question
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    return(random.choice(intent['responses']))
        else:
            return('Sorry I do not understand..')