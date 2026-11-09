

def show_title():
    print("-"*50)
    print("1. 상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
    print("-"*50)

 
# 번호 선택
def ask_num():
    user_input = input("선택 : ")
    return user_input
    
# 상품목록
def choice_1():
    for num, item in enumerate(item_list.show_items(), start = 1):
        if item.inventory > 0: 
            print(f"{num}. {item.name} {item.price} (재고 {item.inventory}개)")
        elif item.inventory == 0:
            print(f"{num}. {item.name} {item.price} (품절)")
            
        
 # 상품 담기?
               
def add_cart():
    input("상품 번호 : ")
    
    
    
         


class ItemList:
    def __init__(self):
        self.item = []
        
    def add_item(self, item):
        self.item.append(item)
        
    def remove_item(self, item):
        self.item.remove(item)
        
    def show_items(self):
        return self.item
    
class Item:
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory
        
# 장바구니 클래스        
class ShoppingCart:
    def __init__(self):
        self.cart = []
        
    def add_item(self, item, quantity):
        self.cart.append(item, quantity)
        
    def remove_item(self, item, quantity):
        self.cart.remove(item, quantity)
        
    def show_items(self):
        return self.cart


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


# 선택할 상품
class SelectItem(Item):
    def __init__(self, name, price, inventory, quantity):
        super().__init__(name, price, inventory)
        self.quantity = quantity

# 상품 담기?
               
def add_cart():
    add_cart_input = input("상품 번호 : ")
    return add_cart_input
        
        
        
def main():
    show_title()
    while True:
        user_input = ask_num()
        if user_input == "1":
            choice_1()
        elif user_input == "2":
            ask_item_num()
            
            
        elif user_input == "q":
            break
        
        
    
    
main()