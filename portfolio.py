def manage_portfolio():
  
    market_prices = {
        "AAPL": 175.50,
        "TSLA": 240.25,
        "GOOG": 160.00,
        "MSFT": 415.75,
        "AMZN": 180.10
    }
    
    my_shares = {}
    
    print("=========================================")
    print("     Welcome to my Portfolio Tracker     ")
    print("=========================================")
    print("Recognized assets in system:", ", ".join(market_prices.keys()))
    print("Type 'done' anytime you want to finish adding shares.\n")

    while True:
        ticker = input("Enter stock ticker symbol (e.g., AAPL): ").upper().strip()
        
        if ticker == "DONE":
            break
            
        if ticker not in market_prices:
            print(" Ticker symbol not found. Try choosing from the list above.")
            continue
            
        try:
            qty = int(input(f"How many shares of {ticker} do you own? "))
            if qty < 0:
                print(" Shares cannot be a negative value.")
                continue
            my_shares[ticker] = my_shares.get(ticker, 0) + qty
        except ValueError:
            print(" Invalid entry. Make sure to type a whole number for shares.")
            
    print("\n=========================================")
    print("           PORTFOLIO VALUE REPORT        ")
    print("=========================================")
    
    if not my_shares:
        print("Your asset list is currently empty.")
        return
        
    grand_total = 0.0
    saved_lines = []
    
    for ticker, count in my_shares.items():
        unit_price = market_prices[ticker]
        position_value = count * unit_price
        grand_total += position_value
        
        line_detail = f"• {ticker}: {count} shares × ${unit_price:.2f} = ${position_value:.2f}"
        print(line_detail)
        saved_lines.append(line_detail)
        
    final_balance_str = f"Total Investment Portfolio Value: ${grand_total:.2f}"
    print("-" * 41)
    print(final_balance_str)
    
    try:
        with open("my_portfolio_summary.txt", "w") as file:
            file.write("=== MY PERSONAL INVESTMENT PORTFOLIO ===\n\n")
            for line in saved_lines:
                file.write(line + "\n")
            file.write("-" * 40 + "\n")
            file.write(final_balance_str + "\n")
        print("\n Success! Valuation report saved locally to 'my_portfolio_summary.txt'.")
    except IOError:
        print("\n Storage Alert: Could not export your text profile summary sheet.")

if __name__ == "__main__":
    manage_portfolio()
