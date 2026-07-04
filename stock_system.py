"""
Stock Buy/Sell System
A simple system to manage stock buying, selling, and portfolio tracking
"""

class Stock:
    def __init__(self, symbol, price, quantity=0):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
    
    def __repr__(self):
        return f"Stock({self.symbol}, Price: ${self.price}, Qty: {self.quantity})"


class Portfolio:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.stocks = {}
        self.transaction_history = []
    
    def buy_stock(self, symbol, price, quantity):
        """Buy stocks"""
        total_cost = price * quantity
        
        if total_cost > self.balance:
            print(f"❌ Insufficient balance! Required: ${total_cost}, Available: ${self.balance}")
            return False
        
        if symbol not in self.stocks:
            self.stocks[symbol] = Stock(symbol, price, quantity)
        else:
            # Update average price and quantity
            old_qty = self.stocks[symbol].quantity
            old_price = self.stocks[symbol].price
            
            new_qty = old_qty + quantity
            new_price = (old_price * old_qty + price * quantity) / new_qty
            
            self.stocks[symbol].quantity = new_qty
            self.stocks[symbol].price = new_price
        
        self.balance -= total_cost
        self.transaction_history.append({
            'type': 'BUY',
            'symbol': symbol,
            'price': price,
            'quantity': quantity,
            'total': total_cost
        })
        
        print(f"✅ Bought {quantity} shares of {symbol} @ ${price}")
        return True
    
    def sell_stock(self, symbol, price, quantity):
        """Sell stocks"""
        if symbol not in self.stocks:
            print(f"❌ You don't own {symbol}")
            return False
        
        if self.stocks[symbol].quantity < quantity:
            print(f"❌ Insufficient quantity! You have {self.stocks[symbol].quantity} shares")
            return False
        
        total_revenue = price * quantity
        profit_loss = (price - self.stocks[symbol].price) * quantity
        
        self.stocks[symbol].quantity -= quantity
        self.balance += total_revenue
        
        if self.stocks[symbol].quantity == 0:
            del self.stocks[symbol]
        
        self.transaction_history.append({
            'type': 'SELL',
            'symbol': symbol,
            'price': price,
            'quantity': quantity,
            'total': total_revenue,
            'profit_loss': profit_loss
        })
        
        print(f"✅ Sold {quantity} shares of {symbol} @ ${price} | Profit/Loss: ${profit_loss:.2f}")
        return True
    
    def view_portfolio(self):
        """Display current portfolio"""
        print("\n" + "="*60)
        print("📊 PORTFOLIO SUMMARY")
        print("="*60)
        
        if not self.stocks:
            print("No stocks in portfolio")
        else:
            total_value = 0
            for symbol, stock in self.stocks.items():
                current_value = stock.price * stock.quantity
                total_value += current_value
                print(f"{symbol:6} | Qty: {stock.quantity:4} | Avg Price: ${stock.price:7.2f} | Value: ${current_value:10.2f}")
        
        print("-"*60)
        print(f"💰 Cash Balance: ${self.balance:10.2f}")
        
        if self.stocks:
            total_stock_value = sum(stock.price * stock.quantity for stock in self.stocks.values())
            total_portfolio_value = self.balance + total_stock_value
            print(f"📈 Stock Value: ${total_stock_value:10.2f}")
            print(f"💼 Total Portfolio: ${total_portfolio_value:10.2f}")
        
        print("="*60 + "\n")
    
    def view_history(self):
        """Display transaction history"""
        print("\n" + "="*60)
        print("📋 TRANSACTION HISTORY")
        print("="*60)
        
        if not self.transaction_history:
            print("No transactions yet")
        else:
            for idx, trans in enumerate(self.transaction_history, 1):
                print(f"{idx}. {trans['type']:4} | {trans['symbol']:6} | Qty: {trans['quantity']:4} | "
                      f"Price: ${trans['price']:7.2f} | Total: ${trans['total']:10.2f}", end="")
                
                if 'profit_loss' in trans:
                    print(f" | P/L: ${trans['profit_loss']:8.2f}")
                else:
                    print()
        
        print("="*60 + "\n")


def main():
    """Main function to run the stock system"""
    portfolio = Portfolio(initial_balance=50000)
    
    while True:
        print("\n📈 STOCK TRADING SYSTEM")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. View History")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
            try:
                price = float(input("Enter price per share: $"))
                quantity = int(input("Enter quantity: "))
                portfolio.buy_stock(symbol, price, quantity)
            except ValueError:
                print("❌ Invalid input! Please enter valid numbers.")
        
        elif choice == '2':
            symbol = input("Enter stock symbol to sell: ").strip().upper()
            try:
                price = float(input("Enter selling price per share: $"))
                quantity = int(input("Enter quantity: "))
                portfolio.sell_stock(symbol, price, quantity)
            except ValueError:
                print("❌ Invalid input! Please enter valid numbers.")
        
        elif choice == '3':
            portfolio.view_portfolio()
        
        elif choice == '4':
            portfolio.view_history()
        
        elif choice == '5':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
