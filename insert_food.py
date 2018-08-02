import sqlite3

conn = sqlite3.connect('allFoods.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS ALLFOOD (id INT PRIMARY KEY NOT NULL, name TEXT  NOT NULL, calories INT NOT NULL, ingredients TEXT, price REAL NOT NULL, image TEXT, date DATE)''')
index = 0
c.execute('''SELECT * FROM ALLFOOD''')
for row in c:
    index = index + 1

#Section for the Everyday items
NULL= "NULL"
c.execute('''SELECT * FROM ALLFOOD WHERE name = "Hamburger" AND calories = 354''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Hamburger", 354, "meat, bun", 2.20, "hamburger.jpg", NULL))


c.execute('''SELECT * FROM ALLFOOD WHERE name = "Cheeseburger" AND calories = 454''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Cheeseburger", 454, "meat, bun, cheese", 2.55, "cheeseburger.png", NULL))


c.execute('''SELECT * FROM ALLFOOD WHERE name = "Bacon Cheeseburger" AND calories = 545''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Bacon Cheeseburger", 545, "meat, bun, cheese, bacon", 2.85, "bacon-cheeseburger.png", NULL))



c.execute('''SELECT * FROM ALLFOOD WHERE name = "Veggie Burger" AND calories = 254''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Veggie Burger", 254, "meatless patty, bun", 2.40, "veggie-burger.png", NULL))



c.execute('''SELECT * FROM ALLFOOD WHERE name = "Steak & Cheese" AND calories = 600''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Steak & Cheese", 600, "steak, cheese, bun, cheese", 2.40, "steak-and-cheese.png", NULL))



c.execute('''SELECT * FROM ALLFOOD WHERE name = "Grilled Cheese w/ Bacon" AND calories = 300''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Grilled Cheese w/ Bacon", 300, "2 slices of bread, cheese, bacon", 2.15, "grilled-cheese-bacon.jpg", NULL))



c.execute('''SELECT * FROM ALLFOOD WHERE name = "Grilled Chicken Sandwich" AND calories = 300''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Grilled Chicken Sandwich", 300, "meat, bun, cheese", 3.45, "grilled-chicken-sand.png", NULL))



c.execute('''SELECT * FROM ALLFOOD WHERE name = "Grilled Chicken Breast" AND calories = 350''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Grilled Chicken Breast", 350, "meat, bun, cheese", 3.45, "grilled-chicken-breast.png", NULL))


  
c.execute('''SELECT * FROM ALLFOOD WHERE name = "French Fries" AND calories = 200''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "French Fries", 200, "potatoes, oil", 0.95, "frenchfries.png", NULL))



c.execute('''SELECT * FROM ALLFOOD WHERE name = "Assorted Chips" AND calories = 250''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Assorted Chips", 250, "depends on chips", 0.75, "assorted-chips.png", NULL))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Cookies" AND calories = 250''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Cookies", 250, "", 0.50, "cookie.png", NULL))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Chicken Panini" AND calories = 350''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Chicken Panini", 350, "chicken, bread", 3.45, "chicken-panini.png", NULL))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Turkey Panini" AND calories = 375''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Turkey Panini", 375, "Smoked Turkey, Swiss Cheese, Tomatoes on Ciabatta Bread", 2.95, "turkey-panini.png", NULL))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Three Cheese Panini" AND calories = 350''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Three Cheese Panini", 350, "Provolone, Swiss & Pepper Jack Cheese on Focaccia Bread", 2.55, "three-cheese-panini.png", NULL))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Vegetarian Panini" AND calories = 300''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Vegetarian Panini", 300, "Fresh Mozzarella Cheese, Tomato, Fresh Basil on focaccia Bread", 2.70, "vegetarian-panini.png", NULL))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Vegetable Panini" AND calories = 300''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Vegetable Panini", 300, "Roasted Vegetables", 2.75, "vegetable-panini.jpg", "NULL"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Vegetable Quesadilla" AND calories = 350''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Vegetable Quesadilla", 350, "Grilled Vegetables, Cheddar & Mozzarella cheese served on Tortilla", 2.75, "vegetable-quesadilla.jpg", "NULL"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Chicken Quesadilla" AND calories = 450''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Chicken Quesadilla", 450, "Chicken Grilled Vegetables, Cheddar and Mozzarella Cheese served on Tortilla", 3.00, "chicken-quesadilla.png", "NULL"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Grilled Vegetarian Wrap" AND calories = 315''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Grilled Vegetarian Wrap", 315, "Grilled Vegetables on Grilled Tortilla", 2.20, "vegetarian-wrap.jpg", "NULL"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Grilled Wrap" AND calories = 400''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Grilled Wrap", 400, "Your choice of meat (specify in the comments) Vegetables on Grilled Tortilla", 3.45, "grilled-wrap.png", "NULL"))



#Monday
c.execute('''SELECT * FROM ALLFOOD WHERE name = "Beef Lasagna with Garlic Bread" AND calories = 600''')
counter = 0
for row in c:
 counter = counter + 1
if counter == 0:
 index = index + 1
 c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Beef Lasagna with Garlic Bread", 600, "Ground Beef, Tomato Sauce, Lasagna Noodles, Bread, Butter, Garlic", 3.95, "beef-lasagna.jpg", "2018-07-16"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Baked Cod Fish with Spicy Salsa" AND calories = 500''')
counter = 0
for row in c:
 counter = counter + 1
if counter == 0:
 index = index + 1
 c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Baked Cod Fish with Spicy Salsa", 500, "Cod, Butter, Salt, Pepper, Salsa, Jalapenos", 4.20, "baked-cod-salsa.jpg", "2018-07-16"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Vegetable Lasagna and Garlic Bread" AND calories = 500''')
counter = 0
for row in c:
 counter = counter + 1
if counter == 0:
 index = index + 1
 c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Vegetable Lasagna and Garlic Bread" , 500, "Assorted Vegetables, Lasagna noodles, White Cream Sauce, Garlic, Butter, Salt, Pepper", 2.95, "veg-lasagna.jpg", "2018-07-16"))

#Tuesday
c.execute('''SELECT * FROM ALLFOOD WHERE name = "Tandori Chicken with Naan" AND calories = 600''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Tandori Chicken with Naan", 600, "Chicken, Naan, Sugar, Salt, pepper", 3.95, "Tandori-Chicken.jpg", "2018-07-17"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Maryland Crab Cake with Cocktail Sauce" AND calories = 530''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Maryland Crab Cake with Cocktail Sauce", 530, "Crab, Flour, salt, cocktail sauce, sugar", 4.20, "Maryland-Crab-Cake.jpg", "2018-07-17"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Blackeye Peas over Rice" AND calories = 400''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Blackeye Peas over Rice", 400, "Blackeye pease, rice, flour, sugar", 3.45, "blackeye-rice.jpg", "2018-07-17"))

#Wednesday
c.execute('''SELECT * FROM ALLFOOD WHERE name = "Homemade Salvadorian Chicken Stew" AND calories = 420''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Homemade Salvadorian Chicken Stew", 420, "Chicken, water, spice, sugar, nuts", 3.95, "salvadorian-chicken-stew.jpg", "2018-07-18"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Seared Cajun Tilapia Fish" AND calories = 480''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Seared Cajun Tilapia Fish", 480, "Fish, Cajun spice, oil, water, herbs", 4.20, "Seared-Cajun-Tilapia-Fish.jpg", "2018-07-18"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Green Cabbage with Chick Pea Stew" AND calories = 420''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Green Cabbage with Chick Pea Stew", 420, "Green Cabbage, chick pea, water, sugar, salt", 2.95, "Cabbage-Chick-Pea-Stew.jpg", "2018-07-18"))

#Thursday
c.execute('''SELECT * FROM ALLFOOD WHERE name = "Chicken Tacos" AND calories = 400''')
counter = 0
for row in c:
 counter = counter + 1
if counter == 0:
 index = index + 1
 c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Chicken Tacos" , 400, "Grilled Chicken, Tortilla, Lettuce, Tomato, Salsa ", 3.95, "chicken-tacos.jpg", "2018-07-19"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Seared Swai Fish with Tomato & Spinach" AND calories = 500''')
counter = 0
for row in c:
 counter = counter + 1
if counter == 0:
 index = index + 1
 c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Seared Swai Fish with Tomato & Spinach" , 500, "Swai Fish, Tomatoes, Spinach", 4.20, "swai-fish-tomato-spinach.jpg", "2018-07-19"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Vegetable Tacos" AND calories = 450''')
counter = 0
for row in c:
 counter = counter + 1
if counter == 0:
 index = index + 1
 c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Vegetable Tacos" , 450, "Assorted Vegetables, Tortilla", 2.95, "veg-tacos.jpg", "2018-07-19"))

#Friday
c.execute('''SELECT * FROM ALLFOOD WHERE name = "Crispy Chicken Tenders" AND calories = 530''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Crispy Chicken Tenders", 530, "Chicken, flour, eggs, milk, black pepper, salt", 3.95, "Crispy-Chicken-Tenders.jpg", "2018-07-20"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Fish Taco" AND calories = 430''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Fish Taco", 430, "Fish, taco, salt, black pepper", 4.20, "Fish-Taco.jpg", "2018-07-20"))

c.execute('''SELECT * FROM ALLFOOD WHERE name = "Curried Vegetable over Rice" AND calories = 550''')
counter = 0
for row in c:
 counter = counter + 1
if counter == 0:
 index = index + 1
 c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Curried Vegetable over Rice" , 550, "Curry, Assorted Vegetables, Rice", 2.95, "curried-veg-rice.jpg", "2018-07-20"))


conn.commit()


#c.execute('''SELECT * FROM ALLFOOD WHERE date = "2018-07-16"''')
c.execute('''SELECT * FROM ALLFOOD''')
for row in c:
  print(row)
  print('****')

conn.close()

