let cart = [];

let menuCategories = [
  {
    name: "Desserts",
    items: [
      { name: "Chocolate Ice Cream", price: 80, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/chocolate-ice-cream-img.png" },
      { name: "Vanilla Ice Cream", price: 70, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/vanilla-ice-cream-img.png" },
      { name: "Pista Ice Cream", price: 90, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/pista-ice-cream-img.png" },
      { name: "Strawberry Ice Cream", price: 75, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/strawberry-ice-cream-img.png" },
      { name: "Mango Ice Cream", price: 85, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/mango-ice-cream-img.png" }
    ]
  },
  {
    name: "Soups",
    items: [
      { name: "Sweet Corn Soup", price: 90, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/sweet-corn-soup-img.png" },
      { name: "Hot & Sour", price: 95, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/hot-sour-soup-img.png" },
      { name: "Tomato Soup", price: 80, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/tomato-soup-img.png" },
      { name: "Veg Clear Soup", price: 85, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/veg-clear-soup-img.png" },
      { name: "Chicken Soup", price: 100, image: "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-responsive-website/chicken-soup-img.png" }
    ]
  }
];

function showItems(index) {
  const container = document.getElementById("categoryItems");
  container.innerHTML = "";

  const items = menuCategories[index].items;

  items.forEach(item => {
    const col = document.createElement("div");
    col.className = "col-12 col-md-6 col-lg-4 mb-4";
    col.innerHTML = `
      <div class="card shadow-sm p-3">
        <img src="${item.image}" class="card-img-top" style="height:200px; object-fit:cover;">
        <div class="card-body">
          <h5 class="card-title">${item.name}</h5>
          <p>₹${item.price}</p>
          <button class="btn btn-sm btn-success" onclick="addToCartByData('${item.name}', ${item.price})">Add to Cart</button>
        </div>
      </div>
    `;
    container.appendChild(col);
  });
}

function showCategory(categoryName) {
  const index = menuCategories.findIndex(cat => cat.name === categoryName);
  if (index !== -1) {
    showItems(index);
    document.getElementById("categoryItems").scrollIntoView({ behavior: "smooth" });
  }
}

function addToCartByData(name, price) {
  const index = cart.findIndex(i => i.name === name);
  if (index !== -1) {
    cart[index].quantity++;
  } else {
    cart.push({ name: name, price: price, quantity: 1 });
  }
  updateCartUI();
}

function updateCartUI() {
  const ul = document.getElementById("cartItems");
  const totalSpan = document.getElementById("cartTotal");
  ul.innerHTML = "";
  let total = 0;

  cart.forEach((item, index) => {
    total += item.price * item.quantity;
    const li = document.createElement("li");
    li.innerHTML = `
      ${item.name} x ${item.quantity} = ₹${item.price * item.quantity}
      <button class="btn btn-sm btn-outline-success ml-2" onclick="changeQty(${index}, 1)">+</button>
      <button class="btn btn-sm btn-outline-warning ml-1" onclick="changeQty(${index}, -1)">-</button>
      <button class="btn btn-sm btn-outline-danger ml-1" onclick="removeItem(${index})">🗑️</button>
    `;
    ul.appendChild(li);
  });

  totalSpan.innerText = total;
}

function changeQty(index, delta) {
  cart[index].quantity += delta;
  if (cart[index].quantity <= 0) {
    cart.splice(index, 1);
  }
  updateCartUI();
}

function removeItem(index) {
  cart.splice(index, 1);
  updateCartUI();
}

function placeOrder() {
  const name = document.getElementById("custName").value;
  const address = document.getElementById("custAddr").value;

  if (!name || !address || cart.length === 0) {
    alert("Please fill all fields and add at least one item to the cart.");
    return;
  }

  fetch("/place_order", {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      customer_name: name,
      address: address,
      cart: cart.map(item => ({
        menu_item_id: 0,
        quantity: item.quantity
      }))
    })
  })
    .then(res => res.json())
    .then(data => {
      alert("Order placed! ID: " + data.order_id);
      cart = [];
      updateCartUI();
      $('#orderModal').modal('hide');
    });
}

window.onload = function () {
  showItems(0);
};
