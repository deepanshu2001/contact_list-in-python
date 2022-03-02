#This project is a contact book that is gonna save your contacts

import sys
class Contact_Book:
    def __init__(self,name):
        self.name=name 
    def N_name(self):
        print(f"Welcome to {self.name}'s contacts list") 

    def display_contacts(self):
        print("The available contacts in the dictionary are :")
        for key,value in dict.items():
            print(key+":"+str(value))

    def add_contact(self):
        name=input("Please enter contacts name!")
        no=int(input("Please enter the contacts phone no"))
        dict.update({name:no})
    def delete_contacts(self):
        Name=input(("Enter name of contact that you want to delete"))
        del dict[Name]
        print(f"The contact {Name} has been deleted!")
    
con=Contact_Book("deepanshu")
dict={"deepanshu":"9646580973","sharma":"889542455","pallavi":567890-0,"pavni":3456789876,"amrinder":34567890,"parvinder":23456789,"ryan":234567765}
if __name__=='__main__':
    while True:
        con.N_name()
        msg='''Please choose an option!
          1-display all the contacts
          2-add a contact
          3-delete a contact
          4-exit
        '''
        print(msg)
        option=int(input("Enter a option:"))

        if option==1:
            con.display_contacts()
        elif option==2:
            con.add_contact()
        elif option==3:
            con.delete_contacts()
        elif option==4:
            sys.exit()


    
