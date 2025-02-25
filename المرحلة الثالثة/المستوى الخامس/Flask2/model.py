import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# بيانات تدريب بسيطة (إيجابي: 1, سلبي: 0)
data = {
    'text': [
        'أحب هذا المنتج، إنه رائع!',
        'تجربة سيئة للغاية، أنا غير راضٍ.',
        'شكرًا، لقد كان يومًا جيدًا.',
        'لم أستمتع بهذا الفيلم على الإطلاق.',
        'الخدمة كانت ممتازة، أنا سعيد جدًا.',
        'هذا أسوأ شيء اشتريته على الإطلاق.'
    ],
    'label': [1, 0, 1, 0, 1, 0]  # 1: إيجابي, 0: سلبي
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# تقسيم البيانات إلى بيانات تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# إنشاء نموذج باستخدام Naive Bayes
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# حفظ النموذج
joblib.dump(model, 'sentiment_model.pkl')