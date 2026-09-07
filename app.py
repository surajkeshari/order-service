def calculate_total(price, quantity):
    return price * quantity


def create_order(product, price, quantity):
    if not product:
        raise ValueError("Product is required")

    if price <= 0:
        raise ValueError("Price must be greater than 0")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    total = calculate_total(price, quantity)

    return {
        "product": product,
        "quantity": quantity,
        "total": total
    }