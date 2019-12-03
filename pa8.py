
import random

class Card:
    def __int__(self):
        self.__Rank = randint(1,13)
        self.__Suit = randint(1,4)
        
    def GetSuitName(self):
        if self.__Suit == 1:
            return 'clubs'
        elif self.__Suit == 2:
            return 'diamonds'
        elif self.__Suit == 3:
            return 'hearts'
        elif self.__Suit == 4:
            return 'spades'

    def GetRankName(self):
        if self.__Rank == 1:
            return 'Ace'
        elif self.__Rank >=2 and self.__rank <=10:
            return self.__Rank
        elif self.__Rank == 11:
            return 'Jack'
        elif self.__Rank == 12:
            return 'Queen'
        elif self.__Rank == 13:
            return 'King'
        
    def GetPointValue(self):
        TP = 0
        
        if (self.__Rank == 1):
            TP = TP + 11
            TP2 = TP2 + 11
        elif (self.__Rank >=2) and (self.__Rank <=10):
            TP = TP + self.__Rank
            TP2 = TP2 + self.__Rank
        elif (self.__Rank == 11):
            TP = TP + 10
            TP2 = TP2 + 10
        elif (self.__Rank == 12):
            TP = TP + 10
            TP2 = TP2 + 10
        elif (self.__Rank == 13):
            TP = TP + 10
            TP2 = TP2 + 10
            
        print(format('Total Points: ','16f'),TP,'         ',TP2)


def main():
    card1 = Card()
    card1.GetSuitName()
    card1.GetRankName()
    print(card1.GetSuitName)

    card2 = Card()
    card2.GetSuitName()
    card2.GetRankName()
    print(card2.GetsuitName)
                
    


main()









        
    
