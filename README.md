# 🍽️ Online Restaurant Web App

This is a Flask-based web application that allows users to browse food categories, view food items, add them to a cart, and checkout with a delivery address.

---

## 🚀 Features

- View food items by category (e.g., Non-Veg Starters, Desserts, etc.)
- Add items to the cart
- Increase or decrease quantity
- Remove items from cart
- Checkout with delivery address form
- User login/logout functionality
- Search functionality to find items like “Paneer”
- Responsive design using Bootstrap

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create Virtual Environment and Install Dependencies
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # On Windows
# source venv/bin/activate   # On macOS/Linux

pip install -r requirements.txt
If requirements.txt is missing, you can install manually:

bash
Copy
Edit
pip install flask
3. Run the App
bash
Copy
Edit
python app.py
Then open your browser and go to:
👉 http://127.0.0.1:5000

🔐 Login Credentials
You can log in using the following test account:

Username: krishna

Password: krishna123

🗂️ Folder Structure
cpp
Copy
Edit
online-restaurant/
├── app.py
├── templates/
│   ├── index.html
│   ├── category.html
│   ├── cart.html
│   ├── checkout.html
│   ├── login.html
│   ├── register.html
│   ├── search_results.html
│   └── base.html
├── requirements.txt
└── README.md
