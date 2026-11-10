#영수증 제목
def show_title():
    print("-"*50)
    print("1. 상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
    print("-"*50)
# 번호 선택
def ask_num():
    user_input = input("선택 : ")
    return user_input


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
        
# 상품목록 정렬
def choice():
    for num, item in enumerate(item_list.show_items(), start = 1):
        if item.inventory > 0: 
            print(f"{num}. {item.name} {item.price} (재고 {item.inventory}개)")
        elif item.inventory == 0:
            print(f"{num}. {item.name} {item.price} (품절)")

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

# 장바구니 클래스        
class ShoppingCart:
    def __init__(self):
        self.cart = {}
        self.discount = Discount("쿠폰없음")
        
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
    
    # 쿠폰 등록
    def apply_discount(self, discount):
        self.discount = discount
        print(f"[{discount.name}] 쿠폰을 적용했습니다.")
        
        
    def show_items(self):
        return self.cart
    # 장바구니 총합?
    def display_cart(self):
        total = 0
        if not self.cart:
            print("장바구니에 내용물이 없습니다.")
            return
        print("-"*50)
        for item, quantity in self.cart.items():
            print(f"{item.name} x {quantity} {quantity*item.price}원")
            total += quantity * item.price
        print("-"*50)
        print(f"상품 합계 {total}원")
        discount_price = self.discount.discount_amount(total)
        print(f"할인 -{discount_price}원 [{self.discount.name}]")
        if total < 30000:
            delivery = 3000
        else:
            delivery = 0
        print(f"배송비 {delivery}원")
        print(f"결제 금액 {total - discount_price + delivery}원")
        print("-"*50)
        
    # 결제 후 재고
    def checkout(self):
        for item, quantity in self.cart.items():
            item.inventory -= quantity
            
        self.cart.clear()
        
        
            
 
# 상품 담기
               
def add_basket():
    basket_input = int(input("상품 번호 : "))
    item = item_list.show_items()[basket_input -1]
    quantity = int(input("수량 : "))
    shopping_cart.add_item(item, quantity)
    
# 장바구니 상품 빼기
def remove_basket():
    basket_input = int(input("상품 번호 : "))
    item = item_list.show_items()[basket_input - 1]
    quantity = int(input("뺄 수량 : "))
    shopping_cart.remove_item(item, quantity)




#쿠폰목록
class DiscountList:
    def __init__(self):
        self.discount = []
        
    def add_discount(self, discount):
        self.discount.append(discount)
    
    def show_discounts(self):
        return self.discount
    
# 쿠폰목록 정렬 및 선택    
def select_discount():
    for num, discount in enumerate(discount_list.show_discounts(), start=1):
        print(f"{num}. {discount.name}")
    #쿠폰 선택
    user_input = int(input("쿠폰 번호: "))
    selected_discount = discount_list.show_discounts()[user_input -1]
    return selected_discount


#쿠폰 클래스
class Discount:
    def __init__(self, name):
        self.name = name
        
    def discount_amount(self, total):
        return 0

        
# 10%할인 클래스 (오버라이딩)
class RateDiscount(Discount):
    def __init__(self, name):
        super().__init__(name)
        
    def discount_amount(self, total):
        rate = int(total * 0.1)
        if rate > 5000:
            return 5000
        else:
            return rate
# 3000원 할인 클래스 (오버라이딩)
class FixedDiscount(Discount):
    def __init__(self, name):
        super().__init__(name)
        
    def discount_amount(self, total):
        if total >= 20000:
            return 3000
        return 0

        
discount_list = DiscountList()

discount1 = Discount("쿠폰 없음")
discount2 = RateDiscount("10%할인(최대 5000원)")
discount3 = FixedDiscount("3000원 할인 (20,000원 이상 구매 시)")

discount_list.add_discount(discount1)
discount_list.add_discount(discount2)
discount_list.add_discount(discount3)

def completed():
    print("(영수증 출력)")
    print("결제가 완료되었습니다. 감사합니다!")







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
        elif user_input == "4":
            shopping_cart.display_cart()

        elif user_input == "5":
        # 장바구니에 쿠폰목록과 쿠폰선택창
            selected_discount = select_discount()
            shopping_cart.apply_discount(selected_discount)
        
        elif user_input == "6":
            shopping_cart.checkout()
            completed()
        

        elif user_input == "q":
            break
        
        
    
    
main()