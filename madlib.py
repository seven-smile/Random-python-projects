# say we want to create a string that says, " My name is _______"
#in the variable say
#name = "Nana"# a string which would store your name in the name variable
#few ways to do would be to ...
# 1. by using a concartinator.that is 
#print("My name is " + name)
# 2. using the .format option, which puts whatever value is in the name variable in to the curly backets of the .format option
#print("My name is {}".format(name))
# 3. using an F string, where we prepend a string with f and in it's curly brackets directly add the variable name.
#print(f"My name is {name}")


#please note that the use of <input> is to ask for user inputs instead of hard coding. 

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("verb: ")
famous_person = input("Famous person: ")


madlib = f"Computer programing is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"


print(madlib)
