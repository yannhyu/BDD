Feature: Our service makes short URLs out of long URLs
         All URLs will start with http://patl.ly:8080/ and end in a number
         representing the lookup index

  Scenario: Shortening an URL
    Given a url https://www.python.org/
    When we shorten it through our service
    Then we should receive a shortened URL

  Scenario: Retrieving an URL is fast
    Given we have shortened the url https://www.python.org/
    When we navigate to that shortened URL
    Then we arrive at https://www.python.org/ as fast as possible

  Scenario: Getting Stats
    Given we have shortened the url https://www.python.org/
    And we navigate to that shortened url 2 times
    And we have shortened the URL http://google.com
    And we navigate to that shortened url 3 times
    When we look at the stats on the homepage
    Then we see the shortened URL for https://www.python.org/ has been visited 2 times
    And we see the shortened URL for http://google.com has been visited 3 times

