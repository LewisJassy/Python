from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayCreditCard(Payment):
    def pay(self, amount):
        print(f"Pay ${amount} using credit card")

class PayPaypal(Payment):
    def pay(self, amount):
        print(f"Pay ${amount} using Paypal")

if __name__ == "__main__":
    credit = PayCreditCard()
    paypal = PayPaypal()

    credit.pay(100)
    paypal.pay(1000)
