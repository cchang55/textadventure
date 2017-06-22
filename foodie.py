start = '''
Hello, there! My name is Foodie! My purpose is to help
you decide where to go for lunch.
'''


print(start)


print("Choose your lifestyle: 'wealthy' or 'poor.'")
user_input = input()
if user_input == "wealthy":
    print("Would you like to eat at 'The Cheesecake Factory'(press a) or 'Black Angus Steakhouse'(press b)?")
    user_w = input()
    if user_w == "a":
        print("Bonjour! Welcome to The Cheesecake Factory! What would you like to order: 'Guacamole Salad'(press g) or 'The Everything Pizza'(press p)?")
        user_c = input()
        if user_c == "g":
            print("Nice choice! You have chosen to have that nice body you've always wanted!")
        elif user_c == "p":
            print("Shame on you! That is WAAAAAAAY too many carbs and calories than you need!")
    elif user_w == "b":
        print("Howdy! Welcome to Black Angus Steakhouse! May I serve you with the 'Ribeye Steak'(press s) or the 'Vegetable Cobb'(press v)?")
        user_b = input()
        if user_b == "s":
            print("You have found a parasite in your meat! Get to the nearest hospital ASAP!")
        elif user_b == "v":
            print("Yess! Healthy greens! You are on your way to being able to fit into that suit or dress! :)")
elif user_input == "poor":
    print("Would you like to eat at 'McDonalds' or 'In-N-Out'?")
    user_p = input()
    if user_p == "McDonalds" or user_p == "mcdonalds":
        print("Welcome to McDonalds! What would you like to order today: 'Big Mac' or 'Ceasar Salad'?")
        user_m = input()
        if user_m == "big mac" or user_p == "Big Mac":
            print("You have gained 5 pounds! Now your friends will notice your body change!")
        elif user_m == "ceasar salad" or user_m == "Ceasar Salad":
            print("Congratulations! You have chosen the healthy lifestyle! You are on your way to a happier body!")
    elif user_p == "In-N-Out" or user_p == "in n out" or user_p == "innout" or user_p == "in-n-out":
        print("Hello and welcome to In-N-Out! What kind of burger would you like: 'protein style' or 'cheese'?")
        user_i = input()
        if user_i == "protein style":
            print("YAAS! WORK THAT BOD!")
        elif user_i == "cheese":
            print("How was that greasy burger? Feel good?")
