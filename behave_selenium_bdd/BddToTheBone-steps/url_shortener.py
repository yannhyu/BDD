import unittest

class URLShortener(object):
    
    def __init__(self):
        self.mapping = {}
        self.retrieved_count = {}

    def shorten(self, url):
        if url not in self.mapping:
            self.mapping[url] = len(self.mapping) + 1
            self.retrieved_count[url] = 0
        return self.mapping[url]

    def retrieve(self, shortened_url):
        for url, index in self.mapping.items():
            if index == shortened_url:
                self.retrieved_count[url] += 1
                return url
        return None

    def get_stats(self):
        return self.retrieved_count

class TestURLShortener(unittest.TestCase):

    def test_retrieve_shortened_url(self):
        url_shortener = URLShortener()
        shortnened_url = url_shortener.shorten("https://www.python.org")
        self.assertEquals(1, shortnened_url)

        shortnened_url = url_shortener.shorten("https://www.google.com")
        self.assertEquals(2, shortnened_url)

    def test_same_url_returns_same_link(self):
        url_shortener = URLShortener()
        shortnened_url = url_shortener.shorten("https://www.python.org")
        self.assertEquals(1, shortnened_url)

        shortnened_url = url_shortener.shorten("https://www.python.org")
        self.assertEquals(1, shortnened_url)

    def test_can_retrieve_url(self):
        url_shortener = URLShortener()
        url = "https://www.python.org"
        shortened_url = url_shortener.shorten(url)
        self.assertEquals(url, url_shortener.retrieve(shortened_url))

    def test_cannot_retreive_url_that_has_not_been_shortened(self):
         url_shortener = URLShortener()
         self.assertEquals(None, url_shortener.retrieve(1))

    def test_stats_are_zero_on_freshly_shortened_url(self):
        url_shortener = URLShortener()
        url_shortener.shorten("https://python.org")
        self.assertEquals({"https://python.org": 0}, url_shortener.get_stats())

    def test_retrieved_url_increments_stats(self):
        url_shortener = URLShortener()
        url_shortener.shorten("https://python.org")
        url_shortener.retrieve(1)
        self.assertEquals({"https://python.org": 1}, url_shortener.get_stats())

        url_shortener.retrieve(1)
        self.assertEquals({"https://python.org": 2}, url_shortener.get_stats())

    def test_retrieved_url_increments_stats_independently(self):
        url_shortener = URLShortener()
        url_shortener.shorten("https://python.org")
        url_shortener.shorten("https://google.com")
        url_shortener.retrieve(1)
        url_shortener.retrieve(1)
        url_shortener.retrieve(2)
        self.assertEquals({"https://python.org": 2, "https://google.com" : 1}, url_shortener.get_stats())
        
