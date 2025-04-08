from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app, resources={r"/initiate_payment": {"origins": "https://ideallogisticsinvestments.com"}})

PAYSTACK_SECRET_KEY = 'sk_live_8fb3d0da528499cb5f464b1e16edbbe119a439fc'

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
        'image': 'https://ideallogisticsinvestments.com/glass4.jpg',
        'description': 'A plastic seal strip typically refers to a flexible, strip-like material used to create an airtight or watertight seal between two surfaces. They are commonly made from materials such as plastic, rubber, or silicone and are often used in a variety of applications.'
    }
}

@app.route('/initiate_payment', methods=['POST'])
def initiate_payment():
    data = request.json
    item_id = data.get('item_id')
    email = data.get('email')
    quantity = data.get('quantity', 1)  # Default to 1 if quantity is not provided

    if item_id not in items:
        return jsonify({'error': 'Invalid item ID'}), 400

    item = items[item_id]
    total_amount = item['price'] * quantity  # Calculate total amount based on quantity
    amount = total_amount * 100  # Paystack expects amount in kobo (1 NGN = 100 kobo)

    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'amount': amount,
        'email': email,
        'currency': 'KES',
        'callback_url': 'https://ideallogisticsinvestments.com/callback'  # Replace with your callback URL
    }

    response = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        authorization_url = response_data['data']['authorization_url']
        return jsonify({'authorization_url': authorization_url})
    else:
        return jsonify({'error': 'Failed to initialize payment', 'status_code': response.status_code}), response.status_code

@app.route('/callback', methods=['GET'])
def callback():
    reference = request.args.get('reference')
    verify_url = f'https://api.paystack.co/transaction/verify/{reference}'
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json'
    }

    verify_response = requests.get(verify_url, headers=headers)

    if verify_response.status_code == 200:
        verify_data = verify_response.json()
        status = verify_data['data']['status']
        amount = verify_data['data']['amount'] / 100  # Convert kobo to NGN

        if status == 'success':
            return render_template_string('''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Payment Successful</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            margin: 0;
                            padding: 0;
                            background-color: #f4f4f4;
                            text-align: center;
                            padding: 50px;
                        }
                        h1 {
                            color: green;
                        }
                    </style>
                </head>
                <body>
                    <h1>Payment Successful!</h1>
                    <p>Thank you for your payment of KES {{ amount }}.</p>
                </body>
                </html>
            ''', amount=amount)
        else:
            return render_template_string('''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Payment Failed</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            margin: 0;
                            padding: 0;
                            background-color: #f4f4f4;
                            text-align: center;
                            padding: 50px;
                        }
                        h1 {
                            color: red;
                        }
                    </style>
                </head>
                <body>
                    <h1>Payment Failed</h1>
                    <p>Sorry, your payment could not be processed.</p>
                </body>
                </html>
            ''')
    else:
        return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Payment Verification Failed</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                        text-align: center;
                        padding: 50px;
                    }
                    h1 {
                        color: red;
                    }
                </style>
            </head>
            <body>
                <h1>Payment Verification Failed</h1>
                <p>Sorry, we could not verify your payment.</p>
            </body>
            </html>
        ''')

if __name__ == '__main__':
    app.run(debug=True)
