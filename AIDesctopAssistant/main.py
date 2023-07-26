import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
import sys
import os
import time
import pygame
import datetime


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()  # Convert the input to lowercase
        except Exception as e:
            return "Some error occurred. Sorry from Puchu"


if __name__ == '__main__':
    say("Hello, I am Puchu A I")
    while True:
        print("Listening....")
        text = takeCommand()
        sites = [["Google", "https://www.google.com"],
                 ["YouTube", "https://www.youtube.com"],
                 ["Facebook", "https://www.facebook.com"],
                 ["Twitter", "https://www.twitter.com"],
                 ["Instagram", "https://www.instagram.com"],
                 ["LinkedIn", "https://www.linkedin.com"],
                 ["Reddit", "https://www.reddit.com"],
                 ["Pinterest", "https://www.pinterest.com"],
                 ["Amazon", "https://www.amazon.com"],
                 ["eBay", "https://www.ebay.com"],
                 ["Wikipedia", "https://www.wikipedia.org"],
                 ["IMDb", "https://www.imdb.com"],
                 ["Netflix", "https://www.netflix.com"],
                 ["Spotify", "https://www.spotify.com"],
                 ["Dropbox", "https://www.dropbox.com"],
                 ["GitHub", "https://www.github.com"],
                 ["Stack Overflow", "https://stackoverflow.com"],
                 ["Medium", "https://www.medium.com"],
                 ["Quora", "https://www.quora.com"],
                 ["Airbnb", "https://www.airbnb.com"],
                 ["Booking.com", "https://www.booking.com"],
                 ["CNN", "https://www.cnn.com"],
                 ["BBC News", "https://www.bbc.com/news"],
                 ["The New York Times", "https://www.nytimes.com"],
                 ["Microsoft", "https://www.microsoft.com"],
                 ["Apple", "https://www.apple.com"],
                 ["Android", "https://www.android.com"],
                 ["Adobe", "https://www.adobe.com"],
                 ["Yelp", "https://www.yelp.com"],
                 ["TripAdvisor", "https://www.tripadvisor.com"],
                 ["Tumblr", "https://www.tumblr.com"],
                 ["Hulu", "https://www.hulu.com"],
                 ["CNN Business", "https://www.cnn.com/business"],
                 ["BBC Sport", "https://www.bbc.com/sport"],
                 ["The Guardian", "https://www.theguardian.com"],
                 ["Microsoft Office", "https://www.office.com"],
                 ["Apple Music", "https://www.apple.com/music"],
                 ["Adobe Creative Cloud", "https://www.adobe.com/creativecloud"],
                 ["Walmart", "https://www.walmart.com"],
                 ["Target", "https://www.target.com"],
                 ["Best Buy", "https://www.bestbuy.com"],
                 ["Craigslist", "https://www.craigslist.org"],
                 ["PayPal", "https://www.paypal.com"],
                 ["Vimeo", "https://www.vimeo.com"],
                 ["SoundCloud", "https://www.soundcloud.com"],
                 ["Fandom", "https://www.fandom.com"],
                 ["BBC Food", "https://www.bbc.co.uk/food"],
                 ["The Verge", "https://www.theverge.com"],
                 ["WebMD", "https://www.webmd.com"],
                 ["Healthline", "https://www.healthline.com"],
                 ["National Geographic", "https://www.nationalgeographic.com"],
                 ["TED", "https://www.ted.com"],
                 ["Goodreads", "https://www.goodreads.com"],
                 ["Etsy", "https://www.etsy.com"],
                 ["AllRecipes", "https://www.allrecipes.com"],
                 ["Investopedia", "https://www.investopedia.com"],
                 ["Bloomberg", "https://www.bloomberg.com"],
                 ["Wired", "https://www.wired.com"],
                 ["HowStuffWorks", "https://www.howstuffworks.com"],
                 ["Mental Floss", "https://www.mentalfloss.com"],
                 ["The Atlantic", "https://www.theatlantic.com"],
                 ["TechCrunch", "https://www.techcrunch.com"],
                 ["Mashable", "https://www.mashable.com"],
                 ["Gizmodo", "https://www.gizmodo.com"],
                 ["Harvard Business Review", "https://www.hbr.org"],
                 ["Fast Company", "https://www.fastcompany.com"],
                 ["CNBC", "https://www.cnbc.com"],
                 ["Forbes", "https://www.forbes.com"],
                 ["Time", "https://www.time.com"],
                 ["Reuters", "https://www.reuters.com"],
                 ["BBC Weather", "https://www.bbc.co.uk/weather"],
                 ["Weather.com", "https://www.weather.com"],
                 ["AccuWeather", "https://www.accuweather.com"],
                 ["NASA", "https://www.nasa.gov"],
                 ["Space.com", "https://www.space.com"],
                 ["ESPN", "https://www.espn.com"],
                 ["NBA", "https://www.nba.com"],
                 ["NFL", "https://www.nfl.com"],
                 ["MLB", "https://www.mlb.com"],
                 ["NHL", "https://www.nhl.com"],
                 ["NCAA", "https://www.ncaa.com"],
                 ["FIFA", "https://www.fifa.com"],
                 ["UEFA", "https://www.uefa.com"],
                 ["Olympics", "https://www.olympics.com"],
                 ["World Health Organization", "https://www.who.int"],
                 ["Centers for Disease Control and Prevention (CDC)", "https://www.cdc.gov"],
                 ["Worldometers", "https://www.worldometers.info"],
                 ["U.S. Census Bureau", "https://www.census.gov"],
                 ["U.S. Department of State", "https://www.state.gov"],
                 ["United Nations", "https://www.un.org"],
                 ["World Bank", "https://www.worldbank.org"],
                 ["Google Maps", "https://www.google.com/maps"],
                 ["Apple Maps", "https://www.apple.com/maps"],
                 ["MapQuest", "https://www.mapquest.com"],
                 ["OpenStreetMap", "https://www.openstreetmap.org"],
                 ["Reddit", "https://www.reddit.com"],
                 ["Tumblr", "https://www.tumblr.com"],
                 ["Pinterest", "https://www.pinterest.com"]
            , ]

        pygame.mixer.init()

        for site in sites:
            if f"open {site[0]}".lower() in text:
                say(f"Opening {site[0]}, sir....")
                webbrowser.open(site[1])
            elif "exit" in text:
                say("Goodbye!")
                break
            elif "open music" in text:
                musicPath = "C:/Users/nagasaki1/Downloads/Arnob Hariye Giyechi.mp3"

                pygame.mixer.music.load(musicPath)
                pygame.mixer.music.play()
            elif "stop music" in text:
                pygame.mixer.music.stop()

            if "the time" in text:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir, the time is {strfTime}")

