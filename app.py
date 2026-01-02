import os
from flask import Flask, render_template

# إعداد التطبيق
app = Flask(__name__, template_folder='templates', static_folder='static')

# الصفحة الرئيسية (Dashboard)
@app.route('/')
def dashboard():
    return render_template('index.html')

# تشغيل السيرفر
if __name__ == '__main__':
    # قراءة المنفذ من البيئة أو استخدام 5000 كافتراضي
    port = int(os.environ.get("PORT", 5000))
    # استخدام '0.0.0.0' ليسمح بالوصول من الإنترنت
    app.run(host='0.0.0.0', port=port)
