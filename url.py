import pyshorteners

url = "https://example.com"

shortener = pyshorteners.Shortener()


short_url = shortener.tinyurl.short(url)

print("Shortened URL:", short_url)
