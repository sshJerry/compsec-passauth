import os
import re
import sys
import bcrypt

users = [['YaredSurendra', b"E6khLjYn", '0'],
    ['MelleBamidele', b"eukvx9QB", '0'],
    ['NairyosHeroides', b"uyvXENvV", '0'],
    ['AjayYiftachang', b"v2NdeP3V", '0'],
    ['FlaviusAlaattin', b"dd3JBAqs", '0'],
    ['YaredAvrumlos', b"Fh7kZLEy", '1'],
    ['DubhghallAtalyah', b"5Zh4FdeR", '1'],
    ['NoriKenzolosa', b"7jfMgUcx", '1'],
    ['SaburouTakumi', b"h3wZd9SR", '1'],
    ['YoshirouTooru', b"rVkfk8gA", '1'],
    ['ChrysesKastor', b"kNrCvWh6", '2'],
    ['HyakinthosErebos', b"bbNM5pkQ", '2'],
    ['ErosIapetoslos', b"mb4X2dkd", '2'],
    ['MenelaosDaidalos', b"zYe625Sc", '2'],
    ['ApollonNotosfos', b"vdxhVKpc", '2']
]

users_hashed_salted = []
for row in users:
    form = []
    hashed = bcrypt.hashpw(row[1], bcrypt.gensalt())
    form = [row[0], hashed, row[2]]
    users_hashed_salted.append(form)


class Class:
    def __init__(self, username, password, perm_level):
        self.perm_level = perm_level
        self.username = username
        self.password = password


def compartment_level(arg):
    compartments = {
        0: "Unclassified",
        1: "Classified",
        2: "Top Secret",
    }
    return compartments.get(int(arg))


def files(subject_level, setting):
    # ['classified.txt', 'topsecret.txt', 'unclassified.txt']
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


def blp(lvl):
    return files(lvl, 0)


def biba(lvl):
    return files(lvl, 1)


def main():
    while True:
        print("Username: ", end='')
        username = input()
        print("Password: ", end='')
        password = input()
        if len(username) > 20 or len(password) > 20:
            print("Error! 20 Character username or password maximum reached!")
            continue

        try:
            tempUsernameValidation = [userN for userN in users if username == str(userN[0]) in userN]
            tempPasswordValidation = [passW for passW in users if password == str(passW[1]) in passW]
            if str(tempPasswordValidation) == str(tempUsernameValidation) \
                    and tempPasswordValidation[0][2] == tempUsernameValidation[0][2]:
                level = tempUsernameValidation[0][2]
                session_user = Class(username, password, level)
                break
        except IndexError:
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
