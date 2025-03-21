from flask import Flask, render_template, request
import os
import tempfile
from utils import chatgpt,diffusion,transcribe_func
import tempfile

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sd-api',methods=['POST'])
def sd_api():
    prompt=request.json.get('prompt')
    return{
        'imageURL':'data:image/png;base64, '+diffusion(prompt)
    }



@app.route('/transcribe-api',methods=['POST'])
def transcribe_api():
    uploaded_file=request.files['file']
    original_filename=uploaded_file.filename
    _,file_extension=os.path.splitext(original_filename) # type: ignore
    with tempfile.NamedTemporaryFile(suffix=file_extension,delete=False) as temp_file:
        temp_path=temp_file.file.name
        uploaded_file.save(temp_path)
        transcription=transcribe_func(temp_path)
        temp_file.close()
    os.remove(temp_path)
    return transcription




@app.route('/gpt-api', methods=['POST'])
def gpt_api():
    # يأخذ 3 معاملات، وهما رسالة النظام ومدخلات المستخدم وإن كان الطلب يريد تقسيم المدخلات، ثم يقوم بإرجاع الرد
    system_settings = request.json.get('system_settings')
    user_input = request.json.get('user_input')
    chunk = request.json.get('chunk')
    return chatgpt(user_input, system_settings,chunk)


@app.route('/create-article')
def create_article():
    return render_template('create-article.html')


@app.route('/summarize-article')
def summarize_article():
    return render_template('summarize-article.html')


@app.route('/transcribe')
def transcribe():
    return render_template('transcribe.html')


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')


if __name__ == "__main__":
    app.run(debug=True)
