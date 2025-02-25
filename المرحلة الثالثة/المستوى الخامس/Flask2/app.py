from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# تحميل النموذج
model = joblib.load('sentiment_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        text = request.form['text']
        # تحليل المشاعر
        prediction = model.predict([text])[0]
        sentiment = "إيجابي" if prediction == 1 else "سلبي"
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)