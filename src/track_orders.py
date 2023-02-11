from collections import Counter


class TrackOrders:

    def __init__(self):
        self.orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        dishes = [
            order[1]
            for order in self.orders
            if order[0] == customer
        ]
        return Counter(dishes).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        dishes = set(order[1] for order in self.orders)
        orders = set(
            order[1]
            for order in self.orders
            if order[0] == customer
        )
        return dishes.difference(orders)

    def get_days_never_visited_per_customer(self, customer):
        days = set(order[2] for order in self.orders)
        days_customer = set(
            order[2]
            for order in self.orders
            if order[0] == customer
        )
        return days.difference(days_customer)

    def get_busiest_day(self):
        days = [order[2] for order in self.orders]
        return max(Counter(days), key=Counter(days).get)

    def get_least_busy_day(self):
        days = [order[2] for order in self.orders]
        return min(Counter(days), key=Counter(days).get)
