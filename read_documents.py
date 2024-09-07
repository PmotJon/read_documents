# with open("check.txt", "r") as file:
# print(file.read())

# with open("document.txt", "w") as file:
# file.write("Sekarang text ini akan muncul")

# with open("document.txt", "r") as file:
# print(file.readline())
# print(file.readline())

# with open("document.txt", "r") as file:
# print(file.readlines())

# with open("text.py", "x") as file:
# file.write('print("hello world")')

with open("test.py", "a") as file:
    file.write("\ninput = input('nama kamu siapa: ')\n")
    file.write("print('halo ', inpur)")
