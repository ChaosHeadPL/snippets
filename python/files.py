# r     - read      - Default value. Opens a file for reading, error if the file does not exist
# w     - write     - Opens a file for writing, creates the file if it does not exist
# a     - append    - Opens a file for appending, creates the file if it does not exist
# x     - create    - Creates the specified file, returns an error if the file exist
# r+    - read + write
# t     - text
# b     - binary (combine with r/b)
import csv
import json
import zipfile

# open file:
with open("/path/to/file", "r") as file:
    print(f"Opening {file.name} in {file.mode} mode")
    for line in file:
        pass


# open file in chunks:
with open("/path/to/file", "r") as file:
    chunk_size = 100
    # read only chunk size:
    file_content = file.read(chunk_size)
    while len(file_content) > 0:
        # print file with separator ("*") between chunks:
        print(file_content, end="*")
        file_content = file.read(chunk_size)


# copy files:
with open("/path/to/file", "rb") as r_file:
    with open("/path/to/file_backup", "wb") as w_file:
        for line in r_file:
            w_file.write(line)


# copy images:
with open("file.png", "rb") as r_file:
    with open("file_backup.png", "wb") as w_file:
        chunk_size = 4096
        r_file_chunk = r_file.read(chunk_size)
        while len(r_file_chunk) > 0:
            w_file.write(r_file_chunk)
            r_file_chunk = r_file.read(chunk_size)



# reading csv
with open("file.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)


# copy csv:
with open("file.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("file_backup.csv", "w") as csv_file_backup:
        csv_writer = csv.writer(csv_file_backup, delimiter="|")

    for line in csv_reader:
        csv_writer.writerow(line)


with open("file.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    fieldnames = ["first_name", "last_name", "email"]

    with open("file_backup.csv", "w") as csv_file_backup:
        csv_writer = csv.DictWriter(
            csv_file_backup, fieldnames=fieldnames, delimiter="|"
        )

    # save headers:
    csv_writer.writeheader()

    for line in csv_reader:
        csv_writer.writerow(line)


# csv to list()
with open("file.csv", "r") as csv_file:
    data = []
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        data.append(line.split("|"))


# csv to dict()
with open("file.csv", "r") as csv_file:
    data = []
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        # line is OrderedDict type
        data.append(line)


# load json from file
with open("file.json", "r") as json_file:
    data = json.load(json_file)


# dump json to file
with open("file.json", "w") as json_file:
    json.dump(data, json_file, indent=2)


# create zip files
with zipfile.ZipFile("files.zip", "w", compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write("test.txt")
    my_zip.write("test.json")


# extract zip files
with zipfile.ZipFile("files.zip", "r") as my_zip:
    my_zip.extractall()
    # extract single file:
    my_zip.extract("test.txt")

