# NEWS HIHLIGHTS
This is a Python application that allows a user to view news sources and highlights around the world.

## BY William Mango https://github.com/mangowilliam/

## Description
This is a Python application that user can use to view diffrent sources of different categories of news around the world.
the users can also click on this sources and view the highlights of news provided by their source of choice
by clicking on the image of the highlight the user can read the news on the website

## user stories
* view sources
* click on a source and see articles
* click on article and read on their web
## BDD
| Behavior           | Input                 | Outcome                            |
| -------------------|-----------------------| -----------------------------------|
| request page       | horuku link url       | news sources                       |
| request highlights | click on source name  | news highlights/articles           |
| request article    | click on article url  | read article on the web            |

## Prerequisites
* Python3.6
## Setup/Installation Requirements
internet access
git clone https://github.com/mangowilliam/Password.git
$ cd news-highlights
$ python3.6 -m venv virtual (install virtual environment)
$ source virtual/bin/activate
$ python3.6 -m pip install -r requirements.txt (install all dependencies)
Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
$ ./start.sh
## Known Bugs

No known bugs

## Technologies Used
- Python3.6
flask botsrap
css
html 
## Support and contact details
contact williammango2015@gmail.com for any kind of support.
## Live Link
https://github.com/mangowilliam/Password

### License

The project is licensed under MIT license https://opensource.org/licenses/MIT
Copyright (c) 2019, mango
