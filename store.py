def calculate_bill(price, quantity):
    """Calculate the total bill amount."""
    if price < 0 or quantity <= 0:
        raise ValueError("Price and quantity must be valid")
    return price * quantity


def check_stock(available_stock, required_quantity):
    """Check whether sufficient stock is available."""
    if required_quantity <= 0:
        return False
    return required_quantity <= available_stock


def update_stock(available_stock, sold_quantity):
    """Reduce stock after a successful sale."""
    if not check_stock(available_stock, sold_quantity):
        raise ValueError("Insufficient stock")
    return available_stock - sold_quantity


if __name__ == "__main__":
    product_name = "Biscuits"
    price = 30
    available_stock = 10
    purchased_quantity = 2

    if check_stock(available_stock, purchased_quantity):
        bill_amount = calculate_bill(price, purchased_quantity)
        remaining_stock = update_stock(
            available_stock,
            purchased_quantity
        )

        print("SMART STORE MANAGEMENT SYSTEM")
        print("Product:", product_name)
        print("Purchased quantity:", purchased_quantity)
        print("Total bill: Rs.", bill_amount)
        print("Remaining stock:", remaining_stock)
    else:
        print("Purchase unsuccessful: Insufficient stock")
