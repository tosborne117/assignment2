import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        order = input("What would you like? (small/medium/large/off/report):")
        if (order.lower() == "small"):
            if (sandwich_maker_instance.check_resources(recipes["small"]) == 0):
                money = cashier_instance.process_coins()
                if (cashier_instance.transaction_result(money, recipes["small"]["cost"])):
                    money -= recipes["small"]["cost"]
                    print("Here is your change: $" + str(money))
                    sandwich_maker_instance.make_sandwich("small", recipes)
                    print("Small sandwich is ready. Bon appetit!")
                else:
                    print("Sorry, that is not enough. Money refunded.")
            elif (sandwich_maker_instance.check_resources(recipes["small"]) == 1):
                print("Sorry, there is not enough ham for your order.")
            elif (sandwich_maker_instance.check_resources(recipes["small"]) == 2):
                print("Sorry, there is not enough cheese for your order.")
            elif (sandwich_maker_instance.check_resources(recipes["small"]) == 3):
                print("Sorry, there is not enough bread for your order.")
        elif (order == "medium"):
            if (sandwich_maker_instance.check_resources(recipes["medium"]) == 0):
                money = cashier_instance.process_coins()
                if (cashier_instance.transaction_result(money, recipes["medium"]["cost"])):
                    money -= recipes["medium"]["cost"]
                    print("Here is your change: $" + str(money))
                    sandwich_maker_instance.make_sandwich("medium", recipes)
                    print("Medim sandwich is ready. Bon appetit!")
                else:
                    print("Sorry, that is not enough. Money refunded.")
            elif (sandwich_maker_instance.check_resources(recipes["medium"]) == 1):
                print("Sorry, there is not enough ham for your order.")
            elif (sandwich_maker_instance.check_resources(recipes["medium"]) == 2):
                print("Sorry, there is not enough cheese for your order.")
            elif (sandwich_maker_instance.check_resources(recipes["medium"]) == 3):
                print("Sorry, there is not enough bread for your order.")
        elif (order == "large"):
            if (sandwich_maker_instance.check_resources(recipes["large"]) == 0):
                money = cashier_instance.process_coins()
                if (cashier_instance.transaction_result(money, recipes["large"]["cost"])):
                    money -= recipes["large"]["cost"]
                    print("Here is your change: $" + str(money))
                    sandwich_maker_instance.make_sandwich("large", recipes)
                    print("Large sandwich is ready. Bon appetit!")
                else:
                    print("Sorry, that is not enough. Money refunded.")
            elif (sandwich_maker_instance.check_resources(recipes["large"]) == 1):
                print("Sorry, there is not enough ham for your order.")
            elif (sandwich_maker_instance.check_resources(recipes["large"]) == 2):
                print("Sorry, there is not enough cheese for your order.")
            elif (sandwich_maker_instance.check_resources(recipes["large"]) == 3):
                print("Sorry, there is not enough bread for your order.")
        elif (order == "off"):
            break
        elif (order == "report"):
            print("Ham: " + str(sandwich_maker_instance.machine_resources["ham"]) + "\nCheese: " + str(
                sandwich_maker_instance.machine_resources["cheese"]) + "\nBread: " + str(sandwich_maker_instance.machine_resources["bread"]))
        else:
            print("Invalid input, please try again")
            continue

if __name__=="__main__":
    main()
