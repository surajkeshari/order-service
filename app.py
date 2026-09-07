def calculate_total(price, quantity):
    return price * quantity


def create_order(product, price, quantity):
    total = calculate_total(price, quantity)

    return {
        "product": product,
        "quantity": quantity,
        "total": total
    }