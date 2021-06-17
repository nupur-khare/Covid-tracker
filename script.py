import requests
import bs4
from tkinter import *  
import tkinter as tk
import tkinter.font
def get_html_data(url):
    data = requests.get(url)
    return data

def get_covid_data():
    url = "https://www.worldometers.info/coronavirus"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = " "

    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_data = all_data + text + " " + count + "\n"
    return all_data

def get_country_data():
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/" +name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""

    for block in info_div:
        text = block.find("h1", class_=None)
        count = block.find("span", class_=None)
        if text is not None and count is not None:
            all_data = all_data + text.get_text() + " " + count.get_text() + "\n"
    mainlabel['text']=all_data

def reload():
    new_data = get_covid_data()
    mainlabel['text'] = new_data

get_covid_data()

root = tk.Tk()
root.geometry("700x700")
root.configure(bg='RosyBrown3')
root.title("Covid Tracker")
f = tkinter.font.Font( family = "Comic Sans MS", size = 25, weight = "bold")
f1 = tkinter.font.Font( family = "Montserrat", size = 15)
banner = tk.PhotoImage(file="covid.jpg")
bannerlable = tk.Label(root, image=banner,bg='RosyBrown3')
bannerlable.pack()
textfield = tk.Entry(root, width=50)
textfield.pack()
mainlabel = tk.Label(root, text=get_covid_data(), font=f, bg='RosyBrown3')
mainlabel.pack()

gbtn = tk.Button(root, text="Get Data", font=f1, relief='raised', padx=10, pady=10, bg='ivory2', command=get_country_data)
gbtn.pack(side=RIGHT, padx=15, pady=20) 
rbtn = tk.Button(root, text="Refresh", font=f1, relief='raised', padx=10, pady=10,bg='ivory2', command=reload)
rbtn.pack(side=LEFT, padx=15, pady=20)

root.mainloop()

