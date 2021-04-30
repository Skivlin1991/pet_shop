# this will be getting the shop name 
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
# to find out how much cash the shop has
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]
# to + or - cash from the shop 
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
# to sell pets and remove them
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
# to show pets sold
def increase_pets_sold(pet_shop, num_pets_sold):
    pet_shop["admin"]["pets_sold"] += num_pets_sold
# to understand the stock count
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
# to see the breeds of the pet in store
def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)
    return found_pets
# to find pets my name(not breed)
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
# find pets to remove from stock once sold 
def remove_pet_by_name(pet_shop, name):
    pet_to_delete = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_to_delete)
# now im add new pets to the stock 
def add_pet_to_stock(pet_shop, name):
    pet_shop["pets"].append(pet_shop)
# now seeing if the customer has the cash to pay for a pet
def get_customer_cash(customer):
    return customer["cash"]
# now im removing the cash amount from the customer(if they have it)
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
# seeing how meany pets the customer has
def get_customer_pet_count(customer):
    return len(customer['pets'])
# adding the pet to the customer as pet
def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)
# now seeing of the customer can afford the pet they want 
def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet['price']
# now i'll be selling the pet to the customer
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(customer, pet["price"])
        increase_pets_sold(pet_shop, 1)    
    