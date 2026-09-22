# CodeAlpha Internship: Stock Portfolio Tracker (Task 2)

A simple console-based **financial investment tracker** written in Python. This script was engineered to fulfill the Task 2 project specifications during my programming internship at **CodeAlpha**.

## 📌 Project Architecture
The target of this tool is portfolio valuation math. The script runs an operational workspace loop that allows users to record stock ticker holdings, inputs custom share quantities, handles automated mathematical aggregation operations, and exports a text file record of the final portfolio.

### Key Highlights:
* **Predefined Pricing Model:** Leverages a hardcoded data dictionary matrix to determine asset evaluations safely without loading sluggish network APIs.
* **Persistent Position Compounding:** Intelligently combines holdings if a user enters the same ticker asset multiple times within a session.
* **Storage Export Integration:** Integrates native file writing parameters (`open()`) to save performance snapshots safely onto local hard disks.

## ⚙️ Core Concepts Used
* **Data Dictionaries:** Implements key-value collections to query item pricing tables instantly.
* **Try-Except Blocks:** Captures invalid user inputs (like letters inside numerical fields) to protect the console runtime loop from dropping out.
* **File I/O Streams:** Employs basic file handling tools to write structured logs out onto local disks.

## 🎮 What it looks like in action
Here is a live layout sample of the runtime environment:

```text
=========================================
     Welcome to my Portfolio Tracker     
=========================================
Recognized assets in system: AAPL, TSLA, GOOG, MSFT, AMZN
Type 'done' anytime you want to finish adding shares.

Enter stock ticker symbol (e.g., AAPL): AAPL
How many shares of AAPL do you own? 10
Enter stock ticker symbol (e.g., AAPL): TSLA
How many shares of TSLA do you own? 5
Enter stock ticker symbol (e.g., AAPL): done

=========================================
           PORTFOLIO VALUE REPORT        
=========================================
• AAPL: 10 shares × \$175.50 = \$1755.00
• TSLA: 5 shares × \$240.25 = \$1201.25
-----------------------------------------
Total Investment Portfolio Value: \$2956.25

💾 Success! Valuation report saved locally to 'my_portfolio_summary.txt'.
```
