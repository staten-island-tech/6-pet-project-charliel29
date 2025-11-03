class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Charlie = Hero("Charlie", 100 , ["Ball"])
Charlie.buy({"title": "Sword", "atk" :34})