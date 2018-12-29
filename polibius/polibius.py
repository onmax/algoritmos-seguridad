import sys
from itertools import permutations
import math

from collections import OrderedDict


def get_a(tk, abc):
    tk_copy = list(tk)
    number_list = [[]] * (len(tk_copy))
    n = 0
    for letter in abc:
        while True:
            if letter in tk_copy:
                i = tk_copy.index(letter)
                number_list[i] = n
                n += 1
                tk_copy[i] = '-'
            else:
                break
    return number_list


if __name__ == "__main__":
    fd = open(sys.argv[1], "r")
    source = fd.read()
    fd.close()

    # Obteniendo la tabla tabular
    source = source.replace('\n', '')
    source = source.replace(' ', '')

    polybios_key = 'COLABORACIONES'
    tab_keys_copy = list('MC-G-QF--S')

    polybios_key = "".join(OrderedDict.fromkeys(polybios_key))
    polybios_key = list(polybios_key)
    # Letras posibles que faltan
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in LETTERS:
        if letter not in polybios_key:
            polybios_key += letter
    for x in range(1, 11):
        i = polybios_key.index(LETTERS[x - 1])
        x %= 10
        polybios_key.insert(i + 1, str(x))
    polybios_keys = ['A', 'D', 'F', 'G', 'V', 'X']
    matrix = {}
    i = 0
    for key_row in polybios_keys:
        matrix[key_row] = {}
        for key_col in polybios_keys:
            matrix[key_row][key_col] = polybios_key[i]
            i += 1
    # Combinacion sin repeticion
    LETTERS_no_tab_keys = ''
    for letter in LETTERS:
        if letter not in tab_keys_copy:
            LETTERS_no_tab_keys += letter
    combinations = permutations(LETTERS, tab_keys_copy.count('-'))
    results = []
    ranges = []
    ranges.append(1)
    for x in range(len(tab_keys_copy) - 1):
        ranges.append(ranges[-1] + int(len(source) / len(tab_keys_copy)))
    ranges.append(len(source) + 1)
    counter = 1
    for a in range(2, len(source) % len(tab_keys_copy) + 2):
        ranges[a] += counter
        counter += 1
    for c in combinations:
        tab_keys = []
        counter = 0
        for i, t in enumerate(tab_keys_copy):
            if t == '-':
                tab_keys.append(c[counter])
                counter += 1
            else:
                tab_keys.append(tab_keys_copy[i])
        indexes = get_a(tab_keys, LETTERS)
        second_stage = [[]] * len(indexes)
        for j in range(len(indexes)):
            i = indexes.index(j)
            second_stage[indexes.index(
                i)] = source[ranges[i] - 1: ranges[i + 1] - 1]
        kk = ''
        for x in range(len(second_stage[0])):
            for col in second_stage:
                if x < len(col):
                    kk += col[x]
        res = ''
        v_c = 0
        append_to_res = True
        for index in range(0, len(kk), 2):
            letter = matrix[kk[index]][kk[index + 1]]
            res += letter
            if letter not in ['A', 'E', 'I', 'O', 'U']:
                v_c += 1
            else:
                v_c = 0
            if v_c == 7:
                append_to_res = False
                break
        if append_to_res:
            results.append(res)
    with open('output.txt', 'w') as f:
        for item in results:
            f.write("%s\n" % item)
    print(len(results), len(source))
