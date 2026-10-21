import math
def print_bill(name,amount):
    print(f"{name:<8}{amount:,.2f}")
if __name__ == '__main__':
    print_bill('xo', 12345.678)