def open_doc():
    file = open("lyrics.txt", "r")
    data = file.read()
    print(data)

    char = len(data)

    print("\nTotal number of letters are:\n", char)
    file.close()


open_doc()


def read_word():
    file = open("lyrics.txt", "r")
    data = file.read()
    count = 0
    word = data.split()

    for count in word:
        count += 1
    file.close()

    print(f"number oof words in lyrics.txt are {count}")


read_word


def count_lowword():
    file = open("lyrics.txt", "r")
    data = file.read()
    count = 0
    word = data.split()

    for j in data:
        if j.islower():
            count += 1
    file.close()

    print("\nNumber of lowercase words are ", count)


count_lowword()


def count_upperword():
    file = open("lyrics.txt", "r")
    data = file.read()
    count = 0
    word = data.split()

    for j in data:
        if j.upper():
            count += 1
    file.close()

    print("\nNumber of uppercase words are ", count)


count_upperword()


def find_s_lines(input):
    file = open("lyrics.txt", "r")
    data = file.read()
    count = 0
    for lines in data:
        if lines[0] == input:
            count += 1
    file.close()
    print(f"\nnumber of lines starting with '{input}' are: {count}")


user_input = str(input("enter the char: "))

find_s_lines(user_input)


def find_words(user_enter):
    file = open("lyrics.txt", "r")
    data = file.read()
    count = 0
    words = user_enter
    word = data.split()

    # looping for find lowercase words
    for w in word:
        if words.lower() in w.lower():
            count += 1
    file.close()

    print(f"{words} found {count} times in the file ")


user_input = str(input("Which word do you want to find?  "))
find_words(user_input)
