import sys

if __name__ == "__main__":
    fd = open(sys.argv[1], "r")
    source = fd.read()
    fd.close()
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    solutions = []
    offset = 0
    for offset in range(len(LETTERS)):
        solution = ""
        for letter in source:
            if letter in LETTERS:
                index = (LETTERS.index(letter) + offset) % len(LETTERS)
                solution += LETTERS[index]
            else:
                solution += letter
        solutions.append(solution)
    for i, solution in enumerate(solutions):
        print("{1}:\n{0}\n".format(solution, i))