result = 0

# ZADANIE: używając sys.argv, zrobić tak, żeby nazwę pliku przyjmować jako parametr wywołania programu
# python3 sum.py test-input.txt
# python3 sum.py moj-fajny-plik.txt
# filename = sys.argv[1]

with open("test-input.txt") as file:
    # line = file.readline()
    # while line:
    for line in file:
        result += int(line)
        # line = file.readline()


print(result)
