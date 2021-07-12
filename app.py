#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_first_response

app = Flask(__name__)
# Create object of ChatBot class with Storage Adapter
bot = ChatBot(
    'Annapaola', 
    logic_adapters=["chatterbot.logic.BestMatch"],
    response_selection_method = get_first_response,
)
# Inport ListTrainer
from chatterbot.trainers import ListTrainer
trainer = ListTrainer(bot)
trainer.train([
'Hi',
'Hello',
'ruslan',
'visit ruslanmv.com'
])

# Create a new trainer for the chatbot
# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(bot)
# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")
# Now we can export the data to a file
#trainer.export_for_training('./my_export.json')
@app.route("/")
def home():  
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg') 
    response = bot.get_response(userText)
    return str(response)
if __name__ == "__main__":    
    app.run()