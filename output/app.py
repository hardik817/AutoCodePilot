
# app.py
import gradio as gr
from accounts import Account

# Initialize the account
account = Account("user1", 10000.00)  # Initial deposit of $10,000


def deposit(amount):
    amount = float(amount)
    if account.deposit(amount):
        return f"Deposit successful. New balance: ${account.balance:.2f}"
    else:
        return "Deposit failed. Please enter a valid amount."


def withdraw(amount):
    amount = float(amount)
    if account.withdraw(amount):
        return f"Withdrawal successful. New balance: ${account.balance:.2f}"
    else:
        return "Withdrawal failed. Insufficient funds or invalid amount."


def buy_shares(symbol, quantity):
    quantity = int(quantity)
    if account.buy_shares(symbol.upper(), quantity):
        return (
            f"Buy order successful. New balance: ${account.balance:.2f}",
            get_holdings(),
            get_profit_loss(),
        )
    else:
        return (
            "Buy order failed. Insufficient funds or invalid quantity.",
            get_holdings(),
            get_profit_loss(),
        )


def sell_shares(symbol, quantity):
    quantity = int(quantity)
    if account.sell_shares(symbol.upper(), quantity):
        return (
            f"Sell order successful. New balance: ${account.balance:.2f}",
            get_holdings(),
            get_profit_loss(),
        )
    else:
        return (
            "Sell order failed. Insufficient shares or invalid quantity.",
            get_holdings(),
            get_profit_loss(),
        )


def get_holdings():
    holdings = account.get_holdings()
    if holdings:
        holdings_str = "\n".join(
            [f"{symbol}: {quantity}" for symbol, quantity in holdings.items()]
        )
    else:
        holdings_str = "No holdings"
    return holdings_str


def get_profit_loss():
    profit_loss = account.get_profit_loss()
    return f"Profit/Loss: ${profit_loss:.2f}"


def get_transactions():
    transactions = account.get_transactions()
    if transactions:
        transactions_str = "\n".join(
            [
                f"{tx['type'].capitalize()}: {tx.get('amount', '') or tx.get('quantity', '')} {tx.get('symbol', '') or ''} @ {tx.get('price', '') or ''}"
                for tx in transactions
            ]
        )
    else:
        transactions_str = "No transactions"
    return transactions_str


with gr.Blocks() as demo:
    gr.Markdown("# Simple Account Management")

    with gr.Tab("Account Actions"):
        with gr.Row():
            with gr.Column():
                deposit_amount = gr.Textbox(label="Deposit Amount")
                deposit_button = gr.Button("Deposit")
                deposit_output = gr.Textbox(label="Deposit Status")
            with gr.Column():
                withdraw_amount = gr.Textbox(label="Withdraw Amount")
                withdraw_button = gr.Button("Withdraw")
                withdraw_output = gr.Textbox(label="Withdrawal Status")

        with gr.Row():
            with gr.Column():
                buy_symbol = gr.Textbox(label="Buy Symbol (e.g., AAPL)")
                buy_quantity = gr.Textbox(label="Buy Quantity")
                buy_button = gr.Button("Buy Shares")
                buy_output = gr.Textbox(label="Buy Status")
            with gr.Column():
                sell_symbol = gr.Textbox(label="Sell Symbol (e.g., AAPL)")
                sell_quantity = gr.Textbox(label="Sell Quantity")
                sell_button = gr.Button("Sell Shares")
                sell_output = gr.Textbox(label="Sell Status")

    with gr.Tab("Account Summary"):
        balance_output = gr.Textbox(label="Current Balance", value=f"${account.balance:.2f}")
        holdings_output = gr.Textbox(label="Holdings", value=get_holdings())
        profit_loss_output = gr.Textbox(label="Profit/Loss", value=get_profit_loss())
        transactions_output = gr.Textbox(label="Transactions", value=get_transactions())

    deposit_button.click(
        fn=deposit, inputs=deposit_amount, outputs=deposit_output
    ).then(
        lambda: f"${account.balance:.2f}", None, balance_output
    ).then(
        get_transactions, None, transactions_output
    )

    withdraw_button.click(
        fn=withdraw, inputs=withdraw_amount, outputs=withdraw_output
    ).then(
        lambda: f"${account.balance:.2f}", None, balance_output
    ).then(
        get_transactions, None, transactions_output
    )

    sell_button.click(
        fn=sell_shares,
        inputs=[sell_symbol, sell_quantity],
        outputs=[sell_output, holdings_output, profit_loss_output],
    ).then(
        lambda: f"${account.balance:.2f}", None, balance_output
    ).then(
        get_transactions, None, transactions_output
    )

    buy_button.click(
        fn=buy_shares,
        inputs=[buy_symbol, buy_quantity],
        outputs=[buy_output, holdings_output, profit_loss_output],
    ).then(
        lambda: f"${account.balance:.2f}", None, balance_output
    ).then(
        get_transactions, None, transactions_output
    )

demo.launch()
