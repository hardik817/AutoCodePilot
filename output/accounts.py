
# accounts.py
from typing import Dict, List, Union


def get_share_price(symbol: str) -> float:
    """
    Retrieves the current share price for a given stock symbol.
    This is a placeholder function for demonstration purposes.
    In a real application, this would fetch the price from an external source.
    """
    if symbol == "AAPL":
        return 170.00
    elif symbol == "TSLA":
        return 800.00
    elif symbol == "GOOGL":
        return 2600.00
    else:
        return 0.00  # Or raise an exception for an unknown symbol


class Account:
    """
    Represents a user's trading account.
    """

    def __init__(self, account_id: str, initial_deposit: float):
        """
        Initializes a new account.

        Args:
            account_id (str): The unique identifier for the account.
            initial_deposit (float): The initial deposit amount.
        """
        self.account_id = account_id
        self.balance = initial_deposit
        self.transactions: List[Dict] = []
        self.holdings: Dict[str, int] = {}
        self.initial_deposit = initial_deposit

    def deposit(self, amount: float) -> bool:
        """
        Deposits funds into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            bool: True if the deposit was successful, False otherwise.
        """
        if amount <= 0:
            return False
        self.balance += amount
        self.transactions.append({
            "type": "deposit",
            "amount": amount,
            "timestamp": "TODO: Implement timestamp",
        })
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws funds from the account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        self.transactions.append({
            "type": "withdraw",
            "amount": amount,
            "timestamp": "TODO: Implement timestamp",
        })
        return True

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        """
        Buys shares of a stock.

        Args:
            symbol (str): The stock symbol (e.g., "AAPL").
            quantity (int): The number of shares to buy.

        Returns:
            bool: True if the purchase was successful, False otherwise.
        """
        if quantity <= 0:
            return False

        price = get_share_price(symbol)
        cost = price * quantity

        if cost > self.balance:
            return False

        self.balance -= cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        self.transactions.append({
            "type": "buy",
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "timestamp": "TODO: Implement timestamp",
        })
        return True

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        """
        Sells shares of a stock.

        Args:
            symbol (str): The stock symbol.
            quantity (int): The number of shares to sell.

        Returns:
            bool: True if the sale was successful, False otherwise.
        """
        if quantity <= 0:
            return False
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            return False

        price = get_share_price(symbol)
        revenue = price * quantity

        self.balance += revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]

        self.transactions.append({
            "type": "sell",
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "timestamp": "TODO: Implement timestamp",
        })
        return True

    def get_portfolio_value(self) -> float:
        """
        Calculates the total value of the portfolio.

        Returns:
            float: The total portfolio value.
        """
        total_value = 0.0
        for symbol, quantity in self.holdings.items():
            price = get_share_price(symbol)
            total_value += price * quantity
        return total_value

    def get_profit_loss(self) -> float:
        """
        Calculates the profit or loss from the initial deposit.

        Returns:
            float: The profit or loss.
        """
        return self.balance + self.get_portfolio_value() - self.initial_deposit

    def get_holdings(self) -> Dict[str, int]:
        """
        Returns the current share holdings.

        Returns:
            dict: A copy of the holdings dictionary.
        """
        return self.holdings.copy()

    def get_transactions(self) -> List[Dict]:
        """
        Returns a list of all transactions.

        Returns:
            list: A copy of the transactions list.
        """
        return self.transactions.copy()


if __name__ == '__main__':
    # Example Usage/Testing
    account = Account("test_account", 10000.00)

    print(f"Account ID: {account.account_id}")
    print(f"Initial Balance: ${account.balance:.2f}")

    # Deposit
    account.deposit(500.00)
    print(f"Balance after deposit: ${account.balance:.2f}")

    # Buy shares
    if account.buy_shares("AAPL", 10):
        print(f"Bought 10 AAPL shares. Balance: ${account.balance:.2f}")
    else:
        print("Could not buy AAPL shares.")

    # Sell shares
    if account.sell_shares("AAPL", 5):
        print(f"Sold 5 AAPL shares. Balance: ${account.balance:.2f}")
    else:
        print("Could not sell AAPL shares.")

    # Get portfolio value
    portfolio_value = account.get_portfolio_value()
    print(f"Portfolio Value: ${portfolio_value:.2f}")

    # Get profit/loss
    profit_loss = account.get_profit_loss()
    print(f"Profit/Loss: ${profit_loss:.2f}")

    # Get holdings
    print(f"Holdings: {account.get_holdings()}")

    # Get transactions
    print(f"Transactions: {account.get_transactions()}")

    # Test insufficient funds
    if account.buy_shares("TSLA", 100):  # This will likely fail
        print(f"Bought 100 TSLA shares. Balance: ${account.balance:.2f}")
    else:
        print("Could not buy TSLA shares (insufficient funds).")

    # Test selling shares that are not owned
    if account.sell_shares("GOOGL", 10):
        print(f"Sold 10 GOOGL shares. Balance: ${account.balance:.2f}")
    else:
        print("Could not sell GOOGL shares (not enough shares).")

    # Test withdrawing more than balance
    if account.withdraw(100000):
        print(f"Withdrew 100000. Balance: ${account.balance:.2f}")
    else:
        print("Could not withdraw (insufficient funds).")
