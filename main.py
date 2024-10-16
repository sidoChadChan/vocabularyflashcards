import random

def main():
    while True:
        print("*===============*")
        print("* 1 - Niemiecki *")
        print("*===============*")
        try:
            choose = int(input())
            flashcards(choose)
        except ValueError:
            print("Musisz podac cyfre, nie litere")

def flashcards(choose):
    try:
        with open(f"Sets/{str(choose)}", "r") as file:
            lines = file.readlines()
            while True:
                    word1, word2 = lines[random.randint(0, len(lines) - 1)].strip().lower().split(" - ")
                    answer = input(f"* {word1} - ").lower()
                    print("-=======================-")
                    if answer==word2:
                        "Poprawna odpowiedz\n"
                    elif answer=="0":
                        break
                    else:
                        print(f"Bledna odpowiedz, poprawna: {word2}\n")


    except FileNotFoundError:
        print(f"Plik o numerze {choose} nie został znaleziony")
    except IOError as e:
        print(f"Błąd przy odczycie pliku: {e}")


if __name__ == "__main__":
    main()