from class_objects import Work_Order
import csv
from collections import defaultdict

def load_orders(file_path):
    work_orders = {}

    with open(file_path) as text_file:
        csv_reader = csv.reader(text_file, delimiter=",")
        first_line = True

        for row in csv_reader:
            if first_line:
                first_line = False
                continue

            id = int(row[0])
            name = row[1]
            work_order = Work_Order(id, name)

            work_orders[id] = work_order

    return work_orders

def load_dependencies(file_path):
    dependencies = defaultdict(list)
    dependent_work_order_ids = set()

    with open(file_path) as text_file:
        csv_reader = csv.reader(text_file, delimiter=",")
        first_line = True

        for row in csv_reader:
            if first_line:
                first_line = False
                continue

            id = int(row[0])
            child_id = int(row[1])

            dependent_work_order_ids.add(child_id)
            dependencies[id] += [child_id]

    return dependencies, dependent_work_order_ids
