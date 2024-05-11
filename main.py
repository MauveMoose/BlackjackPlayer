import random
from tkinter import *
import time


global suits
global courts
global aces


global hearts_nums
global spades_nums
global clubs_nums
global diamonds_nums


global hearts_courts
global spades_courts
global clubs_courts
global diamonds_courts
global n_players


global deck


suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
courts = ['King', 'Queen', 'Jack']
aces = ['Ace of Hearts', 'Ace of Spades', 'Ace of Clubs', 'Ace of Diamonds']


hearts_nums = []
spades_nums = []
clubs_nums = []
diamonds_nums = []


hearts_courts = []
spades_courts = []
clubs_courts = []
diamonds_courts = []


deck = []


for x in range(1, 14):
   hearts_nums.append(x)
   spades_nums.append(x)
   clubs_nums.append(x)
   diamonds_nums.append(x)
for x in range(0, 3):
   hearts_courts.append(courts[x])
   spades_courts.append(courts[x])
   clubs_courts.append(courts[x])
   diamonds_courts.append(courts[x])




class Card:
   def __init__(self):
       while True:
           i = random.randint(0, 3)
           self.suit = suits[i]
           i = random.randint(0, 13)
           self.value = 0
           match self.suit:
               case 'Hearts':
                   try:
                       self.value = hearts_nums[i]
                   except IndexError:
                       continue
                   else:
                       hearts_nums.remove(self.value)
                       if self.value > 10:
                           while True:
                               i = random.randint(0, 2)
                               try:
                                   self.name = hearts_courts[i]
                               except IndexError:
                                   continue
                               else:
                                   hearts_courts.remove(self.name)
                                   self.value = 10
                                   break
                       elif self.value == 1:
                           self.name = "Ace"
                       else:
                           self.name = str(self.value)
               case 'Spades':
                   try:
                       self.value = spades_nums[i]
                   except IndexError:
                       continue
                   else:
                       spades_nums.remove(self.value)
                       if self.value > 10:
                           while True:
                               i = random.randint(0, 2)
                               try:
                                   self.name = spades_courts[i]
                               except IndexError:
                                   continue
                               else:
                                   spades_courts.remove(self.name)
                                   self.value = 10
                                   break
                       elif self.value == 1:
                           self.name = "Ace"
                       else:
                           self.name = str(self.value)
               case 'Diamonds':
                   try:
                       self.value = diamonds_nums[i]
                   except IndexError:
                       continue
                   else:
                       diamonds_nums.remove(self.value)
                       if self.value > 10:
                           while True:
                               i = random.randint(0, 2)
                               try:
                                   self.name = diamonds_courts[i]
                               except IndexError:
                                   continue
                               else:
                                   diamonds_courts.remove(self.name)
                                   self.value = 10
                                   break
                       elif self.value == 1:
                           self.name = "Ace"
                       else:
                           self.name = str(self.value)
               case 'Clubs':
                   try:
                       self.value = clubs_nums[i]
                   except IndexError:
                       continue
                   else:
                       clubs_nums.remove(self.value)
                       if self.value > 10:
                           while True:
                               i = random.randint(0, 2)
                               try:
                                   self.name = clubs_courts[i]
                               except IndexError:
                                   continue
                               else:
                                   clubs_courts.remove(self.name)
                                   self.value = 10
                                   break
                       elif self.value == 1:
                           self.name = "Ace"
                       else:
                           self.name = str(self.value)
           if self.value != 0:
               break
       self.fullname = self.name + " of " + self.suit


   def display(self):
       print(self.fullname)


   def ace_draw(self, v):
       if v == 1:
           self.value = 1
       elif v == 11:
           self.value = 11




class Player:
   def __init__(self):
       self.hand = 0
       self.pass_flag = False


   def draw(self, Card):
       self.hand += Card.value




class AIPlayer(Player):
   def __init__(self):
       super().__init__()
       self.card_drawn = False


   def draw(self, Card):
       super().draw(Card)


   def forfeit(self):
       self.pass_flag = True


   def evaluate(self, Card):
       if Card.fullname not in aces:
           if self.hand + Card.value <= 21:
               self.draw(Card)
               self.card_drawn = True
           else:
               self.forfeit()
       elif self.hand + 11 <= 21:
           Card.ace_draw(11)
           self.draw(Card)
           self.card_drawn = True
       elif self.hand + 1 <= 21:
           Card.ace_draw(1)
           self.draw(Card)
           self.card_drawn = True
       else:
           self.forfeit()


   def show_hand(self):
       print(self.hand)




class HumanPlayer(Player):
   def __init__(self):
       super().__init__()


   def draw(self, Card):
       super().draw(Card)




def generate_deck():
   for i in range(1, 53):
       c = Card()
       deck.append(c)


