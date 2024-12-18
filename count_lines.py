import os

def count_lines_of_code(directory):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        lines = f.readlines()
                        total_lines += len(lines)
                        print(f"{file_path}: {len(lines)} lines")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
    print(f"\nTotal lines of Python code: {total_lines}")
    return total_lines

# Podaj ścieżkę do katalogu
directory = input("Podaj ścieżkę do katalogu: ")
count_lines_of_code(directory)
