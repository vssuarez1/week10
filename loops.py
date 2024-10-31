# while loop = execute some code WHILE some condition remains true 

# name = input("Enter your name: ")

# # iteration = loop
# # iterate (verb) - looping over something

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ") #without this, it will be infinite 
# # infinite loops are bad
# else: 
#     print(f"Hello {name}")


# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")



# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")


# num = int(input("Enter a number between 1 - 10: "))
# while num <1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 1 - 10: "))

# print(f"Your number is {num}")







# for loops = execute a block of code a fixed number of times.
#              You can interate over a range, string, sequence, etc. 


# for x in reversed(range(1, 11, 3)):
#     print(x)

# print("Happy New Year")


# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)




# for x in range(1,21):
#     if x== 13:
#         break # or continue
#     else:
#         print(x)
 
    





# horror_characters = ["Freddy Krueger", "Jason Vorhees", "Michael Myers", "Pennywise", "Chucky"]


# for character in horror_characters:
#     # if character == "Jason Vorhees":
#     #     continue
#     # print(character)
#     if character == "Michael Myers":
#         character == "Dracula"
#     print(character)




horror_movies = ["Goosebumps", "Chucky", "Scream", "Halloween"]

for movie in horror_movies:
    if movie == "Chucky":
        break
    print(movie)


horror_movies[1] = "Terrifier"
print(horror_movies)






