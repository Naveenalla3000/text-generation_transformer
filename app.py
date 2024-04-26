import os
from flask import Flask, request, render_template
from transformers import pipeline
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
generator = pipeline("text-generation",model='distilgpt2')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['POST'])
def generate_text():
	try:
		text = request.form['text']
		generated_texts = generator(text, max_length=100, do_sample=True, num_return_sequences=4)
		return render_template('index.html', generated_texts=generated_texts)
	except Exception as e:
		logger.error(e)
if __name__ == '__main__':
	app.debug = False
	app.run(host='0.0.0.0')