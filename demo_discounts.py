# # Treat this particular data as Immuatable
# cart = [
#     {"name": "Laptop","price":25000},
#     {"name": "Mouse","price":300},
#     {"name": "Keyboard","price":250}
# ]


# def apply_discount(discount_rate: float):
#     print("Applying Discount....")
#     # The cart is outside the function
#     for item in cart:
#         item["price"] *= (1 - discount_rate)

# apply_discount(0.10)
# print(cart[0]["price"])


# Treat this particular data as Immuatable
cart = [
    {"name": "Laptop","price":25000},
    {"name": "Mouse","price":300},
    {"name": "Keyboard","price":250}
]


def apply_discount_pure(items: tuple, discount_rate: float) -> tuple:
    
    def calculate_new_price(item):
        new_price = item["price"] * (1-discount_rate)
        return {"name": item["name"],"price": round(new_price,2)}
    
    return tuple(map(calculate_new_price, items))


discounted_cart = apply_discount_pure(cart, 0.10)

print(cart[0]["price"])
print(discounted_cart[0]["price"])