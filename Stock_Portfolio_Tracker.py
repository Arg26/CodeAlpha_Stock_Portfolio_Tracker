import csv

# Hardcoded stock prices (can be refreshed)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "SMSG": 450,
    "DELL": 300,
    "AMZN": 400
}

# Function to get user portfolio
def get_user_portfolio():
    print("Available Stocks:", ", ".join(stock_prices.keys()))
    portfolio = {}
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Invalid stock symbol. Please try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity < 0:
                raise ValueError
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Please enter a valid positive integer for quantity.")
    return portfolio

# Function to calculate total investment and breakdown
def calculate_investment(portfolio):
    total = 0
    breakdown = {}
    for stock, qty in portfolio.items():
        investment = stock_prices[stock] * qty
        breakdown[stock] = {
            "Quantity": qty,
            "Price": stock_prices[stock],
            "Investment": investment
        }
        total += investment
    return total, breakdown

# Function to display results
def display_results(total, breakdown):
    print("\n--- Portfolio Summary ---")
    for stock, data in breakdown.items():
        print(f"{stock}: {data['Quantity']} x ${data['Price']} = ${data['Investment']}")
    print(f"Total Investment: ${total}")

# Optional: Save results to CSV
def save_to_csv(breakdown, total, filename="portfolio_summary.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Investment"])
        for stock, data in breakdown.items():
            writer.writerow([stock, data["Quantity"], data["Price"], data["Investment"]])
        writer.writerow([])
        writer.writerow(["Total", "", "", total])
    print(f"\nResults saved to {filename}")

# Main Program
if __name__ == "__main__":
    portfolio = get_user_portfolio()
    if portfolio:
        total, breakdown = calculate_investment(portfolio)
        display_results(total, breakdown)

        save_option = input("Do you want to save the result to a CSV file? (yes/no): ").lower()
        if save_option in ['yes', 'y']:
            save_to_csv(breakdown, total)
    else:
        print("No stocks entered. Exiting.")
