import sys

USD_TO_EUR = 0.94  # Conversion rate from USD to EUR
EUR_TO_USD = 1.07  # Conversion rate from EUR to USD
INR_TO_USD = 0.012  # Conversion rate from INR to USD
USD_TO_INR = 83.46  # Conversion rate from USD to INR

print("Currency Converter")
print("1. Convert USD to EUR")
print("2. Convert EUR to USD")
print("3. Convert INR to USD")
print("4. Convert USD to INR")

choice = int(input("Enter your choice (1 or 2)and (3 or 4): "))

if choice == 1:
    amount = float(input("Enter amount in USD: "))
    converted_amount = amount * USD_TO_EUR
    print(f"{amount} USD is {converted_amount} EUR")
elif choice == 2:
    amount = float(input("Enter amount in EUR: "))
    converted_amount = amount * EUR_TO_USD
    print(f"{amount} EUR is {converted_amount} USD")
elif choice == 3:
    amount = float(input("Enter amount in INR: "))
    converted_amount = amount * INR_TO_USD
    print(f"{amount} INR is {converted_amount} USD")
elif choice == 4:
    amount = float(input("Enter amount in USD: "))
    converted_amount = amount * USD_TO_INR
    print(f"{amount} USD is {converted_amount} INR")
else:
    print("Invalid choice")

sys.exit(0)
