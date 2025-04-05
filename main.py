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
        'price': 112000,
        'image': 'https://ideallogisticsinvestments.com/glass1.jpg',
        'description': 'This high-quality double pane glass measures 3 feet by 5 feet, perfect for small to medium-sized windows. It provides excellent insulation and noise reduction, making it ideal for residential and commercial applications.'
    },
    'item2': {
        'name': 'Double pane glass-7ft x 10ft',
        'price': 350000,
        'image': 'https://ideallogisticsinvestments.com/glass2.jpg',
        'description': 'This large double pane glass measures 7 feet by 10 feet, suitable for spacious areas. It offers superior thermal insulation and soundproofing, making it a great choice for large windows and doors in both residential and commercial settings.'
    },
    'item3': {
        'name': 'Double pane glass-20ft x 10ft',
        'price': 700000,
        'image': 'https://ideallogisticsinvestments.com/glass3.jpg',
        'description': 'This extra-large double pane glass measures 20 feet by 10 feet, ideal for large-scale projects. It provides exceptional insulation and noise reduction, making it perfect for commercial buildings, large windows, and architectural projects.'
    },
    'item4': {
        'name': 'Plastic Seal Strip',
        'price': 210,
        'image': 'https://ideallogisticsinvestments.com/lass4.jpg',
        'description': 'A plastic seal strip typically refers to a flexible, strip-like material used to create an airtight or watertight seal between two surfaces. They are commonly made from materials such as plastic, rubber, or silicone and are often used in a variety of applications.'
    }
}

app = Flask(__name__)

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
