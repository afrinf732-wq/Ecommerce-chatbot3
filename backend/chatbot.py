import json

# Load products data
with open("backend/products.json", "r") as file:
    products = json.load(file)

def get_response(user_message):
    if not user_message:
        return "Please type something."

    message = user_message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! Welcome to our store 😊"

    if "products" in message:
        product_names = [p["name"] for p in products]
        return "We have: " + ", ".join(product_names)

    if "price" in message:
        for product in products:
            if product["name"].lower() in message:
                return f"The price of {product['name']} is ₹{product['price']}"
        return "Please mention the product name."

    return "Sorry, I didn't understand. Try asking about products or prices."
