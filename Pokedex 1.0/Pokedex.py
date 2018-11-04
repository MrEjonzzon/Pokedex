from tkinter import *
from mysql.connector import errorcode
import mysql.connector


class Pokedex_Connection:
    """ Handles communication to database """

    def __init__(self):
        """ connects to database """
        try:
            self.connection = mysql.connector.connect(user="root", host="127.0.0.1", database="pokedex")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        self.cursor = self.connection.cursor()

    def add_pokemon(self, id, name, type1, type2, height, weight, entry):
        """ Adds Pokémon to database """
        self.cursor.execute(f"INSERT INTO pokemon VALUES {id, name, type1, type2, height, weight, entry}")
        self.connection.commit()

    def delete_pokemon(self, id):
        """ Removes Pokémon from database """
        self.cursor.execute(f"DELETE FROM pokemon WHERE id={id}")
        self.connection.commit()

    def get_pokemon(self):
        """ Returns all values of Pokémon in database """
        self.cursor.execute("SELECT * FROM pokemon")
        return self.cursor.fetchall()

    def close(self):
        """ Closes database """
        self.connection.close()


class ListBox_Window:
    """ Class for List Window """

    def __init__(self, connection):
        """ Creates Window """
        window = Tk()

        self.frame = Frame(window)
        self.frame.pack()
        self.connection = connection
        self.scrollbar()
        self.update_list()
        self.stat_frame = Pokemon_Stats(self.frame, "", "", "", "", "")

        window.mainloop()

    def scrollbar(self):
        """ Creates scrollbar widgets """
        scrollbar = Scrollbar(self.frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.pokemon_list = Listbox(self.frame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.pokemon_list.yview)
        self.pokemon_list.bind("<Double-Button-1>", self.on_select)

    def update_list(self):
        """ Merges Pokémon form list with Pokémon from database """
        self.pokemon = self.connection.get_pokemon()
        for pkmn in self.pokemon:
            self.pokemon_list.insert(END, pkmn[0:2])
        self.connection.close()
        self.pokemon_list.pack(side=LEFT, fill=BOTH)

    def on_select(self, event):
        """ When clicking an item it updates itself to the right """
        selection = self.pokemon_list.curselection()  # Get Seleciton
        pkm = self.pokemon[selection[0]]  # Get pokemon by selection index
        self.stat_frame.pokemon = (pkm[2], pkm[3], pkm[4], pkm[5], pkm[6])  # Show Pokémon stats
        self.stat_frame.update_labels()


class Pokemon_Stats:
    """ Frame for Pokémon stats """

    def __init__(self, root, type1, type2, height, weight, entry):
        self.frame = Frame(root)
        self.labels = []
        self.pokemon = (type1, type2, height, weight, entry)
        self.create_widgets()
        self.frame.pack()

    def create_widgets(self):
        """ Creates labels """
        for stat in self.pokemon:
            label = Label(self.frame, text=stat)
            label.pack()
            self.labels.append(label)

    def update_labels(self):
        """ Updates labels to self.pokemon """
        for i in range(5):
            self.labels[i].config(text=self.pokemon[i])


def show_pokemon(event):
    """ Creates list window """
    window = ListBox_Window(Pokedex_Connection())


def add_new_pokemon(event):
    window = Tk()

    def add(event):
        """ Adds entries within the fields """
        connection = Pokedex_Connection()
        connection.add_pokemon(id_entry.get(), name_entry.get(), type1_entry.get(), type2_entry.get(),
                               height_entry.get(), weight_entry.get(), entry_entry.get())
        connection.close()

    """ GUI Styling """
    id = Label(window, text="ID")
    id.grid(row=0, sticky=E)
    id_entry = Entry(window)
    id_entry.grid(row=0, column=1)

    name = Label(window, text="Name")
    name.grid(row=1, sticky=E)
    name_entry = Entry(window)
    name_entry.grid(row=1, column=1)

    type1 = Label(window, text="Type 1")
    type1.grid(row=2, sticky=E)
    type1_entry = Entry(window)
    type1_entry.grid(row=2, column=1)

    type2 = Label(window, text="Type 2")
    type2.grid(row=3, sticky=E)
    type2_entry = Entry(window)
    type2_entry.grid(row=3, column=1)

    height = Label(window, text="Height")
    height.grid(row=4, sticky=E)
    height_entry = Entry(window)
    height_entry.grid(row=4, column=1)

    weight = Label(window, text="Weight")
    weight.grid(row=5, sticky=E)
    weight_entry = Entry(window)
    weight_entry.grid(row=5, column=1)

    entry = Label(window, text="Entry")
    entry.grid(row=6, sticky=E)
    entry_entry = Entry(window)
    entry_entry.grid(row=6, column=1)

    add_button = Button(window, text="Add")
    add_button.grid(row=7, column=1)
    add_button.bind("<Button-1>", add)

    window.mainloop()


def delete_new_pokemon(event):
    window = Tk()

    def delete(event):
        """ Deletes Pokémon through ID equal to what is given in entry """
        connection = Pokedex_Connection()
        connection.delete_pokemon(id_entry.get())
        connection.close()

    id = Label(window, text="ID")
    id.grid(row=0, sticky=E)
    id_entry = Entry(window)
    id_entry.grid(row=0, column=1)

    delete_button = Button(window, text="Delete")
    delete_button.grid(row=7, column=1)
    delete_button.bind("<Button-1>", delete)


""" Root Window """
root = Tk()
root.title("Pokédex")
frame = Frame(root, height=400, width=300)
frame.pack()

photo = PhotoImage(file="pokedexroot.gif")
label = Label(frame, image=photo)
label.pack()

show_pokemon_button = Button(frame, text="Show Pokémon")
show_pokemon_button.place(x=30, y=120)
show_pokemon_button.bind("<Button-1>", show_pokemon)

add_pokemon_button = Button(frame, text="Add Pokémon")
add_pokemon_button.place(x=30, y=165)
add_pokemon_button.bind("<Button-1>", add_new_pokemon)

delete_pokemon_button = Button(frame, text="Delete Pokémon")
delete_pokemon_button.place(x=30, y=205)
delete_pokemon_button.bind("<Button-1>", delete_new_pokemon)

root.mainloop()
