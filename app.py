from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def chat_page():
    return render_template('chat.html.jinja2')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    # 处理用户消息并生成回复
    response_message = process_user_message(user_message)
    return response_message

def process_user_message(message):
    # 在这里实现处理用户消息并生成回复的逻辑
    response = "这里是一个示例回复，实际回复将由你的逻辑生成。"
    return response

if __name__ == '__main__':
    app.run(debug=True)
