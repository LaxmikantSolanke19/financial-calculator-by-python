import math
import matplotlib.pyplot as plt

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Value must be greater than zero.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12
    emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
    return emi, months

def calculate_compound_interest(principal, annual_rate, times_compounded, years):
    amount = principal * (1 + annual_rate / (100 * times_compounded)) ** (times_compounded * years)
    return amount

def calculate_future_value(investment, rate, years):
    future_value = investment * ((1 + rate / 100) ** years)
    return future_value

def calculate_retirement_savings(monthly_saving, annual_rate, years):
    months = years * 12
    monthly_rate = annual_rate / (12 * 100)
    total = monthly_saving * ((1 + monthly_rate) ** months - 1) / monthly_rate
    return total

def format_currency(amount):
    return f"₹{amount:,.2f}"

def show_pie_chart(labels, sizes, title):
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()

def main():
    while True:
        print("\n--- Financial Calculator ---")
        print("1. Calculate Loan EMI")
        print("2. Calculate Compound Interest")
        print("3. Calculate Future Value of Investment")
        print("4. Estimate Retirement Savings")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            p = get_float("Enter loan amount: ")
            r = get_float("Enter annual interest rate (%): ")
            t = get_int("Enter loan term (in years): ")
            emi, months = calculate_emi(p, r, t)
            total_payment = emi * months
            interest_paid = total_payment - p
            print(f"Monthly EMI: {format_currency(emi)}")
            print(f"Total payment over {months} months: {format_currency(total_payment)}")
            print(f"Total interest paid: {format_currency(interest_paid)}")
            show_pie_chart(["Principal", "Interest"], [p, interest_paid], "Loan Breakdown")

        elif choice == '2':
            p = get_float("Enter principal amount: ")
            r = get_float("Enter annual interest rate (%): ")
            n = get_int("Enter number of times interest compounded per year: ")
            t = get_int("Enter time (in years): ")
            amount = calculate_compound_interest(p, r, n, t)
            interest_earned = amount - p
            print(f"Compound Interest Amount: {format_currency(amount)}")
            print(f"Interest Earned: {format_currency(interest_earned)}")
            show_pie_chart(["Principal", "Interest"], [p, interest_earned], "Compound Interest Breakdown")

        elif choice == '3':
            investment = get_float("Enter initial investment: ")
            rate = get_float("Enter annual interest rate (%): ")
            years = get_int("Enter number of years: ")
            future_value = calculate_future_value(investment, rate, years)
            gain = future_value - investment
            print(f"Future Value: {format_currency(future_value)}")
            print(f"Gain: {format_currency(gain)}")
            show_pie_chart(["Initial Investment", "Gain"], [investment, gain], "Investment Growth")

        elif choice == '4':
            monthly_saving = get_float("Enter monthly saving amount: ")
            annual_rate = get_float("Enter expected annual return rate (%): ")
            years = get_int("Enter number of years until retirement: ")
            savings = calculate_retirement_savings(monthly_saving, annual_rate, years)
            total_invested = monthly_saving * years * 12
            interest_earned = savings - total_invested
            print(f"Estimated Retirement Savings: {format_currency(savings)}")
            print(f"Total Contributions: {format_currency(total_invested)}")
            print(f"Interest Earned: {format_currency(interest_earned)}")
            show_pie_chart(["Contributions", "Interest"], [total_invested, interest_earned], "Retirement Savings Breakdown")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
