from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'
menu_data = {
    "non-veg-starters": {
        "name": "Non-Veg Starters",
        "items": [
            {"name": "Chicken Lollipop", "price": 120, "image": "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?auto=format&fit=crop&w=400&q=80"},
            {"name": "Tandoori Chicken", "price": 150, "image": "https://images.unsplash.com/photo-1604909053410-70b7b88e8455?auto=format&fit=crop&w=400&q=80"},
            {"name": "Chicken Wings", "price": 130, "image": "https://images.unsplash.com/photo-1602333869840-31c0d2d6d43a?auto=format&fit=crop&w=400&q=80"},
            {"name": "Chicken Seekh Kebab", "price": 140, "image": "https://images.unsplash.com/photo-1598514982885-c3caca46e6ef?auto=format&fit=crop&w=400&q=80"},
            {"name": "Fish Fingers", "price": 160, "image": "https://images.unsplash.com/photo-1621996346565-47d42fb1504d?auto=format&fit=crop&w=400&q=80"}
        ]
    },
    "veg-starters": {
        "name": "Veg Starters",
        "items": [
            {"name": "Paneer Tikka", "price": 100, "image": "https://images.unsplash.com/photo-1671214068025-5b2e159ea1d7?auto=format&fit=crop&w=400&q=80"},
            {"name": "Veg Spring Roll", "price": 90, "image": "https://images.unsplash.com/photo-1608219555690-c6018fe49d6c?auto=format&fit=crop&w=400&q=80"},
            {"name": "Stuffed Mushrooms", "price": 110, "image": "https://images.unsplash.com/photo-1649887324735-2cc586b7e019?auto=format&fit=crop&w=400&q=80"},
            {"name": "Hara Bhara Kebab", "price": 95, "image": "https://images.unsplash.com/photo-1671047394125-85c3d6bbf0ef?auto=format&fit=crop&w=400&q=80"},
            {"name": "Crispy Corn", "price": 105, "image": "https://images.unsplash.com/photo-1589308078057-42eeb1d990f4?auto=format&fit=crop&w=400&q=80"}
        ]
    },
    "soups": {
        "name": "Soups",
        "items": [
            {"name": "Sweet Corn Soup", "price": 80, "image": "https://images.unsplash.com/photo-1590080875512-34c5cf4fe7da?auto=format&fit=crop&w=400&q=80"},
            {"name": "Tomato Soup", "price": 75, "image": "https://images.unsplash.com/photo-1625942082121-395a18b9d2fa?auto=format&fit=crop&w=400&q=80"},
            {"name": "Hot & Sour Soup", "price": 85, "image": "https://images.unsplash.com/photo-1635687988486-1acdb3fa31f1?auto=format&fit=crop&w=400&q=80"},
            {"name": "Chicken Soup", "price": 95, "image": "https://images.unsplash.com/photo-1647914445592-b9b20ffb94a9?auto=format&fit=crop&w=400&q=80"},
            {"name": "Manchow Soup", "price": 90, "image": "https://images.unsplash.com/photo-1606971802640-01486cf9c7d5?auto=format&fit=crop&w=400&q=80"}
        ]
    },
    "fish-sea-food": {
        "name": "Fish & Sea food",
        "items": [
            {"name": "Grilled Fish", "price": 180, "image": "https://images.unsplash.com/photo-1590080875594-4c9f42ef33b4?auto=format&fit=crop&w=400&q=80"},
            {"name": "Prawn Curry", "price": 200, "image": "https://images.unsplash.com/photo-1663851477021-92f51a016be0?auto=format&fit=crop&w=400&q=80"},
            {"name": "Fish Tikka", "price": 175, "image": "https://images.unsplash.com/photo-1645918095576-92771d0a6172?auto=format&fit=crop&w=400&q=80"},
            {"name": "Crab Masala", "price": 220, "image": "https://images.unsplash.com/photo-1629110073342-df8795972403?auto=format&fit=crop&w=400&q=80"},
            {"name": "Prawn Tempura", "price": 190, "image": "https://images.unsplash.com/photo-1587595431973-160d0d23143a?auto=format&fit=crop&w=400&q=80"}
        ]
    },
    "main-course": {
        "name": "Main Course",
        "items": [
            {"name": "Paneer Butter Masala", "price": 140, "image": "https://images.unsplash.com/photo-1667131668250-f18495df2da5?auto=format&fit=crop&w=400&q=80"},
            {"name": "Butter Chicken", "price": 160, "image": "https://images.unsplash.com/photo-1620132823300-b6f36f8f6ef1?auto=format&fit=crop&w=400&q=80"},
            {"name": "Veg Biryani", "price": 130, "image": "https://images.unsplash.com/photo-1626531408623-8826977a39dc?auto=format&fit=crop&w=400&q=80"},
            {"name": "Chicken Biryani", "price": 150, "image": "https://images.unsplash.com/photo-1605478371312-21504c5ecb45?auto=format&fit=crop&w=400&q=80"},
            {"name": "Dal Makhani", "price": 120, "image": "https://images.unsplash.com/photo-1668945234707-419405a9dfe1?auto=format&fit=crop&w=400&q=80"}
        ]
    },
    "noodles": {
        "name": "Noodles",
        "items": [
            {"name": "Veg Hakka Noodles", "price": 90, "image": "https://images.unsplash.com/photo-1609336706725-093cc9061b60?auto=format&fit=crop&w=400&q=80"},
            {"name": "Chicken Noodles", "price": 100, "image": "https://images.unsplash.com/photo-1626808642872-8429bc5b24c5?auto=format&fit=crop&w=400&q=80"},
            {"name": "Schezwan Noodles", "price": 95, "image": "https://images.unsplash.com/photo-1676213471953-591d57ec1f25?auto=format&fit=crop&w=400&q=80"},
            {"name": "Egg Noodles", "price": 98, "image": "https://images.unsplash.com/photo-1649998070426-663333f33865?auto=format&fit=crop&w=400&q=80"},
            {"name": "Mixed Noodles", "price": 110, "image": "https://images.unsplash.com/photo-1615719413546-e772e6bd276e?auto=format&fit=crop&w=400&q=80"}
        ]
    },
    "salads": {
        "name": "Salads",
        "items": [
            {"name": "Caesar Salad", "price": 80, "image": "https://images.unsplash.com/photo-1589308078057-42eeb1d990f4?auto=format&fit=crop&w=400&q=80"},
            {"name": "Greek Salad", "price": 90, "image": "https://images.unsplash.com/photo-1569058242319-bc1e5d337d37?auto=format&fit=crop&w=400&q=80"},
            {"name": "Sprout Salad", "price": 70, "image": "https://images.unsplash.com/photo-1632735399262-cab58bfeab41?auto=format&fit=crop&w=400&q=80"},
            {"name": "Cucumber Salad", "price": 65, "image": "https://images.unsplash.com/photo-1576402187875-4bda2228f42c?auto=format&fit=crop&w=400&q=80"},
            {"name": "Fruit Salad", "price": 85, "image": "https://images.unsplash.com/photo-1524592515119-2c0bd51d33c4?auto=format&fit=crop&w=400&q=80"}
        ]
    },
    "desserts": {
        "name": "Desserts",
        "items": [
            {"name": "Chocolate Ice Cream", "price": 80, "image": "https://images.unsplash.com/photo-1622012214560-6f5d42f1893e?auto=format&fit=crop&w=400&q=80"},
            {"name": "Vanilla Ice Cream", "price": 70, "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=400&q=80"},
            {"name": "Pista Ice Cream", "price": 90, "image": "https://images.unsplash.com/photo-1633212219424-84a9468ef738?auto=format&fit=crop&w=400&q=80"},
            {"name": "Strawberry Ice Cream", "price": 75, "image": "https://images.unsplash.com/photo-1599785209707-28cfed5f0f2f?auto=format&fit=crop&w=400&q=80"},
            {"name": "Mango Ice Cream", "price": 85, "image": "https://images.unsplash.com/photo-1626882048554-1ff1a94fa47a?auto=format&fit=crop&w=400&q=80"}
        ]
    }
}

@app.route("/")
def home():
    return render_template("index.html", menu_data=menu_data)

@app.route("/category/<category_name>")
def category_page(category_name):
    if category_name in menu_data:
        return render_template("category.html", category_name=menu_data[category_name]["name"], items=menu_data[category_name]["items"])
    else:
        return "Category not found", 404

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    item_name = request.form['name']
    item_price = request.form['price']
    item_image = request.form['image']
    
    if 'cart' not in session:
        session['cart'] = []

    for item in session['cart']:
        if item['name'] == item_name:
            item['quantity'] += 1
            break
    else:
        session['cart'].append({
            'name': item_name,
            'price': item_price,
            'image': item_image,
            'quantity': 1
        })

    session.modified = True
    return redirect(request.referrer or url_for('home'))

@app.route("/cart")
def view_cart():
    cart = session.get('cart', [])
    total = sum(int(item['price']) * item['quantity'] for item in cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/remove-from-cart/<item_name>")
def remove_from_cart(item_name):
    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if item['name'] != item_name]
        session.modified = True
    return redirect(url_for('view_cart'))

@app.route("/update-quantity", methods=["POST"])
def update_quantity():
    item_name = request.form['name']
    action = request.form['action']

    for item in session.get('cart', []):
        if item['name'] == item_name:
            if action == 'increase':
                item['quantity'] += 1
            elif action == 'decrease':
                item['quantity'] -= 1
                if item['quantity'] < 1:
                    session['cart'].remove(item)
            break

    session.modified = True
    return redirect(url_for('view_cart'))

@app.route("/checkout", methods=["GET"])
def checkout():
    cart = session.get('cart', [])
    total = sum(int(item['price']) * item['quantity'] for item in cart)
    return render_template("checkout.html", cart=cart, total=total)

@app.route("/place-order", methods=["POST"])
def place_order():
    name = request.form['name']
    address = request.form['address']
    payment_method = request.form['payment_method']
    cart = session.get('cart', [])
    total = sum(int(item['price']) * item['quantity'] for item in cart)

    # Simulate saving order (you could save to database here)
    session.pop('cart', None)  # clear cart after placing order

    return f"<h2>Thank you, {name}!</h2><p>Your order has been placed.<br>Delivery Address: {address}<br>Payment Method: {payment_method}<br><strong>Total Paid: ₹{total}</strong></p><a href='/'>Back to Home</a>"


# === MAIN ENTRY POINT ===

if __name__ == "__main__":
    app.run(debug=True)