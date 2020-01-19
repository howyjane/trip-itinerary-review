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

# 3nd Coding Project:  Code Institute Data Centric Development Milestone Project 

This is my 3rd coding project. In this project I created a CRUD website for users to post their travel reviews.
This website caters to anyone who wish to share their travel itineraries and reviews. Any users can use the website to search or post a trip review. They can also make edits to their trip reviews.
This is a responsive website and the design is simple and easy to use. At the same time, the tools that I have created will respond to the user’s actions and displays information based on users’ requests.


## Project Strategy and Scope

The key intention of this project is to create a CRUD project linking mongodb database to display user data on the website and any users can create, read, update and delete records from the website.
As part of the design process, I have saved the wireframes in folder: /static/imagewireframes. To view the jpg images, please change size view to 20%.

There is no ER diagram for this project because I use Mongodb instead of mysql . Mongodb creates a unique object ID for each record in my collection and all input fields are link to the object ID.

### User Stories

The key intention of this website is to attract users who are planning for their next holiday and for those who had visited to any countries, they can utilise the platform to share their experiences to members of the public. 
This is an informative website and users can find useful information when they search through each travel review. They can check out recommended attractions in each country and what is the estimated cost of trip based on total length of trip 


## Project Structure
###(i)Overview

Based on above project strategy, I identified the following requirements:
1) The website must provide users with ease of navigation and displays information that is clear and easy to read.

2) Content Requirements

The website includes a simple landing page that displays the latest trip reviews posted by users (sorted by latest post).  Users can either scroll down the landing page for all the reviews or they can search for the entries via a search link.

The website pages included:

## Create

1. Add Trip - A page that contains an “add journey” form where users can input information according to each field and add their            reviews on the website.

## Read

1. Tripee.com – Introduction Landing Page shows all travel reviews. Users can click into each review for more details.

2. Search Trip - A page that contains 4 search dropdowns where users can search through the website for trip information.

## Update

1. Users can access the website to edit the trips that they posted.

2. From the landing page, users can click on ‘Click for Trip Details!” under each trip review posted on the landing page and click on      ‘Edit Trip’ to update trip information or 

3. From the Search Trip page, users can select a trip review via “Search Trip” link on the navigation bar to search for a trip and on      the search results page, they can click on ‘View Trip” and click on ‘Edit Trip’ to update trip information.

## Delete

1. Users can access the website to delete the trips that they posted.

2. From the landing page, users can click on ‘Click for Trip Details!” under each trip review posted on the landing page and click on      ‘Delete Trip’ to delete trip review or 

3. From the Search Trip page, users can select a trip review via “Search Trip” link on the navigation bar to search for a trip and on      the search results page, they can click on ‘View Trip” and click on ‘Delete Trip’ to delete trip review.

## Skeleton

As part of the design process, I saved the wireframes in folder/static/imagewireframes. To view the jpg images, please change size view to 20%.

## Surface

1. Colors:

The main colors used are grey, black, purple and white since it is an information website.

2. Background Images

Performing an image search for globe led me to use the background image in my website.

3. Typeface

Throughout the site I used font types: Arial and Courier 

4. Interactions

Created a simple form for users to input their travel information and included easy to use dropdown country list and trip category list. As well as users can use the number arrow ‘updown’ selectors when they input the ratings, length of trip instead of typing the figures.
Users will be prompted to upload a profile image (required) during add /edit of reviews. 

###(ii) Wireframes

As part of the design process, I saved the wireframes in folder/static/imagewireframes. To view the jpg images, please change size view to 20%.

## Project Skeleton
### (i) Existing Features

1. Users can easily create a new record or edit an existing by completing a simple to use form. 
2. Created country dropdown list and number selectors for users to use in each form.
3. Created easy navigation for users to locate each record and link the edit and delete function on each trip record page.
4. Users can also upload a new trip profile image that best represents each trip review. 
5. All pages have been written with semantic HTML in mind.
6. Fixed Scroll to Top: Each page has a fixed scroll to top, for ease of navigation.
7. Responsive Design: Site pages are designed to work on all sizes of device.

### (ii) Features to implement in the future
In future,

1. To include a bootstrap datepicker and calendar for users to indicate start and end date of trip. 
2. To change file upload as an optional requirement instead. So users are not required to upload image for each addition/edit.
3. Users can source for trip based on trip budget and using an api to source for external trip providers.

## Technologies

In this project the following technologies have been used:
1.  Mongodb
2.  Accessing countries names selector using https://restcountries.eu/rest/v2/all API
3.  Javascript
4.  Bootstrap 4
5.  HTML
6.  CSS
7.  Flask
8.  Python
9.  Django
10. jQuery
11. Inline html styling

## Testing

Throughout this project I have done regular testing and reloaded the pages many times after each addition and modification on cloud 9 and Heroku.

1. To test the functionality and usability of the site, I did a class presentation. 

Their feedback was the website needed more images and to include a country selector instead of user typing each country visited manually. This is to avoid duplication of countries being shown in dropdown list.

2. I tested the compatibility of my site by viewing the website on my phone to check responsive settings.

3. Testing the navigation links to ensure the pages are linked.

## Search function

Tests were carried out for each search tool ensuring that the search results display the correct results.

At the start, the search filter didn’t work as it displayed all information from the database. But it was rectified after placing conditions in the app.py for each filter.

## Add/Update function

Created several dummy records to add/update via website. For each new records/edits, I need to make that the fields are updated according to each object ID on Mongodb collection . 

Making sure that there are no flask or jinja errors. At the start of the testing, I received many errors hence I needed to change the jinja syntax in each html and also changed the routes on app.py.

Uploading files created many issues. I received server error after I deploy to Heroku, It got fixed after changing the configuration of cloud9 Ubuntu.

## Deployment

The site has been deployed using github and Heroku:

The app live at :

https://howyjane.github.io/trip_itinerary_review

https://howytripee.herokuapp.com/ 


### Media 

Content & Media All content on this site is taken from https://restcountries.eu/rest/v2/all through the use of APIs, Tripadvisor and Triphobo for recommended attractions and reviews.

All copyrights of images and text belong to their respective owners.

1. Website layout:
https://startbootstrap.com/templates/heroic-features/

2. Rest countries API documentation links:
https://restcountries.eu/rest/v2/all
https://restcountries.eu/#api-endpoints-all

3. Background Image:
https://bitcoinist.com/wp-content/uploads/2019/09/shutterstock_703229845.jpg
       
4. Trip Review Pictures URL:

https://cdn.thecrazytourist.com/wp-content/uploads/2019/04/ccimage-shutterstock_520182697.jpg
https://loveincorporated.blob.core.windows.net/contentimages/fullsize/1751dc80-2a64-4593-8a56-bd75502fb470-lead-image-osaka-2.jpg
https://www.nationalgeographic.com/content/dam/travel/Guide-Pages/asia/tokyo_travel.adapt.1900.1.jpg
https://www.jnto.go.jp/ph/spot-activity/wp-content/uploads/sites/2/2018/12/OdoriPark-1.jpg
https://www.jrailpass.com/blog/wp-content/uploads/2016/06/fukuoka-tower-1200x800.jpg
https://img.theculturetrip.com/768x432/wp-content/uploads/2017/05/5983298210_7d8ecd6dde_b.jpg
https://media.timeout.com/images/105292780/630/472/image.jpg
https://www.tripsavvy.com/thmb/K7_aPC1XA-elxfIVjYcoQDHS4FQ=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/gamcheon-culture-village--busan--south-korea-1149825040-2bc1e16a08c14ee9add5aae5f0e8e9b9.jpg
https://www.fodors.com/wp-content/uploads/2019/04/HERO_BangkokTips_Hero_shutterstock_367503629.jpg
https://img.theculturetrip.com/x/smart/wp-content/uploads/2019/04/asia-thai-chiang.jpg
https://lp-cms-production.imgix.net/2019-06/ab4a79b04c7c96508ea77aec7073e7d3-ho-chi-minh-city.jpg?fit=crop&q=40&sharp=10&vib=20&auto=format&ixlib=react-8.6.4
https://www.tripsavvy.com/thmb/0-6xZYPvwUSNMac0IAY_C9JTO1E=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-520483268-5a8001f5d8fdd50037283bae.jpg
https://www.befreetour.com/img/produk/romantic-danang-city-tour/romantic-danang-city-tour_398c3f9c87f81723ae60a230aeeeaea6c5030778.jpg
https://www.roadaffair.com/wp-content/uploads/2018/07/traffic-phnom-penh-cambodia-shutterstock_653520022-1024x674.jpg
https://media-cdn.tripadvisor.com/media/attractions-splice-spp-540x360/06/74/c2/c3.jpg
https://cdn.britannica.com/61/192661-050-997DE572/Colombo-Sri-Lanka.jpg
https://media.radissonhotels.net/image/Destination-Pages/Localattraction/16256-118729-f63245709_3XL.jpg?impolicy=HomeHero
https://www.tripsavvy.com/thmb/K7_aPC1XA-elxfIVjYcoQDHS4FQ=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/gamcheon-culture-village--busan--south-korea-1149825040-2bc1e16a08c14ee9add5aae5f0e8e9b9.jpg
https://media.timeout.com/images/105292780/630/472/image.jpg
https://lp-cms-production.imgix.net/2019-06/103730883%20.jpg?fit=crop&q=40&sharp=10&vib=20&auto=format&ixlib=react-8.6.4
https://www.tripsavvy.com/thmb/fMD1hxlyP9bVAG_dKjqNKu4NkwM=/3435x2576/smart/filters:no_upscale()/panoramic-skyline-and-cityscape-of-city-hongkong-544144869-5a08d5d3494ec90037f7cfff.jpg
https://lp-cms-production.imgix.net/2019-06/58481926.jpg?fit=crop&q=40&sharp=10&vib=20&auto=format&ixlib=react-8.6.4
https://www.planetware.com/wpimages/2019/08/thailand-krabi-top-beaches-railay-beach.jpg
https://www.tripsavvy.com/thmb/fHLak1CQr6gy0wDhDMBywSZFKUI=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/melaka_tour_01-83cec3bde78c4284bc6ada92559341dd.jpg
https://www.tripsavvy.com/thmb/QFFZg7VN6zEPXGz9MuTrg4rlpl8=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/penang-malaysia-b40c38589e794a61ba904d64c0a02c43.jpg
https://www.tripsavvy.com/thmb/W3sVPeg9soCoiY3dLcqcZh0XhB8=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/where-is-kuala-lumpug-5740492a5f9b58723d520ef4.jpg
https://www.costacruises.com/content/dam/costa/costa-asset/c_037/place/C037_Places_Singapore.jpg.image.750.563.low.jpg
https://r-cf.bstatic.com/images/hotel/max1024x768/216/216484929.jpg
https://img.theculturetrip.com/768x432/wp-content/uploads/2019/01/c9bdmt-feature.jpg
https://lp-cms-production.imgix.net/2019-06/78a5970b7661df124e01cc6f8efd572a-potala-palace.jpg?fit=crop&q=40&sharp=10&vib=20&auto=format&ixlib=react-8.6.4
https://www.indonesia.travel/content/dam/indtravelrevamp/en/destinations/bali-nusa-tenggara/bali/bali/Image3.jpg
 

### Acknowledgements

My website was inspired by Tripadvisor and Triphobo https://www.triphobo.com/tripplans/asia
https://www.tripadvisor.com.sg/

