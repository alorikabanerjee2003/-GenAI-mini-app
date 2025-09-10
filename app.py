from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

# Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Initialize client
client = OpenAI(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json or {}
    prompt = data.get('prompt', '').strip()
    model = data.get('model', 'gpt-4o-mini')
    temp = float(data.get('temperature', 0.7))

    if not prompt:
        return jsonify({'error': 'Prompt is empty.'}), 400

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            temperature=temp,
            max_tokens=500
        )
        text = response.choices[0].message.content.strip()
        return jsonify({'result': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=True)
