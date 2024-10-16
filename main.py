import os
import random

class cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        print("*===============*")
        print("* 1 - Niemiecki *")
        print("*===============*")
        try:
            choose = int(input("Wybierz zestaw: "))
            cls()
            print("*==== Jaki tryb? =====*")
            print("* 1 - Nieskonczonosci *")
            print("* 2 -    Do 10       *")
            print("*=====================*")
            mode = int(input("Wybierz tryb: "))
            cls()
            flashcards(choose, mode)
        except ValueError:
            print("Musisz podac cyfre, nie litere")

def flashcards(choose, mode):
    try:
        with open(f"Sets/{str(choose)}", "r") as file:
            lines = file.readlines()
            ##############zrobic tryby################
            if mode==1:
                infinite_mode(lines)
            elif mode==2:
                ten_mode(lines)



    except FileNotFoundError:
        print(f"Plik o numerze {choose} nie został znaleziony")
    except IOError as e:
        print(f"Błąd przy odczycie pliku: {e}")

def infinite_mode(lines):
    while True:
        word1, word2 = lines[random.randint(0, len(lines) - 1)].strip().lower().split(" - ")
        answer = input(f"* {word1} - ").lower()
        print("-=======================-")
        if answer == word2:
            "Poprawna odpowiedz\n"
        elif answer == "0":
            break
        else:
            print(f"Bledna odpowiedz, poprawna: {word2}\n")

def ten_mode(lines):
    blacklist = []
    correct_answers = 0
    for _ in range(10):
        word1, word2 = lines[random.randint(0, len(lines) - 1)].strip().lower().split(" - ")
        while True:
            if word1 in blacklist:
                word1, word2 = lines[random.randint(0, len(lines) - 1)].strip().lower().split(" - ")
            else:
                break
        answer = input(f"* {word1} - ").lower()
        print("-=======================-")
        if answer == word2:
            print("Poprawna odpowiedz\n")
            blacklist.append(word1)
            correct_answers += 1
        else:
            print(f"Bledna odpowiedz, poprawna: {word2}\n")
    print(f"Poprawnych odpowiedzi {correct_answers}/10")
    blacklist.clear()
    correct_answers = 0


if __name__ == "__main__":
    main()