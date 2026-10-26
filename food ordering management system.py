restaurant_list = ["Food Plaza", "Tasty Bites", "Spice Hub"]
food_list = ["Pizza", "Burger", "Pasta", "Fries"]
cart_list = []

print("Welcome to Food Ordering System")

print("1. View Restaurants")
print("2. View Food Menu")
print("3. Add Food to Cart")
print("4. View Cart")
print("5. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("Restaurants:")
    for restaurant in restaurant_list:
        print(restaurant)

elif choice == "2":
    print("Food Menu:")
    for food in food_list:
        print(food)

elif choice == "3":
    print("Food Menu:")
    for food in food_list:
        print(food)

    food_name = input("Enter food name: ")

    if food_name in food_list:
        cart_list.append(food_name)
        print(food_name, "added to cart")
    else:
        print("Food not available")

    print("Your cart:", cart_list)

elif choice == "4":
    print("Your cart:", cart_list)

elif choice == "5":
    print("Thank you!")

else:
    print("Invalid choice")
