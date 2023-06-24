# Python developer assigment
# Md. Azizul Hakim


from flask import Flask, jsonify
from flask_cors import CORS
import json
import os
#import subprocess
#import itertools
#import shutil
#import random
#import glob
# import yaml
#import csv
import requests
from dotenv import load_dotenv
import streamlit as st

app = Flask(__name__)

CORS(app)
# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_TOKEN = os.getenv("API_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"

headers = {"Authorization": f"Bearer {API_TOKEN}"}



# making with 


@app.route('/analyze',methods=['POST'])
def pred_api(payload):    
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.json())
    return response.json()



# this is our dummy frontend 
# HTTP POST request 
# output = pred_api({
# 	"inputs": "I hate sanam he is not a good at study", 
# })

## start
#Simple Frontend with Streamlit
st.title("Sentiment Analysis")

# Create an input text box
text = st.text_input("Enter text")

# Create a send button
if st.button("Test"):
        # Call the sentiment analysis function
    sentiment = pred_api(text)
        
    # Display the sentiment result
    st.write("Sentiment:", sentiment)

## end



if __name__ == "__main__":
    app.run(debug=True)
