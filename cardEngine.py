### Card Engine to be used for card games
#
class Card:
    #               Spade     Hearts    Diamond     Club
    Suits = [u"\u2660",u"\u2661",u"\u2662", u"\u2663"]

    #initialiser in card type, rare to have unspecified card
    #rare meaning if it does happen something else is wrong
    def __init__(self, suits,isred,rank):
        #Insert Proper Unicode Character from above by using an integer 0-3
        self.suit=self.Suits[suits]
        #Color Code Boolean
        self.red=isred
        #Card Rank
        self.rank=rank
        #Card Face so cards can be set face down or not visible (default)
        self.visable=False

    def cardrank(self,x):
        #no point in spelling out, if it needs to be spelled out write a function
        rank= ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        return (rank[x])

    #implicit command to set card face up or down
    def SetVisable(self, State):
        self.visable=State

    def printcard (self):
        #Print simple version of card if face up
        if self.visable:
            print(self.cardrank(self.rank) ,self.suit)
        else:
            print("###")
class Deck:
    Cards = []
    def __init__ (self, new):
        #check to see if its a new game, if so fill the deck with 52 cards
        if (new):
            #suits
            for y in range(4):
                #set a bool for color code on every other suit
                if (y == 1 or y == 2):
                    red=True
                else:
                    red=False
            #ranks 1-13 for cards
                for x in range(13):
                    #+1 because arrays start at 0 and cards start at 1
                    self.Cards.append(Card(y,red,x))

    def Draw(self):
        if self.Cards:
            return self.Cards.pop(0)
        else:
            print("its empty")
    def Place(self,i):
        self.Cards.insert(0,i)

    def Peek(self):
        if self.Cards:
            return self.Cards[0]