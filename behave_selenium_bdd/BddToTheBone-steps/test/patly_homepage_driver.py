class PatlyHomepageDriver(object):
    def __init__(self, browser):
        self.browser = browser

    def shorten(self, url):
        self.browser.find_element_by_id("input").send_keys(url)
        self.browser.find_element_by_id("get-short-link").click()
        return self.browser.find_element_by_id("return-link").text

    def go_to_page(self, url):
        self.browser.get(url)

    def go_to_homepage(self):
        self.go_to_page("http://pat.ly:8080")

    def get_stats(self):
        stats = {}
        table = self.browser.find_element_by_id("stats")
        for row in table.find_elements_by_tag_name("tr")[1:]:
            cells = row.find_elements_by_tag_name("td")
            stats[cells[0]] = cells[1]
        return stats

    def is_at_page(self, url):
            return url == self.browser.current_url


    def quit(self):
        self.browser.quit()
        
