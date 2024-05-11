from tkinter import *
from tkinter import messagebox
from main import *


global p1_hand
global p2_hand
global p3_hand
global p4_hand
global p1_action
global p2_action
global p3_action
global p4_action
global cur_card
global num_players
global n_players
global confirmation
global turn_count
global check
global input_window
global ace_window
confirmation = False




def open_game_window():
   check = "n"
   game_window = Tk()
   game_window.title("Blackjack")
   game_window.geometry("1920x1080")
   p1_hand = IntVar()
   p2_hand = IntVar()
   p3_hand = IntVar()
   p4_hand = IntVar()
   p1_action = StringVar()
   p2_action = StringVar()
   p3_action = StringVar()
   p4_action = StringVar()
   turn_count = StringVar()
   cur_card = StringVar()


   def take_input():
       global input_window
       def d():
           global check
           check = "y"
           input_window.quit()
           input_window.destroy()


       def f():
           global check
           check = "n"
           input_window.quit()
           input_window.destroy()


       input_window = Toplevel(game_window)
       input_window.geometry("700x300")
       input_window.title("Draw or Forfeit?")


       card_title = Label(input_window, text="Current card: ", font=("Helvetica", 24))
       card_title.pack(side=TOP)


       current_card = Label(input_window, textvariable=cur_card)
       current_card.place(in_=card_title, bordermode="outside", anchor="s", y=200, relx=0.48)


       draw_button = Button(input_window, text="Draw", bg="black", fg="white", command=d)
       draw_button.place(in_=card_title, bordermode="outside", anchor="s", y=250, relx=0.35)


       forfeit_button = Button(input_window, text="Forfeit", bg="red", fg="black", command=f)
       forfeit_button.place(in_=draw_button, bordermode="outside", anchor="w", rely=0.45, relx=1.3)


   def ace_check(card):
       global ace_window
       def value_check():
           match ace_value.get():
               case '1':
                   card.ace_draw(1)
                   ace_window.destroy()
               case '11':
                   card.ace_draw(11)
                   ace_window.destroy()
               case _:
                   messagebox.showerror("Invalid value", message="That is not a valid value for an ace. Try again.", parent=ace_window)


       ace_window = Toplevel(game_window)
       ace_value = StringVar()
       ace_window.geometry("700x300")
       ace_window.title("1 or 11?")


       card_title = Label(ace_window, text="You have drawn an ace. Would you like its value to be 1 or 11?",
                          font=("Helvetica", 16))
       card_title.pack(side=TOP)


       current_card = Label(ace_window, textvariable=cur_card)
       current_card.place(in_=card_title, bordermode="outside", anchor="s", y=100, relx=0.5)


       number = Entry(ace_window, textvariable=ace_value)
       number.place(in_=card_title, bordermode="outside", anchor="s", y=150, relx=0.5)


       check_button = Button(ace_window, text="Draw", bg="white", fg="black", command=value_check)
       check_button.place(in_=card_title, bordermode="outside", anchor="s", y=200, relx=0.5)


   def play():
       global check
       global input_window
       start_button.destroy()
       while True:
           counter = 0
           start_card = deck[0]
           for player in player_list:
               counter += 1
               match counter:
                   case 1:
                       p1_space.config(bg="#da4c3e")
                       p2_space.config(bg="white")
                       p3_space.config(bg="white")
                       p4_space.config(bg="white")
                   case 2:
                       p1_space.config(bg="white")
                       p2_space.config(bg="#da4c3e")
                       p3_space.config(bg="white")
                       p4_space.config(bg="white")
                   case 3:
                       p1_space.config(bg="white")
                       p2_space.config(bg="white")
                       p3_space.config(bg="#da4c3e")
                       p4_space.config(bg="white")
                   case 4:
                       p1_space.config(bg="white")
                       p2_space.config(bg="white")
                       p3_space.config(bg="white")
                       p4_space.config(bg="#da4c3e")
               t = "Player " + str(counter) + "'s Turn"
               turn_count.set(t)
               if type(player) == HumanPlayer:
                   for card in deck:
                       if not player.pass_flag:
                           cur_card.set(card.fullname)
                           take_input()
                           game_window.wait_window(input_window)
                           if check == "y":
                               ace_list = ["Ace of Hearts", "Ace of Spades", "Ace of Diamonds", "Ace of Clubs"]
                               if cur_card.get() in ace_list:
                                   ace_check(card)
                                   game_window.wait_window(ace_window)
                               player.draw(card)
                               deck.remove(card)
                               match counter:
                                   case 1:
                                       p1_hand.set(player.hand)
                                       string = "Drew " + card.fullname
                                       p1_action.set(string)
                                   case 2:
                                       p2_hand.set(player.hand)
                                       string = "Drew " + card.fullname
                                       p2_action.set(string)
                                   case 3:
                                       p3_hand.set(player.hand)
                                       string = "Drew " + card.fullname
                                       p3_action.set(string)
                                   case 4:
                                       p4_hand.set(player.hand)
                                       string = "Drew " + card.fullname
                                       p4_action.set(string)
                               game_window.update()
                               if player.hand > 21:
                                   player.pass_flag = True
                                   messagebox.showwarning("Oops!", message="You went bust! You lose.")
                               time.sleep(2)
                               break
                           else:
                               player.pass_flag = True
                       else:
                           break




               elif type(player) == AIPlayer:
                   player.card_drawn = False
                   for card in deck:
                       if not player.pass_flag:
                           cur_card.set(card.fullname)
                           game_window.update()
                           time.sleep(1)
                           player.evaluate(card)
                           if player.card_drawn:
                               deck.remove(card)
                               match counter:
                                   case 1:
                                       p1_hand.set(player.hand)
                                       string = "Drew " + card.fullname
                                       p1_action.set(string)
                                   case 2:
                                       p2_hand.set(player.hand)
                                       string = "Drew " + card.fullname
                                       p2_action.set(string)
                                   case 3:
                                       p3_hand.set(player.hand)
                                       string = "Drew " + card.fullname
                                       p3_action.set(string)
                                   case 4:
                                       p4_hand.set(player.hand)
                                       string = "Drew " + card.fullname
                                       p4_action.set(string)
                           game_window.update()
                           time.sleep(2)
                           break
                       else:
                           break


           if start_card is deck[0]:
               break


       winning_hand = 0
       for player in player_list:
           for player2 in player_list:
               if player.hand > player2.hand and player.hand > winning_hand and player.hand <= 21:
                   winning_hand = player.hand
                   winning_player_no = player_list.index(player) + 1
       win = "Congratulations! Player " + str(winning_player_no) + " won with a " + str(winning_hand) + "!"
       messagebox.showinfo("Congrats!", message=win)


   p1_space = Frame(game_window, width=600, height=320, highlightbackground="black", highlightthickness=1)
   p1_space.pack(side=BOTTOM)
   p1_space.pack_propagate(False)


   p1_title = Label(p1_space, text="Player 1's Hand:", font=("Arial", 32))
   p1_title.pack(side=TOP)


   p1_text = Label(p1_space, textvariable=p1_hand, font=("Helvetica", 24))
   p1_text.pack(side=TOP, expand=1)


   p1_action_space = Label(p1_space, textvariable=p1_action)
   p1_action_space.place(in_=p1_text, bordermode="outside", anchor="s", y=90, relx=0.5)


   center_space = Frame(game_window, width=600, height=320)
   center_space.pack(side=BOTTOM)
   center_space.pack_propagate(False)


   center_title = Label(center_space, text="Current Card:", font=("Arial", 32))
   center_title.pack(side=TOP)


   card_space = Label(center_space, textvariable=cur_card)
   card_space.place(in_=center_title, bordermode="outside", anchor="n", y=200, relx=0.5)


   turn_counter = Label(center_space, textvariable=turn_count, font=("Helvetica", 14))
   turn_counter.place(in_=center_title, bordermode="outside", anchor="ne", y=60, relx=0.75)


   start_button = Button(center_space, text="Start", command=play)
   start_button.place(in_=center_title, bordermode="outside", anchor="s", y=250, relx=0.5)


   p2_space = Frame(game_window, width=600, height=320, highlightbackground="black", highlightthickness=1)
   p2_space.place(in_=center_space, bordermode="outside", anchor="ne")
   p2_space.pack_propagate(False)


   p2_title = Label(p2_space, text="Player 2's Hand:", font=("Arial", 32))
   p2_title.pack(side=TOP)


   p2_text = Label(p2_space, textvariable=p2_hand, font=("Helvetica", 24))
   p2_text.pack(side=RIGHT, expand=1)


   p2_action_space = Label(p2_space, textvariable=p2_action)
   p2_action_space.place(in_=p2_text, bordermode="outside", anchor="s", y=150, relx=0.5)


   p3_space = Frame(game_window, width=600, height=320, highlightbackground="black", highlightthickness=1)
   p3_space.place(in_=center_space, bordermode="outside", anchor="nw", relx=1.0)
   p3_space.pack_propagate(False)


   p3_text = Label(p3_space, textvariable=p3_hand, font=("Helvetica", 24))
   p3_text.pack(side=BOTTOM, expand=1)


   p3_title = Label(p3_space, text="Player 3's Hand:", font=("Arial", 32))
   p3_title.pack(side=TOP)


   p3_action_space = Label(p3_space, textvariable=p3_action)
   p3_action_space.place(in_=p3_text, bordermode="outside", anchor="s", y=150, relx=0.5)


   p4_space = Frame(game_window, width=600, height=320, highlightbackground="black", highlightthickness=1)
   p4_space.pack(side=BOTTOM)
   p4_space.pack_propagate(False)


   p4_title = Label(p4_space, text="Player 4's Hand:", font=("Arial", 32))
   p4_title.pack(side=TOP)


   p4_text = Label(p4_space, textvariable=p4_hand, font=("Helvetica", 24))
   p4_text.pack(side=LEFT, expand=1)


   p4_action_space = Label(p4_space, textvariable=p4_action)
   p4_action_space.place(in_=p4_text, bordermode="outside", anchor="s", y=110, relx=0.5)


   game_window.mainloop()




def player_confirm():
   window = Tk()
   global num_players
   global confirmation


   def check_players():
       global num_players
       global confirmation
       global n_players
       try:
           n_players = int(num_players.get())
           if n_players > 4 or n_players < 0:
               messagebox.showerror("Invalid input", message="That is not a valid number of players")
               num_players.set("")
           else:
               messagebox.showinfo("Players confirmed!", message="Enjoy your game")
               window.destroy()
       except ValueError:
           messagebox.showerror("Invalid input", message="That is not a valid number of players")
           num_players.set("")
       return n_players


   num_players = StringVar()
   window.title("Please confirm the number of players")
   window.geometry("750x300")
   window.config(background="#da4c3e")
   window.resizable(False, False)


   enter_players = Label(window, text="Please enter the number of human players (0-4): ", font=("Helvetica", 24),
                         bg="#da4c3e")
   enter_players.pack(side=TOP, expand=1)
   player_entry = Entry(window, textvariable=num_players)
   player_entry.pack(side=TOP, expand=1, ipadx=200, ipady=30)


   player_button = Button(window, text="Confirm", bg="black", fg="white", command=check_players)
   player_button.pack(side=TOP, expand=1, ipadx=100, ipady=10)
   window.mainloop()




player_list = []
player_confirm()
print(n_players)


for i in range(1, n_players + 1):
   g = HumanPlayer()
   player_list.append(g)


if len(player_list) < 4:
   for i in range(len(player_list), 4):
       g = AIPlayer()
       player_list.append(g)
print(player_list)
generate_deck()
print(len(deck))
open_game_window()


