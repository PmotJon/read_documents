import csv

# read all lines
# with open("IPL_2018.csv") as file:
#     data = file.readlines()

# print(data)

# # read and print each row
# with open("IPL_2018.csv") as file:
#     data = csv.reader(file)

#     for row in data:
#         print(row)

# with open("IPL_2018.csv") as file:
#     data = csv.reader(file, delimiter=" | ")

#     for row in data:
#         print(row)

# print("\n-- with a specified delimeter")
# with open("IPL_2018.csv") as file:
#     data = csv.reader(file)

#     data_list = list(data)

# print("-- Print the csv file & store them in a list --\n", data_list)

# print the total runs scored by each player then calculate the sum
# match_runs = []

# for row in data_list[1:]:
#     print("total runs scored by", row[0], "in IPL_2018 are", row[6])

#     match_runs.append(int(row[4]))

# print("-" * 48)
# print("total run scored by all the players in matches are", sum(match_runs))

# sixers = []
# for row in data_list[1:]:
#     sixers.append(int(row[12]))

# print("-" * 48)
# print("Sum of sixers", sum(sixers))

# read the number of wickets from each row
wickets = []

# for colomn in data_list[1:]:
#     wickets.append(int(colomn[17]))

# print(wickets)

# print("-" * 48)
# print("sum of wickets", sum(wickets))

# write data to a new CSV file
with open("new_csv.csv", "w") as file:
    csv_writer = csv.writer(file)
    header = ("Name", "class", "city")
    data = (
        ("Jonathan", "12", "Jakarta"),
        ("Aaron", "10", "Surabaya"),
        ("Maria", "12", "Jakut"),
    )

    csv_writer.writerow(header)
    for row in data:
        csv_writer.writerow(row)

# read the new csv file
with open("new_csv.csv", "r") as file:
    data = file.readlines()

# membaca biasa
print(data)

with open("new_csv.csv", "r") as file:
    data = csv.reader(file)

    for row in data:
        print(row)
