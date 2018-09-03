
@given(u'a url {url}')
def step_impl(context, url):
    context.url = url

@given(u'we have shortened the url {url}')
def step_impl(context, url):
    context.url = url
    context.shortened_url = context.browser.shorten(url)
    context.mapping[context.url] = context.shortened_url

@given(u'we navigate to that shortened url {num_times:d} times')
def step_impl(context, num_times):
    # go to the url 
    for _ in range(num_times):
        context.browser.go_to_page(context.shortened_url)
    #reset back to the original page
    context.browser.go_to_homepage()

@when(u'we shorten it through our service')
def step_impl(context):
    context.shortened_url = context.browser.shorten(context.url)

@when(u'we navigate to that shortened URL')
def step_impl(context):
    context.browser.go_to_page(context.shortened_url)

@when(u'we look at the stats on the homepage')
def step_impl(context):
    context.stats = context.browser.get_stats()

@then(u'we arrive at {url} as fast as possible')
def step_impl(context, url):
    assert context.browser.is_at_page(url)
    #how do we test speed?

@then(u'we should receive a shortened URL')
def step_impl(context):
    assert context.shortened_url.startswith("http://pat.ly:8080")

@then(u'we see the shortened URL for {url} has been visited {num_times} times')
def step_impl(context, url, num_times):
    #this is the step that should fail, given our implementation
    assert context.stats[context.mapping[url]] == num_times
