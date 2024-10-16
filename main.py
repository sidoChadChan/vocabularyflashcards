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
            content = file.read()
            print("hej")
            print(content)
    except FileNotFoundError:
        return "Plik nie został znaleziony"
    except IOError:
        return "Błąd przy odczycie pliku"

if __name__ == "__main__":
    main()