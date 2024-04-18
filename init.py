class Drink:
    def __init__(self,name,size):
        self.name =name
        self.size =size

    def __str__(self):
        return f"{self.name} : {self.size}"

#create instance
hot_chocolate = Drink("Hot chocolate", "small")

print(hot_chocolate)