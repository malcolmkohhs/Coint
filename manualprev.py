import tkinter as tk
from tkinter import *


main_screen = Tk()

main_screen.geometry('600x400')

main_screen .title('Manual Coin Finder')
main_title = tk.Label(text='Start?', font=('Open Sans', 25, 'bold'))


#if they choose to start the programme
def gold_window():
    main_screen.destroy()
    global new_gold
    new_gold = tk.Tk()
    new_gold.title('Manual Coin Finder')
    new_gold.geometry('600x400')
    l1 = Label(new_gold, text="Is the coin mainly gold?", font=('Arial', 25, 'bold'))
    l1.pack()
    gold_yes_btn = Button(new_gold, text='Yes', pady=40, padx=70, command=small_gold)
    gold_no_btn = Button(new_gold, text='No', pady=40, padx=70, command=silver_window)
    gold_no_btn.pack()
    gold_no_btn.place(y=150,x=408)
    gold_yes_btn.pack()
    gold_yes_btn.place(y=150, x=0)


#if they choose gold , ask if its small
def small_gold():
    new_gold.destroy()
    global small_gold_window
    small_gold_window = tk.Tk()
    small_gold_window.title('Manual Coin Finder')
    small_gold_window.geometry('600x400')
    small_gold_window_label = Label(small_gold_window, text="Is the coin small?", font=('Arial', 25,'bold'))
    small_gold_yes_btn = Button(small_gold_window, text= 'Yes', pady=40, padx=70, command=five_cent)
    small_gold_no_btn = Button(small_gold_window, text='No', pady=40, padx=70, command=one_dollar_coin1)
    small_gold_yes_btn.place(y=150, x=0)
    small_gold_no_btn.place(y=150,x=408)

    small_gold_window_label.pack()

def one_dollar_coin1():
    small_gold_window.destroy()
    global one_dollar_window1_1
    one_dollar_window1_1 = tk.Tk()
    one_dollar_window1_1.title("Manual Coin FInder")
    one_dollar_window1_1.geometry('600x400')
    one_dollar_Label1_1 = Label(one_dollar_window1_1, text='This is a 1 Dollar ($1) coin.', font=('Arial', 30,'bold'))
    one_dollar_Label2_1 = Label(one_dollar_window1_1, text = 'On the coin, a Merlion can be seen with the number 1 on it', font=('Arial', 22))
    one_dollar_Label1_1.pack()
    one_dollar_Label1_1.place(x=0, y=0)
    one_dollar_Label2_1.pack()
    one_dollar_Label2_1.place(x=0, y=40)

#when its gold and small = 5 cent
def five_cent():
    small_gold_window.destroy()
    global five_cent_coin
    five_cent_coin=tk.Tk()
    five_cent_coin.title('Manual Coin Finder')
    five_cent_coin.geometry('600x400')
    five_cent_Label1 = Label(five_cent_coin, text='This is a 5 cent (5¢) coin.', font=('Arial', 30,'bold'))
    five_cent_Label2 = Label(five_cent_coin, text='On the coin, there is an Esplanade together with a number 5 on it', font=('Arial', 20))
    five_cent_Label1.pack()
    five_cent_Label1.place(x=0, y=0)
    five_cent_Label2.pack()
    five_cent_Label2.place(x=0, y=40)

'''
    five_cent_img = PhotoImage(file = "five_cent_coin_two.png")
    five_cent_img_panel = tk.Label(five_cent_coin, image=five_cent_img)
    five_cent_img_panel.pack()
    five_cent_img_panel.place(x=0, y=0)
'''


'''

    five_cent_img = PhotoImage(file = "five_cent_coin_two.png")
    five_cent_img = five_cent_img.resize((100,100))
    five_cent_img_panel = tk.Label(five_cent_coin, image=five_cent_img)
    five_cent_img_panel.pack()
    five_cent_img_panel.place(x=0,y=0)



    five_cent_img = Image.open("five_cent_coin_two.png")
    five_cent_img = bgimg.resize((540, 60))
    five_cent_img = ImageTk.PhotoImage(bgimg)
    five_cent_panel = tk.Label(resultp, image=bgimg)
    five_cent_panel.image = bgimg
'''

#when its not gold
def silver_window():
    new_gold.destroy()
    global coin_silver_window
    coin_silver_window = tk.Tk()
    coin_silver_window.title('Manual Coin Finder')
    coin_silver_window.geometry('600x400')
    silver_Label = Label(coin_silver_window, text='Is the coin mainly silver?', font=('Arial', 25,'bold'))
    silver_Label.pack()
    silver_Label.place(x=170, y=0)
    silver_no_btn = Button(coin_silver_window, text='No', pady=40, padx=70, command=one_dollar_coin2)
    silver_yes_btn = Button(coin_silver_window, text='Yes', pady=40, padx=70, command=small_silver)
    silver_yes_btn.pack()
    silver_no_btn.pack()
    silver_yes_btn.place(y=150, x=0)

    silver_no_btn.place(y=150,x=408)


# when its not MAINLY silver,
def one_dollar_coin2():
    coin_silver_window.destroy()
    global one_dollar_window2
    one_dollar_window2 = tk.Tk()
    one_dollar_window2.title("Manual Coin FInder")
    one_dollar_window2.geometry('600x400')
    one_dollar_Label1 = Label(one_dollar_window2, text='This is a 1 Dollar ($1) coin.', font=('Arial', 30,'bold'))
    one_dollar_Label2 = Label(one_dollar_window2, text='On the coin, a Merlion can be seen with the number 1 on it', font=('Arial', 22))
    one_dollar_Label1.pack()
    one_dollar_Label1.place(x=0, y=0)
    one_dollar_Label2.pack()
    one_dollar_Label2.place(x=0, y=40)


'''

PHOTO

'''



# when it is silver,
def small_silver():
    coin_silver_window.destroy()
    global silver_and_small_window
    silver_and_small_window = tk.Tk()
    silver_and_small_window.title('Manual Coin Finder')
    silver_and_small_window.geometry('600x400')
    silver_small_Label = Label(silver_and_small_window, text='Is the coin small?', font=('Arial', 25,'bold'))
    silver_small_Label.pack()

    small_silver_no_btn = Button(silver_and_small_window, text='No', pady=40, padx=70, command=changi_airport_image)
    small_silver_yes_btn = Button(silver_and_small_window, text='Yes', pady=40, padx=70, command=ten_cent_coin)
    small_silver_yes_btn.pack()
    small_silver_yes_btn.place(y=150, x=0)
    small_silver_no_btn.pack()
    small_silver_no_btn.place(y=150,x=408)


#when its small and silver
def ten_cent_coin():
    silver_and_small_window.destroy()
    global ten_cent_window
    ten_cent_window = tk.Tk()
    ten_cent_window.title('Manual Coin Finder')
    ten_cent_window.geometry('600x400')
    ten_cent_Label1 = Label(ten_cent_window, text='This is a 10 cent (10¢) coin.', font=('Arial', 30,'bold'))
    ten_cent_Label2 = Label(ten_cent_window, text='On the coin, HBDs can be seen with the number 10 on it', font=('Arial', 23))
    ten_cent_Label1.pack()
    ten_cent_Label1.place(x=0, y=0)
    ten_cent_Label2.pack()
    ten_cent_Label2.place(x=0, y=40)

'''

PHOTO

'''

#when its not small but silver
def changi_airport_image():
    silver_and_small_window.destroy()
    global changi_airport_window
    changi_airport_window = tk.Tk()
    changi_airport_window.title('Manual Coin Finder')
    changi_airport_window.geometry('600x400')
    changi_airport_Label = Label(changi_airport_window,text='Does the coin have an image of Changi Airport?', font=('Arial', 25,'bold'))
    changi_airport_Label.pack()

    changi_airport_no_btn = Button(changi_airport_window, text='No', pady=40, padx=70, command=fifty_cent_coin)
    changi_airport_yes_btn = Button(changi_airport_window, text='Yes', pady=40, padx=70, command=twenty_cent_coin)
    changi_airport_yes_btn.pack()
    changi_airport_yes_btn.place(y=150, x=0)
    changi_airport_no_btn.pack()
    changi_airport_no_btn.place(y=150,x=408)

'''
    changi_airport_img = PhotoImage(file = "changi_airport.jpg")
    changi_airport_img_panel = tk.Label(changi_airport_window, image=changi_airport_img)
    changi_airport_img_panel.pack()
    changi_airport_img_panel.place(x=0, y=0)
'''

#when there is no picture fo changi airport
def fifty_cent_coin():
    changi_airport_window.destroy()
    global fifty_cent_window
    fifty_cent_window = tk.Tk()
    fifty_cent_window.title("Manual Coin Finder")
    fifty_cent_window.geometry('600x400')
    fifty_cent_Label1 = Label(fifty_cent_window, text='This is a 50 cent (50¢) coin.', font=('Arial', 30,'bold'))
    fifty_cent_Label2 = Label(fifty_cent_window, text='On the coin, the Port of Singapore can be seen with the number 50 on it', font=('Arial', 18))
    fifty_cent_Label1.pack()
    fifty_cent_Label2.pack()

    fifty_cent_Label1.place(x=0, y=0)
    fifty_cent_Label2.place(x=0, y=40)




#when there is a picture of changi airport
def twenty_cent_coin():
    changi_airport_window.destroy()
    global twenty_cent_window
    twenty_cent_window = tk.Tk()
    twenty_cent_window.title('Manual Coin Finder')
    twenty_cent_window.geometry('600x400')
    twenty_cent_Label1 = Label(twenty_cent_window, text='This is a 20 cent (20¢) coin.', font=('Arial', 26,'bold'))
    twenty_cent_Label2 = Label(twenty_cent_window, text='On the coin, Changi Airport can be seen with the number 20 on it', font=('Arial', 20))
    twenty_cent_Label1.pack()
    twenty_cent_Label2.pack()

    twenty_cent_Label1.place(x=0, y=0)
    twenty_cent_Label2.place(x=0, y=40)




#if they choose to quit the manual coing finder
def quit_window():
    main_screen.destroy()
    global quit_screen
    quit_screen = tk.Tk()
    quit_screen.title('Manual Coin Finder')
    quit_screen.geometry('600x400')
    quit_gon = tk.Label(quit_screen, text="Goodbye!", font=('Arial', 40))
    quit_gon.pack()
    quit_gon.place(x =216, y = 150 )



main_start_btn = Button(text = 'Start',pady = 40, padx = 70,command= gold_window)
main_end_btn = Button(text='Quit', pady=40, padx=70, command=quit_window)

main_title.pack()

main_end_btn.pack()
main_end_btn.place(y=150, x=400)
main_start_btn.pack()
main_start_btn.place(y=150, x=0)

main_screen.mainloop()

