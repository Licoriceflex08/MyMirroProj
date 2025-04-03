# MyMirroProj

### **Setting Up the Backend (Django + PostgreSQL)**  

Follow these steps to set up and run the backend for **My Mirro**:

---

### **Step 1: Clone the Project & Navigate**
```
git clone <your-repo-url>
cd myMirro
```

---

### **Step 2: Create & Activate Virtual Environment**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### **Step 3: Install Dependencies**
```
pip install -r requirements.txt
```
If `requirements.txt` does not exist, manually install:
```
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary
```

---

### **Step 4: Configure Database Settings**
Modify **`settings.py`** to match your PostgreSQL configuration:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fashion_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### **Step 5: Apply Migrations**
```
python manage.py migrate
```

---

### **Step 6: Create Superuser (for Admin Access)**
```
python manage.py createsuperuser
```
Enter email, username, and password when prompted.

---

### **Step 7: Run the Server**
```
python manage.py runserver
```
Server will be available at: **http://127.0.0.1:8000/**

---

### **Step 8: API Testing (Postman/cURL)**
- **Fetch products**  
  ```
  curl -X GET http://127.0.0.1:8000/api/products/
  ```
- **Get product details**  
  ```
  curl -X GET http://127.0.0.1:8000/api/products/1/
  ```
- **Log user activity (Requires JWT Authentication)**  
  ```
  curl -X POST http://127.0.0.1:8000/api/user-activity/ -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json" -d '{"product": 1, "action": "view"}'
  ```
