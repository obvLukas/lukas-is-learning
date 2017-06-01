# Kod av Lukas Hennicks
# -*- coding: utf-8 -*-

from array import array
#from linkedQFile import LinkedQ
class ArrayQ():

    def __init__(self):
        self.array = []

    def enqueue(self, val):
        self.__val = val
        self.array.append(self.__val)

    def dequeue(self):
        return self.array.pop(0)

    def isEmpty(self):
        if self.array == []:
            return True
        else:
            return False


#TESTPROGRAM
def testQ():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    print(x,y)   # 1 2 ska komma ut


def main():
    cardVal = raw_input('Skriv din ordning på korten:\n')
    cardVal = cardVal.split(" ")
    #cardVal = [int(i) for i in cardVal]
    q = ArrayQ()
    shown_cards = []
    i = 0
    x = 0

    while True:
        try:
            q.enqueue(cardVal[i])
        #    print(str(cardVal[i]) + ' enqueued')
            i += 1
            try:
                shown_cards.append(cardVal[i])
            #    print(str(cardVal[i+1]) + ' shown')
                i += 1

            except:
                break
        except:
            break


    while True:
        shown_cards.append(q.dequeue())
        if q.isEmpty() == True:
            break


#    print shown_cards

    from time import sleep
    cardCount = 0

    while True:
        try:
            print('The magician puts %s on the table...') % (shown_cards[cardCount])
            #print('The magician puts %s on the table...') % (q.dequeue())
            cardCount += 1
            sleep(1)
        except:
            break
#6 1 7 2 8 3 9 4 10 5 ger [1 2 3 4 5 6 7 8 9 10]

if __name__ == '__main__':
    main()
