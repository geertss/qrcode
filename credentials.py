__author__ = "Steven Geerts"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "Unlicensed"
__version__ = "1.0.0"
__maintainer__ = "Steven Geerts"
__status__ = "Development"

class credentials:
    """
        Initialisation of the object credentials
    """
    def __init__(self,name):
        self.name = name
        self.firstname = ""
        self.lastname = ""
        self.birthday = ""
        self.address = ""
        self.addressnumber = ""
        self.postcalcode = ""
        self.city = ""
        self.cellphonenumber = ""
        self.workcellphonenumber = ""
        self.homeemail= ""
        self.workemail = ""

    """
        returns the object in a string format
    """
    def __str__(self):
        return f" \
name = {self.name}\n\
firstname = {self.firstname}\n\
lastname = {self.lastname}\n\
birthday = {self.birthday}\n\
address = {self.address}\n\
cellphonenumber = {self.cellphonenumber}\n\
workcellphonenumber = {self.workcellphonenumber}\n\
homeemail = {self.homeemail}\n\
workemail = {self.workemail}\n\
        "

    # setter for the firstname
    def set_firstname(self,firstname):
        self.firstname = firstname

    # getter for the firstname
    def get_firstname(self):
        return self.firstname 

    # setter for the lastname
    def set_lastname(self,lastname):
        self.lastname = lastname

    # getter for the lastname
    def get_lastname(self):
        return self.lastname 

    # setter for the birthday
    def set_birthday(self,birthday):
        self.birthday = birthday

    # getter for the birthday
    def get_birthday(self):
        return self.birthday 

    # setter for the address
    def set_address(self,address):
        self.address = address

    # getter for the address
    def get_address(self,address):
        return self.address 

    # setter for the cellphonenumber
    def set_cellphonenumber(self,cellphonenumber):
        self.cellphonenumber = cellphonenumber

    # getter for the cellphonenumber
    def get_cellphonenumber(self):
        return self.cellphonenumber 

    # setter for the homeemail
    def set_homeemail(self,homeemail):
        self.homeemail = homeemail

    # getter for the homeemail
    def get_homeemail(self):
        return self.homeemail 

    """
        function to get all the data in the vcard format
        only support for 2.1 currently
        tested with an android phone only
    """
    def vcard(self):
        return f"\
BEGIN:VCARD\n\
VERSION:2.1\n\
N:{self.lastname};{self.firstname};;;\n\
FN:{self.name}\n\
TEL;CELL;PREF:{self.cellphonenumber}\n\
EMAIL;PREF;HOME;ENCODING=QUOTED-PRINTABLE:{self.homeemail}\n\
ADR;PREF;HOME:{self.address}\n\
BDAY:{self.birthday}\n\
END:VCARD\n\
"
