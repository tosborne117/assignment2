
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        req_ham = ingredients["ingredients"]["ham"]
        req_cheese = ingredients["ingredients"]["cheese"]
        req_bread = ingredients["ingredients"]["bread"]

        sufficient = 0
        if (req_ham > self.machine_resources["ham"]):
            sufficient = 1
        elif (req_cheese > self.machine_resources["cheese"]):
            sufficient = 2
        elif (req_bread > self.machine_resources["bread"]):
            sufficient = 3
        return sufficient

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        self.machine_resources["ham"] -= order_ingredients[sandwich_size]["ingredients"]["ham"]
        self.machine_resources["cheese"] -= order_ingredients[sandwich_size]["ingredients"]["cheese"]
        self.machine_resources["bread"] -= order_ingredients[sandwich_size]["ingredients"]["bread"]