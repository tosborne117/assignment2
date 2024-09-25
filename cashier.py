class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollar = half_dollar = quarters = dimes = nickles = pennies = 0

        while True:
            print("Please insert your coins now. \n")
            inp = input("How many dollar coins?: ")
            if (inp.isdigit()):
                dollar += int(inp)
            else:
                print("Please enter a positive, whole number.")
            inp = input("How many half-dollar coins?: ")
            if (inp.isdigit()):
                half_dollar += int(inp)
            else:
                print("Please enter a positive, whole number.")
            inp = input("How many quarters?: ")
            if (inp.isdigit()):
                quarters += int(inp)
            else:
                print("Please enter a positive, whole number.")
            inp = input("How many dimes?: ")
            if (inp.isdigit()):
                dimes += int(inp)
            else:
                print("Please enter a positive, whole number.")
            inp = input("How many nickles?: ")
            if (inp.isdigit()):
                dollar += int(inp)
            else:
                print("Please enter a positive, whole number.")
            inp = input("How many pennies?: ")
            if (inp.isdigit()):
                pennies += int(inp)
            else:
                print("Please enter a positive, whole number.")
            inp = input("Do you have any more coins? y/n: ")
            if (inp.lower() == "y"):
                continue
            else:
                total = 1 * dollar + 0.5 * half_dollar + 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
                return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        tf = False
        if (coins > cost):
            tf = True
        return tf
