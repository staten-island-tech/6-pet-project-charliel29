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



""" class Pet:
      def __init__(self,name,happiness,anger):
        self.name = name
        self.happiness = happiness
        self.anger = anger

      def play (self,fetch,happinessgain):
          self.fetch = fetch
          self.happiness += happinessgain
          print(f"after playing {fetch}, this is your pets happiness: {self.happiness}.")
Lebron = Pet("Lebron",50,10)
Lebron.play("fetch",10) """
          

class Hero:
    def __init__(self, name,money, inventory):
        self.name = name
        self.__money__ = money 
        self.inventory = inventory
    def buy(self, item, cost ):
        self.inventory.append(item)
        self.__money__ -= cost
        print(f"{self.__money__}") 
Jillian=Hero("Jillian",100,['Potion'])
Jillian.buy ("sword",50)
