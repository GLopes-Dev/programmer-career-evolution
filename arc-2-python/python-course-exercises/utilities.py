def discount(price, percentage):
    return price - (price * percentage / 100)

def increase(value, percentage):
    return value + (value * percentage / 100)

def celsius_to_fahrenheit(c):
    return c * 1.8 + 32

def rent_price(k, d):
    return (d * 60) + (k * 0.15)