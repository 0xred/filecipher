![alt text](https://raw.githubusercontent.com/0xred/filecipher/main/pic.png)

# 🛡️ File Cipher - AES-256 Encryption Tool

أداة بسيطة لتشفير وفك تشفير الملفات باستخدام خوارزمية **AES-256** مع واجهة تحكم تفاعلية.

![CLI Preview](https://via.placeholder.com/800x400?text=CLI+Preview+Here) <!-- يمكنك إضافة صورة للواجهة -->

## ✨ المميزات
- تشفير الملفات بمعيار **AES-256-CBC**
- دعم جميع أنواع الملفات (نصوص، صور، فيديوهات، إلخ)
- واجهة رسومية لاختيار الملفات
- توليد مفتاح التشفير من كلمة مرور باستخدام **MD5 Hash**
- توافق مع نظام ويندوز

## ⚙️ طريقة التثبيت (Windows)
**المتطلبات المسبقة**:  
- [Python 3.7+](https://www.python.org/downloads/)
- `pip` (يأتي مع تثبيت بايثون)

```cmd
:: 1. تثبيت المكتبات المطلوبة
pip install pycryptodome

:: 2. تنزيل البرنامج (طريقة بديلة)
git clone https://github.com/yourusername/file-cipher.git
