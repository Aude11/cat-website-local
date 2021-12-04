# Caturday Website

## Overview

Dynamic and responsive website aiming to store picture of cats associated with their quote and their number of like and the date when it has been fetched from the cat API.
The Users can press a "like" button for each image. Then, the amount of likes received by each pictures is stored into the database.
All the image information (image url, date added to website, quote and number of likes) are saved into the MongoDB database.

The website works locally.

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

The archive page displays the cards stored containing the cat image with their date, quote and number of like. Depending on the screen view the maximal number of card displayed will vary. 
By scrolling down the user can access to the previous ou next page contiang the archiev image.
For each image

On the top of the home page, the user can click on the button "", if the current day is saturday the website
The last image



**Start the program**
```
python run.py
```

## Images

![Home Page](images/Home-page.png)

![Archive Page](images/Button.png)

![Home buttom Page](images/Log-page.png)

![Archive bottom Page](images/Setup-page.png)

![Archive bottom Page](images/Setup-page.png)

## ToDo

* Deploy website
* Unittest
* Test the website with Selenium