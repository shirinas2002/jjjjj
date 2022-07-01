supermarket = {}
cart = {}

while True:
    print("Choose Options\n"
          "1. Add product\n"
          "2. View product\n"
          "3. Add to cart\n"
          "4. View cart\n"
          "5. Check out\n"
          "6. Exit")
    option = int(input())
    if option == 1:
        prod_name = input("enter the product name")
        prod_price = input("enter the product price")
        prod_stock = input("enter the stock left")
        supermarket[prod_name] = {prod_price: prod_stock}
    elif option == 2:
        print(supermarket)
    elif option == 3:
        p_name = input("product name")
        if p_name in supermarket :
            print("stock available, Added to cart")
            cart[p_name] = {prod_price: prod_stock}
            print(cart)
        else:
            print("product is not available")
    elif option == 4:
        print(cart)
        











