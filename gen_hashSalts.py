# Jerry A - CS492 Final Project - 05/04/2021

import os  # Imported the os for file access/manipulation
import re  # Regex functionality for limiting characters
import sys  # Used for sys.exit() for debugging
import bcrypt  # Hashing and salting


# Searching through an array to return the position passed
def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{} is not in list".format(repr(search)))


# User Group made of of: Username, Password, and Clearance Level
users = [["YaredSurendra", b"E6khLjYn", '0'],
         ["MelleBamidele", b"eukvx9QB", '0'],
         ["NairyosHeroides", b"uyvXENvV", '0'],
         ["AjayYiftachang", b"v2NdeP3V", '0'],
         ["FlaviusAlaattin", b"dd3JBAqs", '0'],
         ["YaredAvrumlos", b"Fh7kZLEy", '1'],
         ["DubhghallAtalyah", b"5Zh4FdeR", '1'],
         ["NoriKenzolosa", b"7jfMgUcx", '1'],
         ["SaburouTakumi", b"h3wZd9SR", '1'],
         ["YoshirouTooru", b"rVkfk8gA", '1'],
         ["ChrysesKastor", b"kNrCvWh6", '2'],
         ["HyakinthosErebos", b"bbNM5pkQ", '2'],
         ["ErosIapetoslos", b"mb4X2dkd", '2'],
         ["MenelaosDaidalos", b"zYe625Sc", '2'],
         ["ApollonNotosfos", b"vdxhVKpc", '2']
         ]
# Make copy of users where passwords are hashed and salted
users_hashed_salted = []
for row in users:
    form = []
    hashed = bcrypt.hashpw(row[1], bcrypt.gensalt())
    form = [row[0], hashed, row[2]]
    users_hashed_salted.append(form)


# Creating object of User made up of a username, password, and permission level (Clearance)
class User:
    def __init__(self, username, password, perm_level):
        self.perm_level = perm_level
        self.username = username
        self.password = password


# Declaring and initialization of compartments being Unclassified, Classified, and Top Secret
def compartment_level(arg):
    compartments = {
        0: "Unclassified",
        1: "Classified",
        2: "Top Secret",
    }
    return compartments.get(int(arg))


# Authorizing read and write permission based off the BLP and Biba Model
def files(subject_level, setting):
    entries_read = os.listdir('files/')
    entries_write = os.listdir('files/')
    entries = os.listdir('files/')
    file_permission = {
        0: entries[2],
        1: entries[0],
        2: entries[1],
    }
    if int(setting) == 0:
        if int(subject_level) == 0:
            entries_read.remove(file_permission[1])
            entries_read.remove(file_permission[2])
        if int(subject_level) == 1:
            entries_read.remove(file_permission[2])
            entries_write.remove(file_permission[0])
        if int(subject_level) == 2:
            entries_write.remove(file_permission[0])
            entries_write.remove(file_permission[1])
    if int(setting) == 1:
        if int(subject_level) == 0:
            entries_write.remove(file_permission[1])
            entries_write.remove(file_permission[2])
        if int(subject_level) == 1:
            entries_read.remove(file_permission[0])
            entries_write.remove(file_permission[2])
        if int(subject_level) == 2:
            entries_read.remove(file_permission[0])
            entries_read.remove(file_permission[1])
    file_array = [entries, entries_read, entries_write]
    return file_array


# BLP model, expecting an argument and calling files passing clearance level and model. Returning array of entries
def blp(lvl):
    return files(lvl, 0)


# BIBA model, expecting an argument and calling files passing clearance level and model. Return array of entries
def biba(lvl):
    return files(lvl, 1)


"""
    Starts by requiring a username and password for authentication. 
        (i.e U: SaburouTakumi P: h3wZd9SR)
    Requirements through main such as: Character Limit, Key limit
    Username is validated through comparing the username given in stdin with name in 'database'
    Func index_2d is utilized to get the position of an name:pass:level group. Objective, User, is created
    The instructions were vague with introducing a BLP or Biba model so I give the 'Users' options of what model
        to follow
    Given a 'Users' level, the 'User' is prompted with what files (stored locally) are available to read and write
"""


def main():
    while True:
        print("Username: ", end='')
        username = input()
        print("Password: ", end='')
        password = input()
        if len(username) > 20 or len(password) > 20:
            print("Error! 20 Character username or password maximum reached!")
            continue
        username_validation = [userN for userN in users if str(username) == str(userN[0]) in userN]
        position = index_2d(users, username)
        if users[position[0]][0] == username:
            position = index_2d(users_hashed_salted, username)
            if bcrypt.checkpw(password.encode('utf8'), users_hashed_salted[position[0]][1]):
                level = username_validation[0][2]
                session_user = User(username, password, level)
                break
            else:
                print("Wrong Password")
    clearance = compartment_level(level)
    print("Currently signed in as: " + session_user.username +
          "\nClearance Level: " + str(clearance) + " (" + str(level) + ")")
    print("Model Choice: \tBLP Model - 1 \tBiba's Model - 2")
    choice = input()
    if not re.match("^[1-2]*$", choice):
        print("Error! Only numbers 1 or 2 allowed!")
        sys.exit()
    elif len(choice) != 1:
        print("Error! One character expected")
        sys.exit()
    if int(choice) == 1:
        file_array = blp(level)
        print("Files available for read:\t" + str(file_array[1]))
        print("Files available for write:\t" + str(file_array[2]))
    if int(choice) == 2:
        file_array = biba(level)
        print("Files available for read:\t" + str(file_array[1]))
        print("Files available for write:\t" + str(file_array[2]))


main()
