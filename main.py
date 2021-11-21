from sys import argv
from load_text import load_orders, load_dependencies
from helper_functions import generate_orders, generate_json_output_file

def main(orders_file_path, dependencies_file_path):

    # Load the work orders and dependencies onto memory
    work_orders = load_orders(orders_file_path)
    dependencies, dependent_work_order_ids = load_dependencies(dependencies_file_path)
    orders = generate_orders(work_orders, dependencies, dependent_work_order_ids)

    # Generate the output.json file with desired .json file name
    file_name = "output.json"
    generate_json_output_file(orders, file_name)

if __name__ == "__main__":
    if len(argv) < 4:
        print("Incorrect arguments provided")

    # Get file paths
    orders_file_path = argv[1]
    dependencies_file_path = argv[2]

    main(orders_file_path, dependencies_file_path)