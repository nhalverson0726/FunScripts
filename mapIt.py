#! python3
# mapIt.py takes command line arguments and looks them up in google maps to
# directions can be found for that address

import sys, webbrowser, pyperclip
if len(sys.argv) > 1:
    # GEt address from command line.
    address = ' '.join(sys.argv[1:])

# Get address from clipboard
else:
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)


