#영수증 제목
def show_title():
    print("-"*50)
    print("1. 상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
    print("-"*50)
# 상품목록 클래스
class ItemList:
    def __init__(self):
        self.item = []
        
    def add_item(self, item):
        self.item.append(item)
        
    def remove_item(self, item):
        self.item.remove(item)
        
    def show_items(self):
        return self.item

#상품   
class Item:
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory
        
# 상품목록
def choice():
    for num, item in enumerate(item_list.show_items(), start = 1):
        if item.inventory > 0: 
            print(f"{num}. {item.name} {item.price} (재고 {item.inventory}개)")
        elif item.inventory == 0:
            print(f"{num}. {item.name} {item.price} (품절)")


# 장바구니 클래스        
class ShoppingCart:
    def __init__(self):
        self.cart = {}
    # 장바구니에서 상품담기    
    def add_item(self, item, quantity):
        if quantity > item.inventory:
            print("재고가 부족합니다.")
            return

        if item in self.cart:
            if self.cart[item] + quantity > item.inventory:
                print("재고가 부족합니다.")
                return
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity

        print(f"{item.name} {quantity}개를 장바구니에 담았습니다.")
    #장바구니에서 상품 빼기    
    def remove_item(self, item, quantity):
        if item not in self.cart:
            print("장바구니에 없는 상품입니다.")
            return

        if quantity >= self.cart[item]:
            del self.cart[item]
            print(f"{item.name}을(를) 장바구니에서 삭제했습니다.")
        else:
            self.cart[item] -= quantity
            print(f"{item.name} {quantity}개를 장바구니에서 뺐습니다.")
        
        
        
        
        
    def show_items(self):
        return self.cart
 
# 상품 담기
               
def add_basket():
    basket_input = int(input("상품 번호 : "))
    item = item_list.show_items()[basket_input -1]
    quantity = int(input("수량 : "))
    shopping_cart.add_item(item, quantity)
    
# 상품 빼기
# 장바구니 상품 빼기
def remove_basket():
    basket_input = int(input("상품 번호 : "))
    item = item_list.show_items()[basket_input - 1]
    quantity = int(input("뺄 수량 : "))
    shopping_cart.remove_item(item, quantity)
    
    

# 번호 선택
def ask_num():
    user_input = input("선택 : ")
    return user_input

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

#장바구니
shopping_cart = ShoppingCart()

        
        
        
def main():
    show_title()
    while True:
        user_input = ask_num()
        if user_input == "1":
            choice()
        elif user_input == "2":
            add_basket()
        elif user_input == "3":
            remove_basket()
        # elif user_input == "4":

        # elif user_input == "5":

        elif user_input == "q":
            break
        
        
    
    
main()