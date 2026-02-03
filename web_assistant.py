from gemini_client import *
from flask import Flask, request, render_template


app = Flask(__name__)
client = GeminiClient()

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def index():
    response = ''
    prompt = ''

    if request.method == 'POST':
       prompt = request.form.get('prompt')

       if prompt:
        response = client.generate_response(prompt)

    return render_template('index.html', response=response, prompt=prompt)

def main():
  app.run(host='localhost', port=9500)

if __name__ == "__main__":
  main()