
class ItemList:
    def __init__(self):
        self.cart = []
        
    def add_item(self, item):
        self.cart.append(item)
        
    def remove_item(self, item):
        self.cart.remove(item)
        
    def show_items(self):
        return self.cart
    
class Item:
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory
        


# 상품목록        
item_list = ItemList()        
item1 = Item("무선 이어폰", 89000, 3)
item2 = Item("텀블러", 15000, 10)
item3 = Item("보조배터리", 32000, 5)
item4 = Item("마우스패드", 9000, 0)
item5 = Item("USB 허브", 18000, 4)

item_list.add_item(item1)
item_list.add_item(item2)
item_list.add_item(item3)
item_list.add_item(item4)
item_list.add_item(item5)

for num, item in enumerate(item_list.show_items(), start = 1):
    if item.inventory > 0: 
        print(f"{num}. {item.name} {item.price} (재고 {item.inventory}개)")
    elif item.inventory == 0:
        print(f"{num}. {item.name} {item.price} (품절)")


# 원하는 상품의 수량을 장바구니에 담기
class AddItem(Item):
    def __init__(self, name, price, inventory, quantity):
        super().__init__(name, price, inventory)
        self.quantity = quantity