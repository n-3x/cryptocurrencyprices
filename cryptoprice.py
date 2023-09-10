import requests

crypto_symbols = ["bitcoin", "ethereum", "litecoin"]  

def get_crypto_prices(crypto_symbols):
    base_url = "https://api.coingecko.com/api/v3/simple/price"
    
    params = {
        "ids": ",".join(crypto_symbols),
        "vs_currencies": "usd"
    }
    
    try:
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            crypto_data = response.json()
            
            for symbol in crypto_symbols:
                if symbol in crypto_data:
                    price_usd = crypto_data[symbol]["usd"]
                    print(f"{symbol.upper()}: ${price_usd:.2f}")
                else:
                    print(f"{symbol.upper()}: Data not found")
        else:
            print(f"Error ")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    get_crypto_prices(crypto_symbols)
