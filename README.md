# Golden Coin

**Developer: Igor Vasiljev**

[Link to the live project](https://goldencoin.herokuapp.com/)

![logo](media/all-devices-black.png)

## About

The app represents a store which offers to buy coins of different makes, substantially made from gold, silver and bronze. There is also form for sending offers to sell coins.
Admin privileges include adding, removing and modifying coins data.

## Table of Contents

  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Structure](#structure)
    - [Database](#database)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries and Tools](#libraries-and-tools)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)

## Project Goals

### User Goals

- Ability to buy coins when authorized or anonymously.
- Save and update profile data.
- Access order history.
- Offer coins to sell.
- Use the contact form.
- Subscribe for mailing list.

### Site Owner Goals

- To be able to keep track of all orders.
- Add/remove or modify coins data.
- Track offers to sell coins.
- Track contact form enquiries.
- Retain clients by using mailing system.

## User Experience

### Target Audience

- Those who are interested in numismatics.
- Who is looking to sell their coins.
- Who is looking for making investement in precious metals.

### User Requirements and Expectations

- Intuitive navigation.
- Responsive design.
- Exhaustive information about the store items.
- Easy way to add/remove items from cart and checkout.
- Checkout anonymously.
- Access information to previous orders.

## User Stories

### Users

1. As a user I can access the home page so that general site information and navigation can be viewed.
2. As a user I can use navigation links and search bar so that site pages and search results can be viewed.
3. As a user I can view the footer so that social media and contact forms can be accessed
4. As a user I can access all coins link so that all available coins can be viewed.
5. As a user I can use filter coins so that different categories of coins can be grouped on the same view.
6. As a user I can view coins as badges on the coins page so that all relevant each coin's information and price can be viewed.
7. As a user I can preview each coin so that coins's information can be viewed
8. As a user I can use coin ordering so that coins can be sorted by price, origin, condition, name and era.
9. As a user I can open the cart so that cart contents can be viewed and modified.
10. As a user I can add coins to cart so that coins are added to cart and overall price is visible.
11. As a user I can access the checkout page so that delivery and payment information can be entered to process the purchase.
12. As a user I can complete the order so that order is confirmed and order number is available.
13. As a user I can access the coin sell form so that the form can be populated with the coin offer.
14. As a user I can submit the contact form so that site owners can be contacted.
15. As a user I can access profile page so that delivery information can be added/amended and order history can be viewed.
16. As a user I can access Sign Up menu so that it's possible to create an account.
17. As a user I can access the login menu so that it's possible to log in to the site.

### Site Owner

18. As a admin I can access coins management so that new coins can be added to the store.
19. As a admin I can access coin edit page so that coin information can be modified or deleted.

[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Structure

The app has the following structure: navigation bar on top, footer on bottom - visible across all app pages, and the content/functionality are in between.

Common app's pages:
- Home: logo and link to explore the store items.
- Coins: list of all coins available in the store with relevant information.
- Coin details: detailed coin information and add to cart button.
- Cart: coins added to cart, price and delivery information.
- Checkout: checkout form, items information and total price.
- Checkout success: summary of order with the tracking number.
- My Profile: delivery information form and order history.
- Order history: information about the item ordered in past.
- Sell coins: form to offer coins to sell.
- Contact: contact form.
- Sign Up: sign up input fields.
- Pages 400, 403, 404, 500

Admin only pages:
- Edit coin: coin information with ability to modify it.
- Coins Management: form to add a new coin to the store.