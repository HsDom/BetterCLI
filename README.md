<h1 align="center">Discord Recovery</h1>

## Installation
Installs the necessary libraries.
```py
pip install -r requirements.txt
```
Import the library inside the working file
```py
import bettercli
```
Alternatively 
```py
from bettercli import all
```

## Examples
Initate the Menu class
```py
#Create a new menu
#Colors: red, green, yellow, blue, magenta, cyan, white, black
Menu = Menu("Example Main Menu", "blue")
```
To create a button call add_button more elements can be found in the documentation
```py
def hello():
  print('hello world')

#Provide a title, and a function to call when the button is pressed
Menu.add_button("Say hello world", hello)
```

