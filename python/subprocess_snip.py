import subprocess


# get list of catalogs
p1 = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE, shell=True)
print(p1)
print(p1.returncode)


# list of catalogs to file
with open("file.txt", "w") as file:
    p1 = subprocess.run("ls", "-la", stdout=file)
