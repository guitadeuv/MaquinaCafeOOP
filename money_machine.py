class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "R$ 0,50": 0.50,
        "R$ 1,00": 1,
        "R$ 2,00": 2,
        "R$ 5,00": 5
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Dinheiro: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Por favor, insira as moedas.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"Quantas de: {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Aqui esta seu troco: {self.CURRENCY}{change}.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Desculpe, voce nao inseriu dinheiro suficiente")
            self.money_received = 0
            return False
