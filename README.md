#  Coffee Machine (Python - CLI + OOP)

A Python-based coffee machine simulation built in two versions.

A command-line coffee machine simulation built using Object-Oriented Programming in Python.
Order your favorite drinks, insert coins, and enjoy a virtual coffee experience!

---

##  Features

*  Order drinks: **Espresso, Latte, Cappuccino**
*  Coin-based payment system
*  Resource management (water, milk, coffee)
*  Profit tracking
*  Report system for machine status
*  Handles insufficient resources & payment

---

##  Project Structure

```id="c9azx1"
.
├── Coffee_Machine_OOP_ Version.py
├── coffee_maker.py
├── menu.py
├── money_machine.py
├── coffee_logo.py
```

### Files Overview

* **Coffee_Machine_OOP_ Version.py** → Main program & user interaction 
* **coffee_maker.py** → Handles resources & coffee making 
* **menu.py** → Defines menu items and pricing 
* **money_machine.py** → Handles coin input & transactions 
* **coffee_logo.py** → Displays ASCII coffee logo 

---

##  How It Works

1. Displays menu with prices
2. User selects a drink
3. Machine checks:

   * Resource availability
   * Payment sufficiency
4. If valid:

   * Deducts resources
   * Returns change
   * Serves coffee 

---

##  Commands

| Command                             | Action                 |
| ----------------------------------- | ---------------------- |
| `latte` / `espresso` / `cappuccino` | Order drink            |
| `report`                            | View resources & money |
| `off`                               | Turn off machine       |


