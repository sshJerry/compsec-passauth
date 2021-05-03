from cryptography.fernet import Fernet, MultiFernet
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import re, sys

"""
unclass passes:     E6khLjYn eukvx9QB uyvXENvV v2NdeP3V dd3JBAqs
class passes:       Fh7kZLEy 5Zh4FdeR 7jfMgUcx h3wZd9SR rVkfk8gA
topsecre passes:    kNrCvWh6 bbNM5pkQ mb4X2dkd zYe625Sc vdxhVKpc
"""

# Create Groups i.e TOPSECRET{CS492}, CLASSIFIED{CS492,CS1})
# BLP or BIBA Option (IN CS 492 Lec017 Authorization II - ACLCapabilities S19.pdf LECTURE)
# THEN salt and hash passwords after functionality
unclassifiedUsers = [
    ['YaredSurendra', 'E6khLjYn', '0'],
    ['MelleBamidele', 'eukvx9QB', '0'],
    ['NairyosHeroides', 'uyvXENvV', '0'],
    ['AjayYiftachang', 'v2NdeP3V', '0'],
    ['FlaviusAlaattin', 'dd3JBAqs', '0']
]
classifiedUsers = [
    ['YaredAvrumlos', 'Fh7kZLEy', '1'],
    ['DubhghallAtalyah', '5Zh4FdeR', '1'],
    ['NoriKenzolosa', '7jfMgUcx', '1'],
    ['SaburouTakumi', 'h3wZd9SR', '1'],
    ['YoshirouTooru', 'rVkfk8gA', '1']
]
topSecretUsers = [
    ['ChrysesKastor', 'kNrCvWh6', '2'],
    ['HyakinthosErebos', 'bbNM5pkQ', '2'],
    ['ErosIapetoslos', 'mb4X2dkd', '2'],
    ['MenelaosDaidalos', 'zYe625Sc', '2'],
    ['ApollonNotosfos', 'vdxhVKpc', '2']
]

"""
for row in unclassifiedUsers:
    print("Names: " + str(row[0]) + "\t\t" + "Pass: " + str(row[1]) + "\t\t" + "Priority: " + str(row[2]))
    # f.write("Names: " + str(row[0]) + "\t\t" + "Pass: " + str(row[1]) + "\t\t" + "Priority: " + str(row[2]))

print("\n")

for row in classifiedUsers:
    print("Names: " + str(row[0]) + "\t\t" + "Pass: " + str(row[1]) + "\t\t" + "Priority: " + str(row[2]))
    # f.write("Names: " + str(row[0]) + "\t\t" + "Pass: " + str(row[1]) + "\t\t" + "Priority: " + str(row[2]))

print("\n")

for row in topSecretUsers:
    print("Names: " + str(row[0]) + "\t\t" + "Pass: " + str(row[1]) + "\t\t" + "Priority: " + str(row[2]))
    # f.write("Names: " + str(row[0]) + "\t\t" + "Pass: " + str(row[1]) + "\t\t" + "Priority: " + str(row[2]))

with open('unclassified.txt', 'w') as f:
    pass
with open('classified.txt', 'w') as f:
    pass
with open('topsecret.txt', 'w') as f:
    pass
"""

AllUsers = [
    ['YaredSurendra', 'E6khLjYn', '0'],
    ['MelleBamidele', 'eukvx9QB', '0'],
    ['NairyosHeroides', 'uyvXENvV', '0'],
    ['AjayYiftachang', 'v2NdeP3V', '0'],
    ['FlaviusAlaattin', 'dd3JBAqs', '0'],
    ['YaredAvrumlos', 'Fh7kZLEy', '1'],
    ['DubhghallAtalyah', '5Zh4FdeR', '1'],
    ['NoriKenzolosa', '7jfMgUcx', '1'],
    ['SaburouTakumi', 'h3wZd9SR', '1'],
    ['YoshirouTooru', 'rVkfk8gA', '1'],
    ['ChrysesKastor', 'kNrCvWh6', '2'],
    ['HyakinthosErebos', 'bbNM5pkQ', '2'],
    ['ErosIapetoslos', 'mb4X2dkd', '2'],
    ['MenelaosDaidalos', 'zYe625Sc', '2'],
    ['ApollonNotosfos', 'vdxhVKpc', '2']
]


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
            tempUsernameValidation = [userN for userN in AllUsers if username == str(userN[0]) in userN]
            tempPasswordValidation = [passW for passW in AllUsers if password == str(passW[1]) in passW]
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


main()
