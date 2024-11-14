#M04 assignment exercise 11.1 and 11.2
#create a file called zoo.py, define a function called hours() that prints a string
#use interactive interpreter to import the zoo module and call its hours() function
#import the zoo module as menagerie and call its hours() function

with open ('zoo.py', 'w') as f:
    f.write("""
            def hours():
            print ('Opem 9-5 daily')
            """)
import zoo 
zoo.hours()
import zoo as menagerie
menagerie.hours()