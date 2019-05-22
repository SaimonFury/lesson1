def format_price (price):
    price = abs(int(price))
    return(price)
    
print("Цена: ЧИСЛО руб.")

x = format_price(56.24)
print(f'Цена {x} руб.')