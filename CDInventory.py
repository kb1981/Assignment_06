#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KBrock, 2021-Feb-20, updated code to use functions
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# -- PROCESSING -- #
class DataProcessor:      # TODO add functions for processing here
    """Processing the data in list of dictionares"""

    @staticmethod
    def add_cd(ID, Title, Artist):
        """The add_cd() function is adding a new CD to the dictionary

        Args:
            ID: Number assigned to the CD
            Title: Name of the CD album
            Artist: Name of the CD musician

        Returns:
            dictCD: entry to append to the list of dictionaries
        """
        dictCD = {'ID': ID, 'Title': Title, 'Artist': Artist}
        return dictCD

    @staticmethod
    def delete_cd(ID, table):
        """The delete_cd() function is deleting a CD from the list

        Arg:
            ID:  ID of the CD that the user selected
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
            
        Returns:
            Table: Returns updated List of Dictionaries value to the loop
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == ID:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
            print('Here is your updated Inventory:\n')
        else:
            print('Could not find this CD!\n')
        return table

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries
        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table):
        """The write_file function writes the current CD inventory to a text file

        Args: 
            file_name (string): name of file used to read the data from
            table(list of dict): 2D data structure (list of dicts) that holds the data during runtime
            
        Returns:
            None.
        """
        objFile = open(file_name, 'w')
        for row in table:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        print('Your Inventory has been saved!')


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Please choose from: [l, a, i, d, s or x]: ').lower().strip()
        print()
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================\n')

    @staticmethod
    def cd_intake():
        """Gets information from user for CD input

        Args:
            None.

        Returns:
            ID: ID assigned by user to the CD
            Title: Title of CD input by user
            Artist: Artist of CD input by user
        """
        ID = input('Enter ID: ').strip()
        Title = input('What is the CD\'s title? ').strip()
        Artist = input('What is the Artist\'s name? ').strip()
        print()
        return ID, Title, Artist

print('\nWelcome to the Magic CD Inventory!\n') 
FileProcessor.read_file(strFileName, lstTbl)

while True:
    IO.print_menu()  #Display Menu to user and get choice
    strChoice = IO.menu_choice()

    if strChoice == 'x':  #Selection 'x' exits the program
        print ('"CD" ya later! Bye!')
        break

    if strChoice == 'l':  #Selection 'l' loads the CD Inventory from CDInventory.txt
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:  ')
        if strYesNo.lower() == 'yes':
            print('reloading...\n')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.\n')
            IO.show_inventory(lstTbl)
        continue

    elif strChoice == 'a':  #Selection 'a' allows user to add a CD to inventory list
        strID, strTitle, strArtist = IO.cd_intake()
        intID = int(strID)
        dicRow = DataProcessor.add_cd(intID, strTitle, strArtist)
        lstTbl.append(dicRow)
        IO.show_inventory(lstTbl)
        continue

    elif strChoice == 'i':  #Selection 'i' displays the current inventory in the list
        IO.show_inventory(lstTbl)
        continue

    elif strChoice == 'd':  #Selection 'd' deletes a CD from the inventory list
        IO.show_inventory(lstTbl)
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        DataProcessor.delete_cd(intIDDel, lstTbl)
        IO.show_inventory(lstTbl)

    elif strChoice == 's':  #Selection 's' saves the current CD Inventory list to a text file
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue

    else:
        print("You've fa la la la lost me ...")




