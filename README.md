# Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

This project is about building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what have been done.

## Step 1 - Scraping

Initial scraping and analysis are completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Click [mission_to_mars](mission_to_mars.ipynb) for details. 

Following wesites were scraped to complete this project.

### NASA Mars News

* [NASA Mars News Site](https://mars.nasa.gov/news/) for the latest News Title and Paragraph Text. 

### JPL Mars Space Images - Featured Image

* For JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and using splinter found the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`.

### Mars Weather

* Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scraped the latest Mars weather tweet from the page. This tweet text for the weather report is saved to a variable called `mars_weather`.

### Mars Facts

* Mars Facts webpage [here](https://space-facts.com/mars/) was scraped for gathering facts using Pandas about the planet including Diameter, Mass, etc and to convert the data to a HTML table string.

### Mars Hemispheres

* USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

## Step 2 - MongoDB and Flask Application

Data in MongoDB

```
> db.collection.find({}).pretty()
{
        "_id" : ObjectId("5d52636f7cf79918e06981de"),
        "news_title" : "Small Satellite Mission of the Year",
        "news_p" : "The first interplanetary CubeSats were recognized by the engineering community with the 2019 Small Satellite Mission of the Year award.",
        "featured_image_url" : "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23354_hires.jpg",
        "mars_weather" : "InSight sol 250 (2019-08-10) low -100.0ºC (-148.1ºF) high -26.2ºC (-15.1ºF)\nwinds from the SSE at 4.4 m/s (9.8 mph) gusting to 16.2 m/s (36.2 mph)\npressure at 7.60 hPapic.twitter.com/9sZRRUi3dm",
        "hemisphere_image_urls" : [
                {
                        "title" : "Cerberus Hemisphere Enhanced",
                        "img_url" : "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"
                },
                {
                        "title" : "Schiaparelli Hemisphere Enhanced",
                        "img_url" : "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"
                },
                {
                        "title" : "Syrtis Major Hemisphere Enhanced",
                        "img_url" : "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"
                },
                {
                        "title" : "Valles Marineris Hemisphere Enhanced",
                        "img_url" : "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"
                }
        ],
        "mars_facts" : {
                "Equatorial Diameter:" : {
                        "value" : "6,792 km"
                },
                "Polar Diameter:" : {
                        "value" : "6,752 km"
                },
                "Mass:" : {
                        "value" : "6.39 × 10^23 kg (0.11 Earths)"
                },
                "Moons:" : {
                        "value" : "2 (Phobos & Deimos)"
                },
                "Orbit Distance:" : {
                        "value" : "227,943,824 km (1.38 AU)"
                },
                "Orbit Period:" : {
                        "value" : "687 days (1.9 years)"
                },
                "Surface Temperature:" : {
                        "value" : "-87 to -5 °C"
                },
                "First Record:" : {
                        "value" : "2nd millennium BC"
                },
                "Recorded By:" : {
                        "value" : "Egyptian astronomers"
                }
        }
}
```
MongoDB with Flask templating was used to create a new HTML page that displays all of the information that was scraped from the URLs.above.

Before:

![before](Images/before-scraping.png)

After scraping:

![part1.png](Images/part1.png)
![part2.png](Images/part2.png)


## Copyright

© 2019 Trilogy Education Services. All Rights Reserved.
