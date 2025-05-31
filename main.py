MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(rep):
    for k, v in resources.items():
        if rep == "report":
            print(f"{k}: {v}")

def check_resources(buyer_prompt):
    for k, v in resources.items():
        if buyer_prompt == "latte" or buyer_prompt == "cappuccino":
            if resources[k] < MENU[buyer_prompt]["ingredients"][k]:
                print(f"Sorry there's not enough {k}")
                return "insufficient"
        elif buyer_prompt == "espresso":
            if k == "milk":
                continue
            elif resources[k] < MENU[buyer_prompt]["ingredients"][k]:
                print(f"Sorry there's not enough {k}")
                return "insufficient"


def receive_money():
    money = {}
    sum_money = 0
    # print("Please insert coins.")
    quarters = (float(input("how many quarters?: "))) * 0.25
    dimes = (float(input("how many dimes?: "))) * 0.1
    nickels = (float(input("how many nickels?: "))) * 0.05
    pennies = (float(input("how many pennies?: "))) * 0.01
    denominations = ["quarters", "dimes", "nickels", "pennies"]
    cash_received = [quarters, dimes, nickels, pennies]
    for cash in range(4):
        money[denominations[cash]] = cash_received[cash]
        sum_money = sum_money + cash_received[cash]
        return sum_money

def sufficient_money(received_money, buyer_prompt):
    check_money = True
    while check_money:
        if received_money < MENU[buyer_prompt]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif received_money >= MENU[buyer_prompt]["cost"]:
            return True

def dispense_coffee(buyer_prompt):
    if buyer_prompt == "espresso":
        for k, v in resources.items():
            if k == "milk":
                continue
            else:
                remaining_resources = resources[k] - MENU["espresso"]["ingredients"][k]
                resources[k] = remaining_resources
    elif buyer_prompt == "latte" or buyer_prompt == "cappuccino":
        for k, v in resources.items():
            remaining_resources = resources[k] - MENU[buyer_prompt]["ingredients"][k]
            resources[k] = remaining_resources

def change_from_transaction(cost, receive):
    if receive < cost:
        return False
    elif receive == cost:
        return False
    elif receive > cost:
        return True

machine_ready = True
money_from_sales = 0

while machine_ready:
    buyer_inputs = input("What would you like?(espresso/latte/cappuccino): ").lower()
    if buyer_inputs == "off":
        break
    elif buyer_inputs == "report":
        print_report(buyer_inputs)
        print(f"Money ${money_from_sales}")
        continue
    else:
        resources_check = check_resources(buyer_inputs)
        if resources_check == "insufficient":
            continue
    print("Please insert coins.")
    cash_in = receive_money()
    if sufficient_money(cash_in, buyer_inputs):
        dispense_coffee(buyer_inputs)
        coffee_cost = MENU[buyer_inputs]["cost"]
        money_from_sales = money_from_sales + coffee_cost
        # print(f"Here is your {buyer_inputs}. Enjoy!")
        check_change = change_from_transaction(coffee_cost, cash_in)
        if check_change:
            print(f"Here is ${cash_in - MENU[buyer_inputs]["cost"]} in change.")
            print(f"Here is your {buyer_inputs}. Enjoy!")
            # print(f"money in safe ${money_from_sales}")

