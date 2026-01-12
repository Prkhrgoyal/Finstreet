class PaperBroker:
    def __init__(self, capital):
        self.capital = capital
        self.trades = []

    def place_order(self, date, action, price, qty):
        self.trades.append({
            "date": date,
            "action": action,
            "price": price,
            "quantity": qty
        })
