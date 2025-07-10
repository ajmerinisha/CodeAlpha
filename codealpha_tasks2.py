
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3400,
    "MSFT": 300
}


portfolio = {}

print("Enter your stock holdings.")
print("Type 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock] = quantity


total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

save = input("\nWould you like to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Your Portfolio:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print("Portfolio saved to 'portfolio_summary.txt'.")
