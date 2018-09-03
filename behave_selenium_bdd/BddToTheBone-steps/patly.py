"""
A hard-coded webserver meant for PyTN BDD to the Bone talk
"""
from bottle import  get, post, redirect, request, run, static_file
from url_shortener import URLShortener

@get("/")
def return_index():
    """
    return index.html from the static folder
    """
    return return_static_file("index.html")

@get("/static/<path:path>")
def return_static_file(path):
    """
    return a static file from the static folder
    param path the path to the file
    """
    return static_file(path, root="static")

@post("/createShortenedLink")
def create_shortened_link():
    """
    create a shortened link from the user
    """
    index = url_shortener.shorten(request.json["url"])
    return {"shortened_link": "http://pat.ly:8080/{}".format(index) }

@get("/<identifier:int>")
def redirect_to_page(identifier):
    """
    redirect to the appropriate id
    param id the id that we've registered
    """
    url = url_shortener.retrieve(identifier)
    redirect(url)

@get("/get-stats")
def get_stats():
    """
    Return a list of stats for each URL we have shown
    """
    return url_shortener.get_stats()

url_shortener = URLShortener()
run(host="0.0.0.0", reloader=True)
