# Computer Security Course - Project, Presentation, Essay
## Password Authentication and MLS compartments

I initially started making the program in C as it coincided with what I was learning in Systems Programming. I ran into problems with input functionality and with my workload, I couldn’t justify sticking with my initial approach. I moved on to python where I ran into another hurdle pertaining to curses although I was really adamant in having my program run in a terminal. I ended up veering away from my application utilizing a terminal window and opted in for the python console. Looking online, it seemed at the time that there was only one security focus package being cryptography although I later found bcrypt which will be the package used for hashing and salting the inputs. 

My program starts by requiring a username and password to be authenticated to read and write files. I made a 2 dimensional array of username:password:clearance_level with the number being denoted as a numerical value to allow for BLP and Biba model functionality. Regarding the BLP and Biba model, it wasn’t specified whether or not to leave that to the user. In terms of class concepts, the MLS, BLP and Biba model mentioned above as well as hashing and salting. There wasn’t anything unique about design decisions made for this program although I wanted to do a lot more than I did. The program is fully functional and with little modification, could scale with more users and passwords. In terms of optimization, the program is rather wasteful in resources and I acknowledge that could have definitely been improved.

> Technologies Used
- Python, C (Initial Implementation)
- External Packages: N/A
