# ------------------------------------
# Loops through available drives and returns 
# the drive letter if one matches the given
# drive name. If none match, return 0.
# Ideal for checking if a specific USB 
# drive is mounted. 
#
# David Metcalfe, January 19, 2020
# ------------------------------------

import win32api

def get_drive_by_name(name: str):
    '''Loop through potential drives on system and return 
    the letter if one matches the provided name.'''
    drive_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in drive_letters:
        
        drive_path = "{}:\\".format(i) # Format drive path so win32api will accept it.
        try:
            if win32api.GetVolumeInformation(drive_path)[0] == name:
                return i
        except:
            continue
    return 0
