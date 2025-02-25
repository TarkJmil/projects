import os

class SimpleSearchEngine:
    def __init__(self, directory):
        self.directory = directory  # المجلد الذي يحتوي على الملفات النصية

    def search(self, keyword):
        results = []
        # البحث في جميع الملفات داخل المجلد
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):  # نتعامل فقط مع الملفات النصية
                filepath = os.path.join(self.directory, filename)
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()
                    # إذا كانت الكلمة المفتاحية موجودة في النص
                    if keyword.lower() in content.lower():
                        results.append((filename, content))
        return results

# مثال على الاستخدام
if __name__ == "__main__":
    # إنشاء مجلد يحتوي على ملفات نصية
    directory = "text_files"  # قم بإنشاء مجلد باسم "text_files" وضع فيه ملفات نصية
    if not os.path.exists(directory):
        os.makedirs(directory)
        # إنشاء ملفات نصية كمثال
        with open(os.path.join(directory, "file1.txt"), "w", encoding="utf-8") as f:
            f.write("هذا ملف نصي يحتوي على كلمات للبحث.")
        with open(os.path.join(directory, "file2.txt"), "w", encoding="utf-8") as f:
            f.write("محرك البحث Tark البسيط يعمل بشكل جيد.")
        with open(os.path.join(directory, "file3.txt"), "w", encoding="utf-8") as f:
            f.write("هنا مثال Tark آخر على محتوى نصي.")

    # إنشاء كائن محرك البحث
    search_engine = SimpleSearchEngine(directory)

    # البحث عن كلمة مفتاحية
    keyword = "بحث"
    results = search_engine.search(keyword)

    # عرض النتائج
    if results:
        print(f"تم العثور على {len(results)} نتيجة للكلمة المفتاحية '{keyword}':")
        for filename, content in results:
            print(f"\nالملف: {filename}")
            print(f"المحتوى: {content}")
    else:
        print(f"لم يتم العثور على أي نتائج للكلمة المفتاحية '{keyword}'.")