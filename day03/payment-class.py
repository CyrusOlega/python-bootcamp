class Payment:
    def __init__(self, amount):
        self.amount = amount

    def valid(self):
        return self.amount >= 0

class Coupon(Payment):
    def __init__(self, amount, expired):
        super().__init__(amount)
        self.expired = expired

    def valid(self):
        return super().valid() and not self.expired

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number


    def valid(self):
        return super().valid() and len(self.card_number) == 16 and self.card_number.isnumeric()

class OnlinePayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def valid(self):
        return super().valid() and self.email.endswith("gmail.com")

print("Payment class")
payment = Payment(100)
print(payment.valid())

payment = Payment(-100)
print(payment.valid())

print("Coupon class")
coupon = Coupon(100, False)
print(coupon.valid())

coupon = Coupon(-100, False)
print(coupon.valid())

coupon = Coupon(100, True)
print(coupon.valid())

print("CardPayment class")
card_payment = CardPayment(100, "0123456789012345")
print(card_payment.valid())

card_payment = CardPayment(-100, "0123456789012345")
print(card_payment.valid())

card_payment = CardPayment(100, "12345")
print(card_payment.valid())

print("OnlinePayment class")
online_payment = OnlinePayment(100, "myname@gmail.com")
print(online_payment.valid())

online_payment = OnlinePayment(-100, "myname@gmail.com")
print(online_payment.valid())

online_payment = OnlinePayment(100, "myname@yahoo.com")
print(online_payment.valid())