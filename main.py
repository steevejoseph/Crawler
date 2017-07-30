import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# Change to allow user to enter project name, REMEMBER STEEVE
PROJECT_NAME = 'thenewboston'
# Change to allow user to enter homepage, REMEMBER STEEVE
HOMEPAGE = 'https://thenewboston.com/'


DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'

# POSSIBLY CANCER, REMEMBER STEEVE
NUMBER_OF_THREADS = 8

# Thread queue/job
queue = Queue()

# Start first crawl
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)

    queue.join()
    crawl()

# Create worker threads (dies on program exit)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do next job in queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Check if there are items in queue, and crawl if so.
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
