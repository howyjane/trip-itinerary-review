       ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!
# Trip Itineraries and reviews

# 3nd Coding Project:  Code Institute 

This is my 3rd coding project. In this project I created a CRUD website for users to post their travel reviews.
This website caters to anyone who wish to share their travel itineraries and reviews. Any users can use the website to search or post a trip review. They can also make edits to their trip reviews.
This is a responsive website and the design is simple and easy to use. At the same time, the tools that I have created will respond to the user’s actions and displays information based on users requests.


## Project Strategy and Scope

The key intention of this project is to create a CRUD project linking mongodb database to display data on the website and users can create, read, update and delete records from the website.
As part of the design process, I have saved the wireframes in folder: ‘imagewireframes’. To view the jpg images, please change size view to 20%.
There is no ER diagram for this project mainly because I am using mongodb instead of mysql . Mongodb creates a unique object ID for each record in my collection and the fields are link to the object ID.


The key intention of this website is to attract users who are planning for their next holiday and for those who had travelled to any countries, they can utilise the platform to share their experiences to members of the public. 
### User Stories

| User Stories        | Description           | Features to implement  |
| :------------- |:-------------| :-----|
| 1      | User would like to see the latest game trailer. | To include the video game trailer on the website.  |
| 2      | User would like to know more about the game. | To include an about section that gives more information about the game.  |
| 3      | User would like to see the various gameplay features in the game. | To include more information on the gameplay features in the game.  |
| 4      | User would like to purchase the game. | To include a buy now section that leads them to the official purchase page.  |
| 5      | User would like to purchase the game in either console or pc. | To include a buy now section that leads them to the official purchase page of both console (PS4/XBOX) and PC (STEAM).  |
| 6      | User would like to subscribe to the latest news and updates about the game. | To include a section in the buy now page that lets them enter their email and "subscribe".  |

## Project Structure
###(i)Overview
- Homepage - The homepage has a short, muted, autoplay video that features the gameplay. Below that, there is a short description of the game. There is also a logo on the top right-hand side of the website and a collapsable navigation bar on the right-hand side of the website. 

- About Game - The about section includes more information about the game. There is a short description about the game, its features and there is also a gallery of images.

- Buy Now - The buy now page includes links to the official PC and Console purchase pages. There is also a parallax image in the background and a sticky social media bar on the side of the page. 

###(ii) Wireframes here.

Save your wireframe in a pdf document. Upload to google drive. Get a shareable link. Put it here.

## Project Skeleton
### (i) Existing Features
- Homepage
The muted, autoplay video gives users a peek into the gameplay. Additionally, the short introduction of the game gives users a little more detail about the game. The logo on the top-left hand corner also lets users know that they have come to the right website. Additionally, it makes the website more credible. There is a collapsable navigation bar on the top-right hand corner of the homepage. This was placed to give users an easier access to navigate the different pages easily and quickly. 

- About
Bootstrap features like cards were used to explain the various features of the gameplay. Another Bootstrap feature that was used in the about page was the carousel images, to showcase the screenshots taken from the game. The image under the Expansion Pack section is a link to the official video game page, which gives more information. 

- Buy Now
In the buy now page, users can visit the official social media sites to learn more about the game 
and connect with the game community. Apart from that they will be able to purchase the game in the platform of their choice. At the bottom of the page, users will be able to input their email address and subscribe to the latest news and updates.

### (ii) Features to implement in the future
In the future, I would like to include more information about the expansion packs and the 
season pass so as to give users more of a choice when it comes to what they want to buy. 

In the about page, I would like to have more images and information about the different characters in the game. I also think including a buy now button will increase and drive sales.

I would also like to include more interactive elements in the buy now page that would achieve the end goal of persuading users to buy the game. These interactive elements could be in the form of image hover overlay, an animated buy now button, etc. 

###Limitation 
There is also a subscription form at the bottom of the page,
although clicking on the submit button will not navigate away from the website. (There is no Javascript). This would be a feature to implement in the future.

## Project Surface
### Design Choices
(i) The color scheme of orange and black reflects the main theme of the overall game and hence why it is consistently used throughout the website. I also believe that the colour scheme will appeal to users.
(ii) The font looks fun and appeals to gamers. It also reflects the game and the gameplay.
(iii) A scrollable parallax image was included in the buy now page to give the webpage more depth. I also believe the juxtaposition of the image and the subscription form will enable and encourage users to buy and subscribe to the game. An active subscription is equally important as a purchase as it measures the individual's interest level and allows developers to push more news and updates to their email so as to attain the goal of a purchase if the user has not already bought the game. 

## Technologies

1. HTML (link to the documentation: https://devdocs.io/html/)
HTML was used to structure the content of the website.
2. CSS (link to the documentation: https://devdocs.io/css/)
CSS was used to style the website.
3. Bootstrap (link to the documentation: https://getbootstrap.com)
4. Javascript — for country dropdown. (link to the documentation: https://devdocs.io/jsdoc/)

## Testing
(i) Mobile Responsiveness

This site was tested across multiple devices multiple mobile devices 
(iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness.)

- Screenshots of your test: --insert links---
Website tested on mobile and on laptop mode.

(ii) Browser Compatability

This site was tested across multiple devices multiple mobile devices 
(iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness.)

(iii) Additionally, parallax scrolling has been turned off for phones, as soon as the breakpoint hits min-device-width: 300px.

(iv) Under the subscription section, users will get a prompt in red if their email has not been entered in the correct format.

(v) Test Cases 

| Test Case(s)        | Description           | Outcome |
| :------------- |:-------------| :-----|
| 1      | When user clicks on home link on the top-right navigation bar, the website redirects to the home page. | Pass  |
| 2      | When user clicks on about link on the top-right navigation bar, the website redirects to the about page. | Pass  |
| 3      | When user clicks on home link on the top-right navigation bar, the website redirects to the buy now page. | Pass  |
| 4      | User should see 3 buttons at the top corner of the navigation bar. | Pass  |
| 5      | When user clicks on the linkable image under the Expansion Pack section in the about page, he/she will be directed to the official page which gives the user more information. | Pass  |
| 6      | When user clicks on the linkable platforms (Steam, PS4, Xbox) in the buy now page, he/she will be directed to the official purchase page for each of the different platforms. | Pass  |
| 7      |When user enters their email address in the wrong format, they will be prompted in red to re-type their email address. | Pass  |
| 8      |All links in the website will open in a new tab using 'target="_blank"' | Pass  |

## Bugs Discovered
// Any bugs that you've discovered and has yet to be fixed.

### Media 

All photos and video were taken from the game via screenshots and screen recordings.
All rights go to Techland, the game developer and publisher. 

### Acknowledgements

W3Schools:

1. Used an overlay for the navigation bar W3Schools: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_overlay
2. Used a sticky social bar from W3Schools: https://www.w3schools.com/howto/howto_css_sticky_social_bar.asp

Bootstrap features: 

1. Used cards for the about page of the website : https://getbootstrap.com/docs/4.3/components/card/
2. Used carousel for the about page of the website: https://getbootstrap.com/docs/4.3/components/carousel/
3. Used form for the subscription section in the buy now page: https://getbootstrap.com/docs/4.3/components/forms/#overview

Fonts:

https://fonts.google.com.