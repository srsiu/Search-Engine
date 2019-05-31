import atexit
import logging
import sys

from crawler import Crawler
from frontier import Frontier

if __name__ == "__main__":
    # Configures basic logging
    logging.basicConfig(filename = "out.txt", format='%(asctime)s (%(name)s) %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.INFO)

    # Instantiates frontier and loads the last state if exists
    frontier = Frontier()   
    frontier.load_frontier()
    # Registers a shutdown hook to save frontier state upon unexpected shutdown
    atexit.register(frontier.save_frontier)

    # Instantiates a crawler object and starts crawling
    crawler = Crawler(frontier)
    crawler.start_crawling()

    
    sys.stdout = open("url_out.txt", "w")
    print("DOWNLOADED URLS [", len(crawler.downloaded_urls), "]")
    print("TRAPS [", len(crawler.traps), "]")
    print("MAX OUTLINKS PAGE: ", crawler.get_max_out_links(), "\n\n")

    print("DOWNLOADED URLS [", len(crawler.downloaded_urls), "]: ", crawler.downloaded_urls, "\n\n")
    print("TRAPS [", len(crawler.traps), "]: ", crawler.traps, "\n\n")
    print("SUBDOMAINS: ", crawler.subdomains, "\n\n")
    print("OUT LINKS: ", crawler.out_links, "\n\n")


