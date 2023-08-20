try:
    with open("D:\\danial python\\danial.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
