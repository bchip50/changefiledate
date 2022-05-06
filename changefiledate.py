
import PySimpleGUI as sg
from pathlib import Path
import filedate as fd
import dateutil.parser as dp

"""
Force the create date and modified date for all files in a single directory to a specified date.
Windows only
Two pop-up windows :
    Pick the folder to be changed. Press cancel to stop the process.
    After OK is pressed, then the next box appears.
    
    Pick the date to be used using a calendar widget.
        Press cancel to stop the program.
        Press OK to apply the change to all of the files in the folder.
"""
def newFileDate(filename: str, newdate: str) -> tuple:
    """ Change the create and modified date of the indicated file.
        Returns a list of the new dates associated with the file.
    """
    nd = dp.parse(newdate)
    fdates = fd.File(filename)
    fdates.set(created = nd, modified = nd)
    ndates = fd.File(filename).get()

    return ndates

def folderPopup() -> str:
    foldername = sg.popup_get_folder('Enter the directory you wish to process')
    return foldername

def folderFiles(folder) -> list:
    """ Return a list of all regular files in the folder given."""
    fldr = Path(folder)
    return ([x for x in fldr.iterdir() if x.is_file()])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sg.theme('BluePurple')

    targetFolder = folderPopup()
    if targetFolder == None:
        exit(0)

    files = folderFiles(targetFolder)

    ndate = sg.popup_get_date()
    if ndate == None:
        exit(0)

    for l in files:
        newFileDate(l, f"{ndate[2]}-{ndate[0]}-{ndate[1]}")
