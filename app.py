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
    def __init__(self,name,happiness,tiredness,hunger,cleansiness):
        self.name = name
        self.happiness = happiness
        self.tiredness = tiredness
        self.hunger = hunger
        self.cleansiness = cleansiness

    print("1) Play with your pet")
    print("2) Feed you pet")
    print("3) Clean your pet")
    print("4) Rest your pet")
    print("5) ignore your pet")
    y = input("What would you like to do?")

    if y == "1":
        print("1) Fetch")
        print("2) Catch")
        print("3) tug of war")
    x = input("What game would you like to play? 1,2,3")
    if x == "1":
        print("after playing fetch your pet gains 3 happiness")
    

    


 
          


