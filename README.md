# search it
## About
Did you ever wish you could use a search function on a webpage without opening the page? Well this little python doodle hopes to help you with that.
## How-to
* It can be used by passing the website address(youtube.com for example) and desired to the python program. 
The form looks like this: 
```
python searchit.py [website] [search]
```
* For example running "python search-it.py youtube.com linux" would search youtube for linux.
## Required python dependencies
* Beautiful soup 4 and requests
## Features
* After it makes a search on a desired webpage it can also memorize it with an easier to use name of your choosing. For example instead of typing duckduckgo.com you could just type duck which makes it easier and quicker to use.
* It can also be used with the provided bash script in the terminal with the command browse. It uses the same form as the python program so it should be intuitive to use.
* Webpages can be manually modified/added to stored.txt
## Planned QOL CHANGES
* ~~Providing all python dependencies~~
* cleaning up the code
* making a linux/windows installer(installable by pip but full installer soon!)
* ~~searching unscrapable pages by providing the search url example~~
* gui with pyqt
* gui in system tray
* ~~add an __init__ file and move the functions to the seperate file~~
