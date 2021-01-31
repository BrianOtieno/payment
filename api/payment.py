from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from .gateway import Gateway


app = Flask(__name__)
api = Api(app)

class PaymentRoot(Resource):
  def get(self):
    return jsonify({"message": "Welcome to payment"})

class ProcessPayment(Resource):
    def post(self):
        CreditCardNumber = request.json['CreditCardNumber']
        CardHolder = request.json['CardHolder']
        ExpirationDate = request.json['ExpirationDate']
        SecurityCode = request.json['SecurityCode']
        Amount = request.json['Amount']  

        #To Validate Input
        # return (request.json)

        Gateway(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount)

api.add_resource(ProcessPayment, '/ProcessPayment')
api.add_resource(PaymentRoot, '/')

def configure_routes(api):
  return api

