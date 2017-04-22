from bintreeFile import Bintree


def main():
    svenska = Bintree()
    with open('word3.txt', "r",encoding = "utf-8") as svenskfil:
        for line in svenskfil:
            word = line.strip()
            if word in svenska:
                print(word, end = " ")
            else:
                svenska.put(str(word))
    print("\n")




if __name__ == "__main__":
    main()
