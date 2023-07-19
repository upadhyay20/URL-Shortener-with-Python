import pyshorteners

url = "https://example.com"

# Create an instance of the Shortener class
shortener = pyshorteners.Shortener()

# Shorten the URL
short_url = shortener.tinyurl.short(url)

print("Shortened URL:", short_url)
