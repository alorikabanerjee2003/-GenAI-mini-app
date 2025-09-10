# GenAI Mini App


![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-2.3-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

**GenAI Mini App** is a simple web application built with **Flask** and **OpenAI’s API** that generates text responses based on user prompts. Users can enter any prompt, choose a model, and receive AI-generated output in real-time. The app features a clean frontend with HTML/CSS and supports local execution via Python virtual environments. Environment variables are handled securely using **python-dotenv**. It can be shared over the internet using **ngrok** for temporary public URLs. This project demonstrates full-stack Python development, API integration, and deploying AI-powered applications in a user-friendly interface.

## Features
- Input a prompt and get AI-generated text
- Choose AI model (default: gpt-4o-mini)
- Clean HTML/CSS frontend
- Local execution via Python venv
- Secure environment variable handling with `.env`
- Temporary public access via ngrok

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/alorikabanerjee2003/-GenAI-mini-app.git
   
2. Navigate to the project folder:
   cd genai-mini-app

  
4. Create and activate a virtual environment:
   python -m venv venv
   
venv\Scripts\activate      # Windows

source venv/bin/activate   # macOS/Linux


5. Install dependencies:
   pip install -r requirements.txt
   
7. Create a .env file in the project root with your OpenAI API key:
   OPENAI_API_KEY=your_openai_api_key


Usage
1. Start the Flask app:
   python app.py
2. (Optional) Run ngrok to share publicly:
   ngrok.exe http 7860
3. Open the URL in your browser (http://127.0.0.1:7860 locally or the ngrok URL for public access).


Contributing
Feel free to submit issues or pull requests. Make sure not to commit your .env or venv/.


License
This project is licensed under the MIT License.


---

If you want, I can **also make it even prettier** with a screenshot of your app and badges like Python version, Flask, and OpenAI, so it **looks super professional on GitHub**.  
Do you want me to do that?

![public_url](https://github.com/user-attachments/assets/e17199aa-0ddf-4753-b923-7d70a0e3ca26)
<img width="1832" height="882" alt="local_host" src="https://github.com/user-attachments/assets/b9d5679d-9dc9-4412-ae40-d08055754b27" />
<img width="1082" height="887" alt="genai_app" src="https://github.com/user-attachments/assets/cf15f3ac-bdb6-41be-b58a-759e52fff2d2" />
