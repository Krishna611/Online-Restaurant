from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'
menu_data = {
  "non-veg-starters": {
    "name": "Non‑Veg Starters",
    "items": [
      {"name": "Chicken Lollipop", "price": 120, "image": "https://source.unsplash.com/featured/?chicken-lollipop"},
      {"name": "Tandoori Chicken", "price": 150, "image": "https://source.unsplash.com/featured/?tandoori-chicken"},
      {"name": "Chicken Wings", "price": 130, "image": "https://source.unsplash.com/featured/?chicken-wings"},
      {"name": "Chicken Seekh Kebab", "price": 140, "image": "https://source.unsplash.com/featured/?chicken-kebab"},
      {"name": "Fish Fingers", "price": 160, "image": "https://source.unsplash.com/featured/?fish-fingers"},
      {"name": "Mutton Shami Kebab", "price": 170, "image": "https://source.unsplash.com/featured/?mutton-kebab"},
      {"name": "Prawn Tempura", "price": 180, "image": "https://source.unsplash.com/featured/?prawn-tempura"},
      {"name": "Chicken Malai Tikka", "price": 145, "image": "https://source.unsplash.com/featured/?chicken-tikka"},
      {"name": "Crispy Fried Chicken", "price": 135, "image": "https://source.unsplash.com/featured/?crispy-chicken"},
      {"name": "Lamb Chops", "price": 200, "image": "https://source.unsplash.com/featured/?lamb-chops"}
    ]
  },
  "veg-starters": {
    "name": "Veg Starters",
    "items": [
      {"name": "Paneer Tikka", "price": 100, "image": "https://source.unsplash.com/featured/?paneer-tikka"},
      {"name": "Veg Spring Roll", "price": 130, "image": "https://source.unsplash.com/featured/?spring-rolls"},
      {"name": "Stuffed Mushrooms", "price": 110, "image": "https://source.unsplash.com/featured/?stuffed-mushrooms"},
      {"name": "Hara Bhara Kebab", "price": 120, "image": "https://source.unsplash.com/featured/?hara-bhara-kebab"},
      {"name": "Crispy Corn", "price": 105, "image": "https://source.unsplash.com/featured/?crispy-corn"},
      {"name": "Aloo Tikki", "price": 85, "image": "https://source.unsplash.com/featured/?aloo-tikki"},
      {"name": "Veg Samosa", "price": 60, "image": "https://source.unsplash.com/featured/?veg-samosa"},
      {"name": "Paneer Pakora", "price": 120, "image": "https://source.unsplash.com/featured/?paneer-pakora"},
      {"name": "Corn Cheese Balls", "price": 110, "image": "https://source.unsplash.com/featured/?cheese-balls"},
      {"name": "Cheese Garlic Bread", "price": 100, "image": "https://source.unsplash.com/featured/?garlic-bread"}
    ]
  },
  "soups": {
    "name": "Soups",
    "items": [
      {"name": "Sweet Corn Soup", "price": 100, "image": "https://source.unsplash.com/featured/?sweet-corn-soup"},
      {"name": "Tomato Soup", "price": 125, "image": "https://source.unsplash.com/featured/?tomato-soup"},
      {"name": "Hot & Sour Soup", "price": 115, "image": "https://source.unsplash.com/featured/?hot-and-sour-soup"},
      {"name": "Chicken Soup", "price": 150, "image": "https://source.unsplash.com/featured/?chicken-soup"},
      {"name": "Manchow Soup", "price": 110, "image": "https://source.unsplash.com/featured/?manchow-soup"},
      {"name": "Veg Clear Soup", "price": 120, "image": "https://source.unsplash.com/featured/?veg-clear-soup"},
      {"name": "Mushroom Soup", "price": 120, "image": "https://source.unsplash.com/featured/?mushroom-soup"},
      {"name": "Lentil Soup", "price": 130, "image": "https://source.unsplash.com/featured/?lentil-soup"},
      {"name": "Minestrone Soup", "price": 100, "image": "https://source.unsplash.com/featured/?minestrone-soup"},
      {"name": "Broccoli Soup", "price": 140, "image": "https://source.unsplash.com/featured/?broccoli-soup"}
    ]
  },
  "fish-sea-food": {
    "name": "Fish & Sea Food",
    "items": [
      {"name": "Grilled Fish", "price": 180, "image": "https://source.unsplash.com/featured/?grilled-fish"},
      {"name": "Prawn Curry", "price": 200, "image": "https://source.unsplash.com/featured/?prawn-curry"},
      {"name": "Fish Tikka", "price": 175, "image": "https://source.unsplash.com/featured/?fish-tikka"},
      {"name": "Crab Masala", "price": 220, "image": "https://source.unsplash.com/featured/?crab-masala"},
      {"name": "Prawn Tempura", "price": 190, "image": "https://source.unsplash.com/featured/?tempura"},
      {"name": "Fish Fry", "price": 170, "image": "https://source.unsplash.com/featured/?fish-fry"},
      {"name": "Garlic Butter Prawns", "price": 210, "image": "https://source.unsplash.com/featured/?butter-prawns"},
      {"name": "Squid Rings", "price": 160, "image": "https://source.unsplash.com/featured/?squid-rings"},
      {"name": "Lobster Tails", "price": 250, "image": "https://source.unsplash.com/featured/?lobster"},
      {"name": "Seafood Platter", "price": 300, "image": "https://source.unsplash.com/featured/?seafood-platter"}
    ]
  },
  "main-course": {
    "name": "Main Course",
    "items": [
      {"name": "Paneer Butter Masala", "price": 140, "image": "https://source.unsplash.com/featured/?paneer-butter-masala"},
      {"name": "Butter Chicken", "price": 160, "image": "https://source.unsplash.com/featured/?butter-chicken"},
      {"name": "Veg Biryani", "price": 130, "image": "https://source.unsplash.com/featured/?veg-biryani"},
      {"name": "Chicken Biryani", "price": 150, "image": "https://source.unsplash.com/featured/?chicken-biryani"},
      {"name": "Dal Makhani", "price": 120, "image": "https://source.unsplash.com/featured/?dal-makhani"},
      {"name": "Mushroom Biryani", "price": 220, "image": "https://source.unsplash.com/featured/?mushroom-biryani"},
      {"name": "Panner Biryani", "price": 200, "image": "https://source.unsplash.com/featured/?paneer-biryani"},
      {"name": "Fish Curry", "price": 170, "image": "https://source.unsplash.com/featured/?fish-curry"},
      {"name": "Mutton Biryani", "price": 200, "image": "https://source.unsplash.com/featured/?mutton-biryani"},
      {"name": "Paneer Lababdar", "price": 150, "image": "https://source.unsplash.com/featured/?paneer-lababdar"}
    ]
  },
  "noodles": {
    "name": "Noodles",
    "items": [
      {"name": "Veg Hakka Noodles", "price": 100, "image": "https://source.unsplash.com/featured/?hakka-noodles"},
      {"name": "Chicken Noodles", "price": 100, "image": "https://source.unsplash.com/featured/?chicken-noodles"},
      {"name": "Schezwan Noodles", "price": 95, "image": "https://source.unsplash.com/featured/?schezwan-noodles"},
      {"name": "Egg Noodles", "price": 100, "image": "https://source.unsplash.com/featured/?egg-noodles"},
      {"name": "Mixed Noodles", "price": 110, "image": "https://source.unsplash.com/featured/?mixed-noodles"},
      {"name": "Singapore Noodles", "price": 120, "image": "https://source.unsplash.com/featured/?singapore-noodles"},
      {"name": "Schezuan Chicken Noodles", "price": 130, "image": "https://source.unsplash.com/featured/?schezwan-chicken-noodles"},
      {"name": "Garlic Noodles", "price": 110, "image": "https://source.unsplash.com/featured/?garlic-noodles"},
      {"name": "Seafood Noodles", "price": 140, "image": "https://source.unsplash.com/featured/?seafood-noodles"},
      {"name": "Chili Noodles", "price": 100, "image": "https://source.unsplash.com/featured/?chili-noodles"}
    ]
  },
  "salads": {
    "name": "Salads",
    "items": [
      {"name": "Caesar Salad", "price": 80, "image": "https://source.unsplash.com/featured/?caesar-salad"},
      {"name": "Greek Salad", "price": 90, "image": "https://source.unsplash.com/featured/?greek-salad"},
      {"name": "Sprout Salad", "price": 70, "image": "https://source.unsplash.com/featured/?sprout-salad"},
      {"name": "Cucumber Salad", "price": 65, "image": "https://source.unsplash.com/featured/?cucumber-salad"},
      {"name": "Fruit Salad", "price": 85, "image": "https://source.unsplash.com/featured/?fruit-salad"},
      {"name": "Pasta Salad", "price": 100, "image": "https://source.unsplash.com/featured/?pasta-salad"},
      {"name": "Quinoa Salad", "price": 110, "image": "https://source.unsplash.com/featured/?quinoa-salad"},
      {"name": "Greek Chickpea Salad", "price": 95, "image": "https://source.unsplash.com/featured/?chickpea-salad"},
      {"name": "Kale & Apple Salad", "price": 105, "image": "https://source.unsplash.com/featured/?kale-apple-salad"},
      {"name": "Caprese Salad", "price": 120, "image": "https://source.unsplash.com/featured/?caprese-salad"}
    ]
  },
  "desserts": {
    "name": "Desserts",
    "items": [
      {"name": "Chocolate Ice Cream", "price": 80, "image": "https://source.unsplash.com/featured/?chocolate-ice-cream"},
      {"name": "Vanilla Ice Cream", "price": 70, "image": "https://source.unsplash.com/featured/?vanilla-ice-cream"},
      {"name": "Pista Ice Cream", "price": 90, "image": "https://source.unsplash.com/featured/?pista-ice-cream"},
      {"name": "Strawberry Ice Cream", "price": 75, "image": "https://source.unsplash.com/featured/?strawberry-ice-cream"},
      {"name": "Mango Ice Cream", "price": 85, "image": "https://source.unsplash.com/featured/?mango-ice-cream"},
      {"name": "Gulab Jamun", "price": 60, "image": "https://source.unsplash.com/featured/?gulab-jamun"},
      {"name": "Rasmalai", "price": 70, "image": "https://source.unsplash.com/featured/?rasmalai"},
      {"name": "Brownie with Ice Cream", "price": 120, "image": "https://source.unsplash.com/featured/?brownie-ice-cream"},
      {"name": "Cheesecake", "price": 130, "image": "https://source.unsplash.com/featured/?cheesecake"},
      {"name": "Tiramisu", "price": 140, "image": "https://source.unsplash.com/featured/?tiramisu"}
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
<<<<<<< HEAD
    
=======
    
>>>>>>> abd2d67 (Saved changes before pull)
