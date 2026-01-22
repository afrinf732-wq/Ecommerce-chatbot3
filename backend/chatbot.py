def get_response(user_message):
    if not user_message:
        return "Please type something."

    message = user_message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! Welcome to our store. How can I help you?"

    if "products" in message:
        return "We have mobiles, laptops, and accessories."

    if "price" in message:
        return "Please tell me which product you want the price for."

    return "Sorry, I didn't understand that. Please try again."
