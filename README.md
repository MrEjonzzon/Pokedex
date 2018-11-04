# Pokédex
A GUI that is used to present data from my Pokédex database in MySQL. The code can be used for other things than Pokémon of course, but some code will have to be changed to match variables with your table rows etc. 

## What you will need
This program needs to connect to a MySQL database, in line 12 you may change the names to match your own database.
```
self.connection = mysql.connector.connect(user="root", host="127.0.0.1", database="pokedex") #Change this to
self.connection = mysql.connector.connect(user="yourusername", host="Your IP", database="databasename") #This
```

As I mentioned above, this code may be used for other things than Pokémon, but for simplicity I will tell you how to setup your database without having to change the code, should you wish to use it for other things you may do so later.

### Creating database
1. Create a database named "pokedex"
2. Within the database, create a table named "pokemon"
3. Within the table, create these rows (name, type) in the follwing order:


	id, int #Also make this one Primary

	name, varchar(255)

	type1, varchar(255)

	type2, varchar(255)

	height_m, float

	weight_m, float

	entry, text

	Once finished it should look something like this 

	```
		1 	idPrimary 	int(11) 						
		2 	name 	varchar(255) 	latin1_swedish_ci 				
		3 	type1 	varchar(255) 	latin1_swedish_ci 					
		4 	type2 	varchar(255) 	latin1_swedish_ci 				
		5 	height_m 	float 							
		6 	weight_kg 	float 						 	
		7 	entry 	text 	latin1_swedish_ci 						
	```

## Manipulating and presenting database data with GUI
If your database has been correctly set up you should now be able to use the program "Pokedex.py", start off by making sure your MySQL database is on. Once the GUI is on, you will be presented with three different buttons.

### Show Pokémon
This Button will open up a new window with a scrollable list. If you click a Pokémon in that list you will be presented with its stats to the right. If you click on a new Pokémon the stats will update to match.

### Add Pokémon
This button will open up a new  window with 7 different entry fields. Enter your data and click "Add", the Pokémon should now have been added to the database. Type2 can be left empty if Pokémon has none, in practicality all fields can be left empty, but if so nothing will show once you try to look at it.

```
ID: 1
Name: Bulbasaur
Type1: Grass
Type2: Poison
Height: 0.7
Weight: 6.9
Entry: A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON.

```


```
ID: 25
Name: Pikachu
Type1: Electric
Type2: 
Height: 0.7
Weight: 6.9
Entry: When several of these POKéMON gather, their electricity could build and cause lightning storms.
```

### Delete Pokémon
This button will open up a new window with one entry field called "ID". Enter the Pokémon's ID number of which you wish to delete. If you do not know what number the Pokémon you wish to delete has, simply use the "Show Button", it has the id next to the name. 
```
List window
1 Bulbasaur

Delete window
ID: 1

Bulbasaur has now been deleted
```

## Good to knows/Bugs
The program does not give any output for an event, if you wish to know if your data update has been successful you will need to look at the Pokémon list.
