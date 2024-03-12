"""#Repetition Statements
# Data types allowed to be iterated: Lists, Ranges, Sets, Tuple, Dictionaries, String

x = range(5,11)
petName = ["snowy","blacky","bruno"]

#for loop
#for (initialization; condition; incrementation/decre) - JAVA
for num in x:
    print(num)

#slicing a list
for name in petName[0:2]: 
    print(name) """
"""
#loop dictionaries
# key : value 
user = {
        "first_name" : "Johnny",
        "last_name" : "Tadea",
        "age" : 25,
        "average" : 81.76,
        "list_subjects" : ["Programming", "Mathematics", "English"]
}

# ctrl + / shrtct for comment

for key in user:
        print(key,":",user[key]) """
"""
#looping in dictionaries
list_of_users = [
    {
            "first_name" : "Johnny",
            "last_name" : "Tadea",
            "age" : 25,
            "average" : 81.76,
            "list_subjects" : ["Programming", "Mathematics", "English"]
    },
    {
            "first_name" : "Rose",
            "last_name" : "Tadea",
            "age" : 23,
            "average" : 82.54,
            "list_subjects" : ["Programming", "Mathematics", "English"]
    },
    {
            "first_name" : "Angel",
            "last_name" : "Tadea",
            "age" : 27,
            "average" : 86,
            "list_subjects" : ["Programming", "Mathematics", "English"]
    }
]
for key in list_of_users:
    for x in key:
        print(x,":",key[x])"""

#looping in reversed
x = range(1,11)
for i in x[::-1]:
    print(i)

