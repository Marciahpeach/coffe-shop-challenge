from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("=== Coffee Shop Debug Demo ===")

    
    marciah = Customer("Marciah")
    mantel = Customer("Mantel")
    print(f"Created customers: {marciah.name}, {mantel.name}")

    
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    print(f"Created coffees: {latte.name}, {espresso.name}")

   
    order1 =  marciah.create_order(latte, 5.0)
    order2 =  marciah.create_order(espresso, 4.0)
    order3 = mantel.create_order(latte, 6.0)
    print(f"Order 1: {order1.customer.name} ordered {order1.coffee.name} for ${order1.price}")
    print(f"Order 2: {order2.customer.name} ordered {order2.coffee.name} for ${order2.price}")
    print(f"Order 3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price}")


    print(f"\nMarciah's orders: {len(marciah.orders())}")
    print(f"Marciah's coffees: {[coffee.name for coffee in marciah.coffees()]}")
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")
    print(f"Latte's order count: {latte.num_orders()}")


    print(f"\nLatte's average price: ${latte.average_price():.2f}")
    print(f"Espresso's order count: {espresso.num_orders()}")

  
    aficionado = Customer.most_aficionado(latte)
    print(f"\nMost aficionado for Latte: {aficionado.name if aficionado else 'None'}")

    
    americano = Coffee("Americano")
    aficionado = Customer.most_aficionado(americano)
    print(f"Most aficionado for Americano: {aficionado if aficionado else 'None'}")

if __name__ == "__main__":
    main()