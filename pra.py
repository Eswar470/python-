class Flower:
    def __init__(self,name:str,petals:int,price:float):
        self.name=name
        self.petals=petals
        self.price=price
    def set_name(self,name1:str):
        self.name=name1
    def get_name(self):
        return self.name
    
    def set_petals(self,petals:int):
        self.petals=petals
    def get_petals(self):
        return self.petals
    
    def set_price(self,price:float):
        self.price=price
    def get_price(self):
        return self.price
flower=Flower("rose",6,12.25)
print(f"Name:{flower.get_name()}")
print(f"petals:{flower.get_petals()}")
print(f"price:{flower.get_price()}")

flower.set_name("Marigold")
flower.set_petals(7)
flower.set_price(12.50)
print(f"Name:{flower.get_name()}")
print(f"petals:{flower.get_petals()}")
print(f"price:{flower.get_price()}")
print("hell00")