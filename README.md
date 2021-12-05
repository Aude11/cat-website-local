# Caturday Website

## Overview

Dynamic and responsive website aiming to store cat's card. Each saturday, the users has the ability to generate a new card. A card contains a picture of a cat associated with a quote and a number of like that the card has received and the date when the card has been added to the website collection.
All the card information (image url, date added to website, quote and number of likes) are saved into the MongoDB database.
The users can press a "like" button for each image. Then, the new amount of likes is updated into the database.

The website works currently locally. The deployment of the website is in progress.

## Technologies

* Front-end :
  * HTML
  * CSS
  * Javascript
  * Boostrap - version 5.0

* Back-end :
  * Python - version 3.8
  * Flask

* DataBase:
  * MongoDB - version 4.4.5

* API:
  * [Cat API](https://api.thecatapi.com/)
  * [Quote ZEN API](https://zenquotes.io/api/random

## Usage

On the home page, scroll down and click either on the button next to feeling hungry section to get a meal. Or if you are feeling thirsty, click on the button next to this section.

On the homepage, the button "" allows user to generated a new cat's card

The archive page displays the cards stored containing the cat's image with its added date, quote and number of like. Depending on the screen view the maximal number of card displayed per page will vary. 
The pagination button views for navigating through pages are at the bottom of each achieve pages.


By scrolling down the user can access to the previous ou next page contiang the archive image.
For each image
the pagination button views for navigating through pages
On the top of the home page, the user can click on the button "", if the current day is saturday the website
The last image



**Start the program**
```
python run.py
```

## Images

![Home Page](images/Home_page_top.png)

![Card Example Home Page](images/card.png)

![Archive Top Page](images/Archive_top_page.png)

![Archive bottom Page](images/Archive_bottom_page.png)

![Archive Last Page](images/Archive.png)

![Archive Page on small screen](images/small_screen.png)

## ToDo

* Deploy website
* Unittest
* Test the website with Selenium