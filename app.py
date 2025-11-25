""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Jillian = Hero("Jillian" , 150, ["Potion"])
Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__)
 """

""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
 """

""" class Hero:
    def __init__(self, name, money, inventory,):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Thomas = Hero("Thomas", 250, ["backpack"])
Thomas.buy({"title": "gun", "atk": 45})
print(Thomas.__dict__) """


class Pet:
    def __init__(self,name):
        self.name = name
    def play(self,happiness):
        happiness = input("How much happiness does your pet have from 1-10?")
        if not happiness .isdigit():
            print("Your happiness must be a number.")
        happiness=int(happiness)
        if happiness <= 10 and happiness >= 1:
            input("What game would you like to play?")
        else: 
            print("number has to be 1-10")
        def __init__(self,fetch,catch,toys):
            self.fetch = fetch
            self.catch = catch
            self.toys = toys  
    def hunger(self,hunger):
        hunger = input("How hungry is your pet from 1-10?")
        if not hunger .isdigit():
            print("Your hunger must be a number")
        hunger=int(hunger)
        hunger <=10 or hunger >= 1
        print("You number must be 1-10")
Lebron=Pet("Lebronnnnn")

 
          


