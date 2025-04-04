from flask import Flask, request, render_template_string, redirect, jsonify
import requests
import json
from datetime import datetime

# Define your secret key directly in the code (not recommended for production)
PAYSTACK_SECRET_KEY = 'sk_live_8fb3d0da528499cb5f464b1e16edbbe119a439fc'

# Define the items and their prices with images
items = {
    'item1': {
        'name': 'Double pane glass-3ft x 5ft',
        'price': 4000,
        'image': 'https://ideallogisticsinvestments.com/glass1.jpg',
        'description': 'This high-quality double pane glass measures 3 feet by 5 feet, perfect for small to medium-sized windows. It provides excellent insulation and noise reduction, making it ideal for residential and commercial applications.'
    },
    'item2': {
        'name': 'Double pane glass-7ft x 10ft',
        'price': 7000,
        'image': 'https://ideallogisticsinvestments.com/glass2.jpg',
        'description': 'This large double pane glass measures 7 feet by 10 feet, suitable for spacious areas. It offers superior thermal insulation and soundproofing, making it a great choice for large windows and doors in both residential and commercial settings.'
    },
    'item3': {
        'name': 'Double pane glass-20ft x 10ft',
        'price': 9000,
        'image': 'https://ideallogisticsinvestments.com/glass3.jpg',
        'description': 'This extra-large double pane glass measures 20 feet by 10 feet, ideal for large-scale projects. It provides exceptional insulation and noise reduction, making it perfect for commercial buildings, large windows, and architectural projects.'
    }
}

app = Flask(__name__)

@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template_string('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Products</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }
                .header {
                    background-color: #000;
                    color: #fff;
                    padding: 10px 20px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .logo {
                    font-size: 1.5em;
                    font-weight: bold;
                }
                .nav-links {
                    list-style: none;
                    display: flex;
                }
                .nav-links li {
                    margin-left: 20px;
                }
                .nav-links a {
                    color: #fff;
                    text-decoration: none;
                }
                .container {
                    width: 90%;
                    margin: auto;
                    overflow: hidden;
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                    gap: 20px;
                    padding: 20px;
                }
                .product {
                    border: 1px solid #ddd;
                    padding: 15px;
                    background-color: #fff;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .product img {
                    width: 100%;
                    height: auto;
                    border-radius: 8px;
                    margin-bottom: 10px;
                }
                .product h2 {
                    margin: 0 0 5px;
                    font-size: 1.5em;
                }
                .product p {
                    margin: 0 0 15px;
                    font-size: 1em;
                }
                .product button {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 1em;
                    margin: 4px 2px;
                    cursor: pointer;
                    border-radius: 5px;
                }
                .footer {
                    background-color: #000;
                    color: #fff;
                    text-align: center;
                    padding: 10px 0;
                    position: fixed;
                    width: 100%;
                    bottom: 0;
                }
                @media (max-width: 600px) {
                    .header {
                        flex-direction: column;
                        align-items: flex-start;
                    }
                    .nav-links {
                        flex-direction: column;
                    }
                    .nav-links li {
                        margin-left: 0;
                        margin-top: 10px;
                    }
                    .container {
                        grid-template-columns: 1fr;
                    }
                    .product {
                        padding: 10px;
                    }
                    .product h2 {
                        font-size: 1.2em;
                    }
                    .product p {
                        font-size: 0.9em;
                    }
                    .product button {
                        padding: 8px 16px;
                        font-size: 0.9em;
                    }
                }
            </style>
        </head>
        <body>
            <div class="header">
                <img src="https://ideallogisticsinvestments.com/logo.png" alt="logo" loading="lazy">
                <div class="logo">Ideal Logistics</div>
                <ul class="nav-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="/contact">Contact</a></li>
                    <li><a href="/aboutus">About Us</a></li>
                    <li><a href="/products">Products</a></li>
                </ul>
            </div>
            <div class="container">
                <h1 style="text-align: center; margin: 20px 0;">Products</h1>
                {% for item_id, item in items.items() %}
                    <div class="product">
                        <img src="{{ item.image }}" alt="{{ item.name }}" loading="lazy">
                        <h2>{{ item.name }}</h2>
                        <p>{{ item.description }}</p>
                        <p>Price: KES {{ item.price }}</p>
                        <form action="/initiate_payment" method="post" style="display: inline;">
                            <input type="hidden" name="item_id" value="{{ item_id }}">
                            <input type="hidden" name="email" value="ideallogisticsinvestments@gmail.com">
                            <button type="submit">Buy Now</button>
                        </form>
                    </div>
                {% endfor %}
            </div>
            <div class="footer">
                <p>&copy; {{ current_year }} Kevin Nandi. Contact us at <a href="mailto:kevinnandi1631@gmail.com" style="color: #fff;">kevinnandi1631@gmail.com</a></p>
            </div>
        </body>
        </html>''', items=items, current_year=current_year)

@app.route('/initiate_payment', methods=['POST'])
def initiate_payment():
    item_id = request.form.get('item_id')
    email = request.form.get('email')

    if item_id not in items:
        return jsonify({'error': 'Invalid item ID'}), 400

    item = items[item_id]
    amount = item['price'] * 100  # Paystack expects amount in kobo (1 NGN = 100 kobo)

    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'amount': amount,
        'email': email,
        'currency': 'KES',
        'callback_url': 'https://yourdomain.com/callback'  # Replace with your callback URL
    }

    response = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        authorization_url = response_data['data']['authorization_url']
        return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Payment</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                    }
                    iframe {
                        width: 100%;
                        height: 100vh;
                        border: none;
                    }
                </style>
            </head>
            <body>
                <iframe src="{{ authorization_url }}"></iframe>
            </body>
            </html>
        ''', authorization_url=authorization_url)
    else:
        return jsonify({'error': 'Failed to initialize payment', 'status_code': response.status_code}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
