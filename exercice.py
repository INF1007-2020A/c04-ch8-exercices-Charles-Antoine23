#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici

def exercice1(file1, file2):
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        for index, line1 in enumerate(f1):
            line2 = f2.readline()

            if line1 != line2:
                print(f"Les fichiers sont differents! A la ligne {index + 1}, on a:")
                print(line1)
                print("Et on a:")
                print(line2)
                break

def exercice2(input_file, output_file):
    with open(input_file, encoding="utf-8") as in_file, open(output_file, 'w', encoding="utf-8") as out_file:
        for line in in_file:
            words = line.split()
            line_triple = "   ".join(words)
            out_file.write(line_triple)

def exercice3(file_path, result_file_path):
    with open(file_path, encoding="utf-8") as f:
        note_percent = f.readlines()

    with open(result_file_path, 'w', encoding="utf-8"):
        for note in note_percent:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] <= int(note) < value[1]:
                    f.write(note + " " + key)
                    break




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice3("./notes.txt", "./notes_letter.txt")
    pass
