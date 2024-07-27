import requests

def convert_currency(currency,targeted_currency):
    
    apiUrl = f"https://v6.exchangerate-api.com/v6/d8b1c384b5d5dfa65df15bab/latest/{currency}"
    response = requests.get(apiUrl)
    
    data = response.json()
    
    if (response.status_code == 200):
        return data["conversion_rates"][targeted_currency]
    else:
        raise Exception(f"Error fetching exchange : {data['error-type']}") 

def main():
    amount = float(input("Enter the amount: "))
    currency = input("Enter Currency: ").upper()
    targeted_currency = input("Enter Tagret Currency: ").upper()
    
    try:
        rate = convert_currency(currency,targeted_currency)
        amount_after_conversion = amount * rate
        print(f"{amount} {currency} is equal to {amount_after_conversion: .2f} {targeted_currency}")
    except Exception as e:
        print(f"error:{e}")
        

main()