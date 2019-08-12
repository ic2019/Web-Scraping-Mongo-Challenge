# Import all dependencies    
import pandas as pd
import requests
from bs4 import BeautifulSoup
from splinter import Browser
import time
import json

# Defining functions to instantiate webdriver, opening browser and closing browser.
# Defining functions to instantiate webdriver, opening browser and closing browser.

def init_browser():
    """
    Function to create an instance of Chrome webdriver class object.
    Parameters: None
    Return: browser object
    """
    # Import Splinter and set the chromedriver path
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    return browser

def open_browser(browser, url):
    """
    Function to open the url using the browser instance of Chrome webdriver class object.
    Parameters: browser object and url of the web page.
    Return: None
    """
    browser.visit(url)

def close_browser(browser):
    """
    Function to close the webpage opened using chromedriver object.
    Parameters: browser object
    Return: None
    """
    browser.quit()

def scrape_info():
    """
    Function to scrape mars related facts from web pages
    Parameters: None
    Return:  A dictionary object
    """

    # Collecting Nasa Mars news
    # Visit the Nasa URL
    url = "https://mars.nasa.gov/news/"
    try:
        browser = init_browser()
        open_browser(browser, url)
    
        # Scrape the browser into a soup object
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        news_title = soup.find('div', {"class" : "list_text"}).find('div', {"class" : "content_title"}).find('a').text
        news_p = soup.find('div', {"class" : "list_text"}).find('div', {"class" : "article_teaser_body"}).text
        close_browser(browser)
    except Exception as e:
        print(f"Error ocurred. Check your network connection! {e}")

    # Collecting JPL Mars Space Images - Latest Featured Image
    # Import Splinter and set the chromedriver path
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    try:
        browser = init_browser()
        open_browser(browser, url)

        try:
            time.sleep(1)
            element = browser.find_by_name('category')
            element.select('featured')
        except:
            time.sleep(1)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        imgs = soup.find('div', { 'class': 'image_and_description_container'}).find('div', {'class' : 'img'}).find_all('img')
        relative_image_url = imgs[0]["src"]
        featured_image_url = "https://www.jpl.nasa.gov"+relative_image_url
        #print(f" { featured_image_url}")
        close_browser(browser)
    except Exception as e:
        print(f"Error ocurred. Check your network connection! {e}")

    # Collecting Mars Latest Weather Tweet
    try:
        browser = init_browser()
        url = "https://twitter.com/marswxreport?lang=en"
        open_browser(browser, url)
        html = browser.html
        close_browser(browser)

        soup = BeautifulSoup(html, 'html.parser')

        tweets = soup.find_all('li', {'class' : 'js-stream-item'})
        for tweet in tweets:
            screen_name = tweet.find('div')["data-screen-name"]
            if screen_name == 'MarsWxReport':
                #print(tweet)
                result = tweet.find('div', {'class' : 'content'})\
                            .find('div', {'class' : 'js-tweet-text-container'})\
                            .find('p', {'class' : 'tweet-text'})
                mars_weather = result.text
                print(mars_weather)
                break
    except Exception as e:
         print(f"Error ocurred. Check your network connection! {e}")

    # Collecting Planet details from Mars Facts

    # Use Pandas to scrape the following site and decode the mars facts in the list.

    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    mars_facts = tables[1]
    
    # Cleaning up the table

    mars_facts.columns = ["description", "value"]

    mars_facts = mars_facts.set_index('description')
    mars_facts_json = json.loads(mars_facts.T.to_json())
    # mars_html_output = mars_facts.to_html("./html/mars_facts.html", justify="justify", bold_rows = True, table_id="mars_facts")
    print(mars_facts_json)

    # Collecting images from Mars Hemispheres.

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    try:
            browser = init_browser()
            open_browser(browser, url)
            html = browser.html

            hemisphere_image_urls = []

            soup = BeautifulSoup(html, 'html.parser')
            images = soup.find('div', {'id': 'product-section'}).find_all('h3')


            result = {}
            for image in images:
                result = {}
                image_text = image.text
                print(image)
                try:
                    time.sleep(10)
                    browser.find_link_by_partial_text(image_text)
                    browser.click_link_by_partial_text(image_text)
                    time.sleep(10)
                except:
                    time.sleep(1)
                title= browser.find_by_xpath('//div[@class="content"]//h2[@class="title"]').first.text
                img_url = browser.find_by_xpath('//div[@class="downloads"]//ul//li//a')["href"]
                result = { "title" : title, "img_url" : img_url}
                hemisphere_image_urls.append(result)
                browser.back()
                time.sleep(10)
            close_browser(browser)
    except Exception as e:
        print(f"Error ocurred. Check your network connection! {e}")

    #print(hemisphere_image_urls)
    mars_data = {
        'news_title' : news_title,
        'news_p' : news_p,
        'featured_image_url' : featured_image_url,
        'mars_weather' : mars_weather,
        'hemisphere_image_urls' : hemisphere_image_urls,
        'mars_facts' : mars_facts_json
        
    }
    print(mars_data)
    # Return results
    return mars_data
