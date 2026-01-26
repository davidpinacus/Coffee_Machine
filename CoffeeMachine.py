
QUARTER=0.25
DIME=0.10
NICKLES=0.05
PENNIES=0.01

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
    "money": 0,

}
units={
    "water":"ml",
    "milk":"ml",
    "coffee":"g",
    "money":"",
}


def report():
    for key,value in resources.items():
        print(f"{key}: {value}{units[key]}")

def total_money(coins):
    q=coins["quarters"]*QUARTER
    d=coins["dimes"]*DIME
    n=coins["nickles"]*NICKLES
    p=coins["pennies"]*PENNIES

    amount=q+d+n+p
    return amount

def remaining_amount(paid,cost):
    change=paid-cost
    change=round(change,2)
    return change
def check_resources(drink_name):
    enough=True
    for item,required in MENU[drink_name]["ingredients"].items():
        if resources[item]<required:
            print(f"Sorry there is not enough {item}😔.")
            enough=False
    return enough
def subtract_resources(drink_name):
    for item,required in MENU[drink_name]["ingredients"].items():
        resources[item]-=required
def start():
    coffee=True
    while coffee:
        user_pick=input("What would you like? (espresso/latte/cappuccino)☕:").lower()
        if user_pick=="off":
            break
        elif user_pick=="report":
            report()
            continue
        if user_pick not in MENU:
            print("Invalid Input")
            continue
        if not check_resources(user_pick):
            continue
        print("Please insert coins.")
        coins = {
            "quarters": int(input("how many quarters?:")),
            "dimes": int(input("how many dimes?:")),
            "nickles": int(input("how many nickles?:")),
            "pennies": int(input("how many pennies?:"))

        }
        amount=total_money(coins)
        cost=MENU[user_pick]["cost"]
        if amount>=cost:
            subtract_resources(user_pick)
            resources["money"]+=cost
            change = remaining_amount(amount, cost)
            print(f"Here is ${change} in change.")
            print(f"Here is your {user_pick} ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money 😔. Money refunded 💵.")

start()
