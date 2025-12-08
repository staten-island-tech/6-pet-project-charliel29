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
        self.happiness = 5
        self.tiredness = 5
        self.hunger = 5
        self.cleansiness = 5

    def play(self):
        valid = True
        print("1) Fetch")
        print("2)Tug of war")
        print("3)catch")
        while valid == True:
            game = input("Choose what you want to do")
            if game == "1":
                self.happiness += 3
                valid = False
                print(f"{self.name} played fetch! Gained 3 Happiness")
            elif game == "2":
                self.happiness += 3
                valid = False
                print(f"{self.name} Played tug of war! Gained 3 Happiness")
            elif game == "3":
                self.happiness += 3
                valid = False
                print(f"{self.name} Played catch! Gained 3 Happines")
            else:
                print("You must choose a option 1,2,or 3")
        print (f"Happiness: {self.happiness}  Tiredness: {self.tiredness} Hunger: {self.hunger} Cleansiness: {self.cleansiness} ")
        
    def feed(self):
        valid = True
        print("1)Meat")
        print("2)Vegeatables")
        print("3)water")
        while valid == True:
            feed = input("What would you like to feed your pet")
            if feed == "1":
                self.hunger -=3
                valid = False
                if self.hunger<0:
                    self.hunger=0
                print(f"after eating meat{self.name} lost 3 hunger")
            elif feed == "2":
                self.hunger -=2
                valid = False
                if self.hunger<0:
                    self.hunger=0
                print(f"after eating vegatble {self.name} lost 2 hunger")
            elif feed == "3":
                self.hunger -=1
                valid = False
                if self.hunger<0:
                    self.hunger=0
                print(f"after drinking water {self.name} lost 1 hunger")
            else:
                print("You must choose a option 1,2, or 3")
        print (f"Happiness: {self.happiness}  Tiredness: {self.tiredness} Hunger: {self.hunger} Cleansiness: {self.cleansiness} ")

    def clean(self):
        valid = True
        print("1)Wash")
        print("2)Brush")
        while valid == True:
            clean = input("How would you like to clean your pet?")
            if clean == "1":
                self.cleansiness +=3
                valid = False
                if self.cleansiness<0:
                    self.cleansiness=0
                print(f"after washing {self.name} lost 3 cleansiness")
            elif clean == "2":
                self.cleansiness +=2
                valid = False
                if self.cleansiness<0:
                    self.cleansiness=0
                print(f"after brushing {self.name} lost 2 cleansiness")
            else:
                print("You must choose 1 or 2")
        print (f"Happiness: {self.happiness}  Tiredness: {self.tiredness} Hunger: {self.hunger} Cleansiness: {self.cleansiness} ")

    def rest(self):
        valid = True
        print("1)sleep")
        print("2)nap")
        while valid == True:
            rest = input("How would you like to rest your pet")
            if rest == "1":
                self.tiredness -=3
                valid = False
                if self.tiredness<0:
                    self.tiredness=0
                print(f"after sleeping {self.name} lost 3 tiredness")
            elif rest == "2":
                self.tiredness -=2
                valid = False
                if self.tiredness<0:
                    self.tiredness=0
                print(f"after napping {self.name} lost 2 happiness")
            else:
                print("You must choose 1 or 2")
        print (f"Happiness: {self.happiness}  Tiredness: {self.tiredness} Hunger: {self.hunger} Cleansiness: {self.cleansiness} ")


    def ignore(self):
        self.happiness -= 3
        self.tiredness += 3
        self.hunger += 3
        self.cleansiness -= 3
        print(f"after ignoring {self.name} he lost 3 happiness, gained 3 tiredness, gained 3 hunger, lost 3 cleansiness")
        print (f"Happiness: {self.happiness}  Tiredness: {self.tiredness} Hunger: {self.hunger} Cleansiness: {self.cleansiness} ")
            


name = input("What is your pet's name?")
my_pet = Pet(f"{name}")
def game(my_pet):
    play=True
    while play==True:
        print("1) Play with your pet")
        print("2) Feed you pet")
        print("3) Clean your pet")
        print("4) Rest your pet")
        print("5) ignore your pet")
        y = input("What would you like to do?")
        if y == "1":
            Pet.play(my_pet)
        elif y == "2":
            Pet.feed(my_pet)
        elif y == "3":
            Pet.clean(my_pet)
        elif y == "4":
            Pet.rest(my_pet)
        elif y == "5":
            Pet.ignore(my_pet)
        else:
            print("You have to choose 1,2,3,4, or 5.")
game(my_pet)




    
    






























    


 
          


