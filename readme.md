# Order Manager
This is project is a Customer/Order Management tool.
It allows for visitors to view the status of order and customer.
Logged in users can create, edit, and delete records.
Admins (or superusers) can view all the users, as well as create more.

## Take a Tour
A running example of this site can be found at [https://calm-plateau-71855.herokuapp.com/]
Here try looking at the records displayed on the main page. then take a look at the side bar to view a dashboard for more specif types of orders. Try out the search bar!

Now log in as:

> user: user1
> pass: pass1111

Where the login drop down was, you can now logout or change the password (please don't :) ). you can also create a new customer (make sure to check needs follow up to see them on the home page). One the customer is created, go to their page either from the home screen or by searching. Here you will be able to create order for the customer, they start as quotes, but you can edit them to make them full fledged orders.
Once you are done, log out and log back in as:

> user: admin
> pass: super1111

One you have logged in as an Admin, you will notice a new sidebar item, this is where you can view, edit, and create new users. Create a users account for yourself, to add things like name and email, you will also need to edit the account. After that you can log in as your account!


## Design
This project follows the proposal closely, with a few exceptions, the point of this project was to practice reusability, and abstraction. To this end I created various level of abstraction between the controllers and the data, I knowingly broke the YAGNI (you ain't gonna need it) principle, so I could practice a more hearty design. I had hoped to create a restful API that could access this data as well, but realized too late that Django Rest Framework is another beast unto itself, but since the data is abstracted it will be easy to add later. This tool is also minimally invasive to day-to-day process, as was also a goal.

## Technology used
Python
Django
Google Icons and Fonts
[Material UI](https://daemonite.github.io/material/)

## Structure

There are three apps in this project

 - backend - common resources, the bulk of the project
 - web - the app for the html web interface - mostly urls and views
 - api - the urls and views for the restful service (COMING SOON)

Inside of backend there are packages for forms and models similar to the files django sets up

There is also:

 - service - these represent the set of data that represents the business process, these are accesed from the views.
 - repositories - a way to abstract the models one step further in case a different ORM is used at some point, these are accessed from the services.
