from flask import Flask
import json

from api.payment import configure_routes
 

def test_valid_credit_card_number():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/ProcessPayment'

    mock_request_headers = {}

    mock_request_data = {
        "CreditCardNumber": "5173352003043300", 
        "CardHolder": "Brian G. O Otieno",
        "ExpirationDate": "2021-01-29", 
        "SecurityCode": "224",
        "Amount": "50"
    }

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 200

def test_valid_credit_card_holder():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/ProcessPayment'

    mock_request_headers = {}

    mock_request_data = {
        "CreditCardNumber": "5173352003043300", 
        "CardHolder": "Brian Otieno",
        "ExpirationDate": "2021-01-29", 
        "SecurityCode": "224",
        "Amount": "50"
    }

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 200

def test_valid_expiry_date():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/ProcessPayment'

    mock_request_headers = {}

    mock_request_data = {
        "CreditCardNumber": "5173352003043300", 
        "CardHolder": "Brian Otieno",
        "ExpirationDate": "2015-01-29", 
        "SecurityCode": "224",
        "Amount": "50"
    }

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 400

def test_valid_amount():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/ProcessPayment'

    mock_request_headers = {}

    mock_request_data = {
        "CreditCardNumber": "5173352003043300", 
        "CardHolder": "Brian Otieno",
        "ExpirationDate": "2021-01-29", 
        "SecurityCode": "224",
        "Amount": "-50"
    }

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 400

def test_payment_redirection():
    pass