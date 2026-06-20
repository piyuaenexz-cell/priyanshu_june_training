# *****************
# PART A — SPOT THE BUG (Explanation & Predicted Output)
# *****************
# expected output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']
#
# reson :
# The bug is that cart=[] only gets created once when the function is defined.Because it doesn't reset, the same list keeps getting reused every time.This makes different function calls mix up and stack data together.

# ******************

# PART B — FIX IT 

def add_item(item, cart=None):
    # if no cart is given, make a fresh empty list
    if cart is None:
        cart = []
    cart.append(item)
    return cart

# ********************


# PART C — BUILD THE CART

# FIXED: Function name changed back to create_cart
def create_cart(owner, discount=0):
    new_basket = {
        "owner": owner, 
        "items": [], 
        "discount": discount
    }
    return new_basket


def add_to_cart(cart, name, price, qty=1):
    product = {
        "name": name, 
        "price": price, 
        "qty": qty
    }
    cart["items"].append(product)


# FIXED: Function name and parameters changed back to update_price(price_tuple, new_price)
def update_price(price_tuple, new_price):
    # Tuples are immutable because they are designed to be constant data structures.Once created, their size and values are fixed in memory, which makes them faster than lists and completely safe from unexpected bugs or unwanted changes.
    price_tuple[0] = new_price


# FIXED: Function name changed back to calculate_total
def calculate_total(cart):
    bill_sum = 0.0
    
    for product in cart["items"]:
        item_cost = product["price"] * product["qty"]
        bill_sum = bill_sum + item_cost
        
    discount = bill_sum * (cart["discount"] / 100)
    bill = bill_sum - discount
    return bill



def main():
    print("--- 1. Creating Separate Carts ---")
    # FIXED: Calls create_cart now
    aman_cart = create_cart("Aman", discount=10)
    priya_cart = create_cart("Priya", discount=0)

    # adding items to aman's cart
    add_to_cart(aman_cart, "Notebook", 80, qty=2)
    add_to_cart(aman_cart, "Pen", 20, qty=5)

    # adding items to priya's cart
    add_to_cart(priya_cart, "School Bag", 500, qty=1)

    print("Aman's Items:", aman_cart["items"])
    print("Priya's Items:", priya_cart["items"])
    print()

    print("Checking Bill")
    # FIXED: Calls calculate_total now
    print("Aman Total (10% off): Rs.", calculate_total(aman_cart))
    print("Priya Total (0% off): Rs.", calculate_total(priya_cart))
    print()

    print("Testing Tuple")
    item_rates = [120, 250]
    item_rates = tuple(item_rates) # making sure it is a locked tuple
    # FIXED: Calls update_price now (This will raise a TypeError as requested)
    update_price(item_rates, 150)


# Running program
main()


#  *********************
# DISCUSSION POINTS (Answers written as comments at the bottom)
# **********************


# que 1. Why is discount=0 safe but cart=[] dangerous?
# Ans: discount=0 uses an integer, which is immutable (cannot be changed). Every time the function reads it, it just copies the value 0. However, cart=[] creates a mutable list object in memory once. Every call without a cart parameter keeps pointing back to that exact same list object, making multiple carts merge data.

# que2. What is the difference between rebinding and mutating?
# Ans: rebinding means changing where a variable name points (like setting x = 5 and then changing it to x = 10, or renaming a pointer block). mutating means altering the internal contents of an existing data container directly in place without changing its identity (like doing list.append() or changing a dictionary key value).

# que 3. Which of these are mutable? — list, tuple, dict, set, str, int
# Ans: list, dict, set are mutable and tuple, str, int are immutable

# que 4. When you pass a list into a function and modify it, do changes reflect outside? Why?
# Ans: yes the changes are fully visible outside the function. This is because python uses pass-by-object-reference behavior. The function does not receive a copy of the list; it receives a pointer to the original list object in memory. modifying it inside alters the actual parent item directly.
