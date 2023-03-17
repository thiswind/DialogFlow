from flask import Flask, render_template, request
import openai

app = Flask(__name__)


@app.route('/')
def chat_page():
    return render_template('chat.html.jinja2')


@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    response_message = process_user_message(user_message)
    return response_message


def process_user_message(message):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                                "role":
                                                "system",
                                                "content":
                                                "You are a helpful assistant."
                                            }, {
                                                "role": "user",
                                                "content": message
                                            }])
    response_message = response['choices'][0]['message']['content']
    return response_message


@app.route('/set_api_key', methods=['POST'])
def set_api_key():
    api_key = request.form['api_key']
    openai.api_key = api_key
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
