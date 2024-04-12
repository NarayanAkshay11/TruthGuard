from flask import Flask, render_template, request
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense


app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the text input from the form
        text_input = request.form['text_input']
        nnews = tokenizer.texts_to_sequences([news])
        nnnews = pad_sequences(nnews, maxlen=max_len)
        preditc =  model.predict(nnnews)
        number_to_display =  np.argmax(preditc)
        
        # Render the template with the number to display
        return render_template('index.html', number_to_display=number_to_display)
    else:
        # Render the template without displaying any number
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
