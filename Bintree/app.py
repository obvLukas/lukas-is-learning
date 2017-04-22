from bintreeFile import Bintree
engelska = Bintree()
svenska = Bintree()

def main():

    svenska = Bintree()
    with open('word3.txt', "r",encoding = "utf-8") as svenskfil:
        for line in svenskfil:
            word = line.strip()
            if word in svenska:
                pass
            else:
                svenska.put(str(word))
    print("\n")

    with open('engelska.txt', "r", encoding = "utf-8") as fil:
        for line in fil:
            if len(line) > 1:
                rad = line.strip().split(" ")
                for word in rad:
                    word = (word.replace(",","").replace("\"","").replace(".","").replace("!",""))
                    if word in engelska:
                        pass
                    else:
                        engelska.put(str(word))
                        if word in svenska:
                            print(word, end = " ")
    print('\n')



if __name__ == "__main__":
    main()
