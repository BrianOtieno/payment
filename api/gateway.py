
class Gateway():
    def __init__(self, CreditCardNumber, CardHolder, 
    ExpirationDate, SecurityCode, Amount ):
        self.CreditCardNumber = CreditCardNumber
        self.CardHolder = CardHolder
        self.ExpirationDate = ExpirationDate
        self.SecurityCode =SecurityCode
        self.Amount = Amount

    @classmethod
    def redirectByAmount(cls, CreditCardNumber, CardHolder,ExpirationDate, SecurityCode, Amount):
        if int(cls.Amount) < 20:
            return None #To redirect to CheapPaymentGateway
        elif int(cls.Amount) >20 and int(Amount) < 501:
            return None # Redirect to ExpensivePaymentGateway 
        else:
            return None # To redirect to PremiumPaymentGateway 
        

class PremiumPaymentGateway(Gateway):
    pass 

class PremiumPaymentGateway(Gateway):
    pass 

class PremiumPaymentGateway(Gateway):
    pass 