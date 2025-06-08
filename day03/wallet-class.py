class Wallet:
    def __init__(self, brand, initial_amount=0):
        self.amount = initial_amount
        self.brand = brand

food_wallet = Wallet("SEIKO", 250)
transport_wallet = Wallet("SEIKO", 1000)

print("Food budget:", food_wallet.amount)
print("Transport budget:", transport_wallet.amount)
