print("Let's Go on a date!")
date_name = input("Who do you want to go out with? \n")
date_amount = input("How much do you want to spend? \n")
#Italian: 
#Seafood:
#Mexican:

print(f"We are going to a food hall where you can choose from a variety of food but remember your budget of ${date_amount}!")

#menu dictionary
menu = {
    "foodmenu":[
        {"entrees":[{"Shrimp Alfredo": 25}, {"Crab Legs": 40}, {"Lobster": 50}, {"Fried Shrimp": 10}, {"Quesadilla":8}, {"Enchiladas":15}]},
        {"drinks":[{"Wine": 15}, {"Rum Punch": 15}, {"Margarita":12}]},
        {"dessert":[{"Cheesecake": 10}, {"tres leches": 7}]}
    ]
}
#promting the user with choice for their entree 
print(menu["foodmenu"][0]["entrees"])
entreechoice = input("first pick an entree!")

print(menu["foodmenu"][1]["drinks"])
drinkchoice = input("now pick a drink")

print(menu["foodmenu"][2]["dessert"])
dessertchoice = input("now pick a dessert")

#the list where the order items will be stored 
order = [entreechoice, drinkchoice, dessertchoice]

#to calculate the total 

def ordertotal(order):
    total = 0.00
    for i in range(0, len(order)):
        total = total + order[i]
    return total
#how to see if the user went over or under budget 
if ordertotal > date_amount:
print("you went over budget! You can't afford another date :(")
else 
print("you stayed within budget! You can afford another date! :)")
