#
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
# print(food)
# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }
# if food in bakery_stock:
#     print(str(bakery_stock.get(food)) + " left")
# else:
#     print("We don't make that")

# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"]
# initial_game_state = {}.fromkeys(game_properties, 0)
# print(initial_game_state)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
stock_list = inventory.copy()
print(stock_list)
stock_list["cookie"] = 18
print(stock_list)
stock_list.pop("cake")
print(stock_list)
