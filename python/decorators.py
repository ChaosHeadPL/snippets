# create dcorator to save wrapped data to file
# Should take two args:
# data, file_type
import json
import csv

test_data = [{"name": "john", "age": 25}, {"name": "bill", "age": 36}]


def example_decorator(func):
    def wrapper(data):
        a = func(data)
        print(f"Wrapper: {a}")
        return a

    return wrapper


@example_decorator
def example_function(data):
    print(f"Function: {data}")
    return data


# print(f"Global: {test_function(test_data)}")
# Returns:
# Function: [{'name': 'john', 'age': 25}, {'name': 'bill', 'age': 36}]
# Wrapper: [{'name': 'john', 'age': 25}, {'name': 'bill', 'age': 36}]
# Global: [{'name': 'john', 'age': 25}, {'name': 'bill', 'age': 36}]


def save_to_json(file_path):
    """Decorator for saving returned data to json file"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            func_output = func(*args, **kwargs)

            if isinstance(func_output, dict()):
                print(f"Saving data to file: {file_path}")
                with open(file_path, "w") as json_file:
                    json.dump(func_output, json_file, indent=4)
            else:
                print(
                    f"Returned data is not dict() type and cannot be "
                    "save to file: {file_path}"
                )

            return func_output

        return wrapper

    return decorator


def file_save(file_path, file_type, separator="|"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_output = func(*args, **kwargs)

            if file_type == "json":
                print(f"Saving data to file: {file_path} as {file_type}")
                with open(file_path, "w") as json_file:
                    json.dump(func_output, json_file, indent=4)

            elif file_type == "csv":
                print(f"Saving data to file: {file_path} as {file_type}")
                with open(file_path, "w") as csv_file_backup:
                    csv_writer = csv.DictWriter(
                        csv_file_backup, fieldnames=func_output[0], delimiter="|"
                    )

                    # save headers:
                    csv_writer.writeheader()

                    for line in func_output:
                        csv_writer.writerow(line)

            return func_output

        return wrapper

    return decorator


@file_save(file_path="test_file.csv", file_type="csv")
def test_function(data):
    return data


print(f"Global: {test_function(test_data)}")
