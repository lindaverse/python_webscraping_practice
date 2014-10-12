from lxml import html
import requests
from urllib.parse import urlparse


def domain_matches_filter(url, domain_filter):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain_filter in domain


def get_links_from_url(url, domain_filter):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    tree.make_links_absolute(url)
    iterlinks = list(tree.iterlinks())
    return {
        link for element, attribute, link, pos in iterlinks
        if domain_matches_filter(link, domain_filter) and attribute == 'href'
    }


def crawl(url, domain_filter):
    queue = [url]
    unique_urls = set(queue)
    while queue:
        next_url = queue.pop()
        links = get_links_from_url(next_url, domain_filter)
        queue.extend(link for link in links if link not in unique_urls)
        unique_urls.update(links)
    return unique_urls

result = crawl("http://uk.queryclick.com/", "queryclick")

print(len(result))
