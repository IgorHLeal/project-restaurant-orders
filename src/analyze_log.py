import csv
from collections import Counter


def most_requested_dish(orders, customer):
    customer_orders = [order[1] for order in orders if order[0] == customer]
    return Counter(customer_orders).most_common()[0][0]


def customer_dish(orders, customer, dish):
    customer_orders = [
        order[1]
        for order in orders if order[0] == customer and order[1] == dish
    ]
    return len(customer_orders)


def never_ordered_dish(orders, customer):
    dishes = set(order[1] for order in orders)
    customer_dishes = set(order[1] for order in orders if order[0] == customer)
    return dishes - customer_dishes


def days_never_visited(orders, customer):
    days = set(order[2] for order in orders)
    customer_days = set(order[2] for order in orders if order[0] == customer)
    return days - customer_days


def read_file(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, mode="r", encoding="utf-8") as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def analyze_log(path_to_file):
    orders = read_file(path_to_file)

    maria_most_requested_dish = most_requested_dish(orders, "maria")
    arnaldo_count_dishes = customer_dish(orders, "arnaldo", "hamburguer")
    joao_never_ordered_dish = never_ordered_dish(orders, "joao")
    joao_days_never_visited = days_never_visited(orders, "joao")

    with open("data/mkt_campaign.txt", mode="w", encoding="utf-8") as file:
        file.write(
            f"{maria_most_requested_dish}\n"
            f"{arnaldo_count_dishes}\n"
            f"{joao_never_ordered_dish}\n"
            f"{joao_days_never_visited}\n"
        )
