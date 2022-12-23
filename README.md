# YaserAltaiy-CarMarket Project
### Final Project Harvard CS50 Course 
This project has been done to apply all features I learned from this course implementing HTML5, CSS, 
JavaScript(DOM) Python, and Database. Working on this project helps to learn a lot of new things that 
go into building a website.

The project video is: 

## Pages Build
* Register page
* Login Page 
* Home page
* Display page
* New Post page
* My Posts page
* CarWash page
* Watchlist page
* contact page

## Functionalities Added
* watch all posts
* search with details
* add to WatchList
* watch my posts
* serach for CarWashing locations
* add new CarWashing location
* comment on posts

## Tech Stack 
* HTML-5
* CSS
* JS-DOM
* LocalStorage
* Python (backend)
* Models (database)

## Distinctiveness and Complexity
he home page has a lot of features when we click on the user icon in the navbar , it will move us to login page.

from login page we can go to register page if we don't have account.

there is search box for searching about details in the posts we want.

any user can add new post and he is only how can delete it.

any user can write comment on the posts.

you can see all CarWashing locations near by you, and you can add new one if you have.

you can add the posts you want to WatchList or remove from WatchList.

user can contact us by sending a message.

In terms of complexity, I used Django with more than one model and javascript file to the frontend.

Moreover, all of the website is responsive to the different screen sizes (mainly mobile phones and computers).

The webite has been designed with figma, and the design then has been implemented with html, css, js, and bootstrap.

## Files information
* In views.py there is all of the backend code. The main functions are:
   - index with all the posts obtained from the database.
   - search for searching about details in the posts we want.
   - login, logout and register for user.
   - mypost for showing all my posts.
   - newpost to show newpost page.
   - save and removepost to post a new post or remove my post.
   - display to display the post.
   - watchlist, add and remove to see your watchlist, add to and remove.
   - comment to add comment on post.
   - getlocations to see all CarWashing location on map.
   - savelocation to add new location.
   - contact to contact the page admin.

* Models.py The different models are:
   - CustomUser
   - Category
   - Brand
   - Mileage
   - Model
   - Color
   - PostImages
   - Post
   - Location
   - Comment
   - Contact

* Templates for all of the different html pages
* CSS file for the theme and common clases.
* Other files like urls, admin, settings…

## How to run the application 
* Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
* Run the server by running python manage.py runserver
* Make sure to create a new superuser and fill the website content through admin dashboard