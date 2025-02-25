import sqlite3

# الاتصال بقاعدة البيانات (إذا لم تكن موجودة، سيتم إنشاؤها)
conn = sqlite3.connect('QQQ.db')

# إنشاء كائن Cursor للتفاعل مع قاعدة البيانات
cursor = conn.cursor()

# إنشاء جدول إذا لم يكن موجودًا
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# دالة لإضافة مستخدم
def add_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    print(f"تمت إضافة المستخدم: {name} (العمر: {age})")

# دالة لحذف مستخدم
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    print(f"تم حذف المستخدم ذو المعرف: {user_id}")

# دالة لتحديث بيانات مستخدم
def update_user(user_id, new_name, new_age):
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (new_name, new_age, user_id))
    conn.commit()
    print(f"تم تحديث بيانات المستخدم ذو المعرف: {user_id}")

# دالة لاسترجاع جميع المستخدمين
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(f"المعرف: {user[0]}, الاسم: {user[1]}, العمر: {user[2]}")

# مثال على استخدام الدوال
add_user("أحمد", 25)
add_user("محمد", 30)
get_all_users()

update_user(1, "أحمد علي", 26)
get_all_users()

delete_user(2)
get_all_users()

# إغلاق الاتصال بقاعدة البيانات
conn.close()