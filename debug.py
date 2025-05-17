from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("=== Coffee Shop Debug Demo ===")

    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    print(f"Created customers: {alice.name}, {bob.name}")

    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    print(f"Created coffees: {latte.name}, {espresso.name}")

    # Create orders
    order1 = alice.create_order(latte, 5.0)
    order2 = alice.create_order(espresso, 4.0)
    order3 = bob.create_order(latte, 6.0)
    print(f"Order 1: {order1.customer.name} ordered {order1.coffee.name} for ${order1.price}")
    print(f"Order 2: {order2.customer.name} ordered {order2.coffee.name} for ${order2.price}")
    print(f"Order 3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price}")

    # Test relationship methods
    print(f"\nAlice's orders: {len(alice.orders())}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")
    print(f"Latte's order count: {latte.num_orders()}")

    # Test aggregate methods
    print(f"\nLatte's average price: ${latte.average_price():.2f}")
    print(f"Espresso's order count: {espresso.num_orders()}")

    # Test bonus: most_aficionado
    aficionado = Customer.most_aficionado(latte)
    print(f"\nMost aficionado for Latte: {aficionado.name if aficionado else 'None'}")

    # Test empty case for bonus
    americano = Coffee("Americano")
    aficionado = Customer.most_aficionado(americano)
    print(f"Most aficionado for Americano: {aficionado if aficionado else 'None'}")

if __name__ == "__main__":
    main()