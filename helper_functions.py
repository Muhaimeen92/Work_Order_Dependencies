import json

def generate_orders(work_orders, dependencies, dependent_work_order_ids):
    orders_list = []

    '''This is a helper function that will be called recursively to generate a dictionary of dependent
    work orders'''
    def create_dependency_list(ids):
        dependency_list = []
        for id in ids:
            work_order = work_orders[id]
            dependency_list.append({
                "id": work_order.id,
                "name": work_order.name,
                "dependencies": create_dependency_list(dependencies[work_order.id])
            })
        return dependency_list

    for id, work_order in work_orders.items():
        if id not in dependent_work_order_ids:
            order = {
                "id": work_order.id,
                "name": work_order.name,
                "dependencies": create_dependency_list(dependencies[work_order.id])
            }

            orders_list.append(order)

    orders = {"orders": orders_list}

    return orders

def generate_json_output_file(orders, file_name):
    with open(file_name, "w") as file:
        json.dump(orders, file, indent=2)


