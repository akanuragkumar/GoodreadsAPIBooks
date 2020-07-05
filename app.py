# python app.py 1764323.A_Name_to_Conjure_With
# export API_KEY='vOAW5NlDLXt00UcKuotxtg'
import sys
import xml
from xml.etree import ElementTree
from requests import HTTPError
from exceptions import InvalidGoodreadsURL, MissingArguementError, MissingAPIKey
from requests.api import get
import os
import logging


class GoodReadsAPIClient:
    try:
        book_name = str(sys.argv[1])
    except IndexError:
        raise MissingArguementError

    API_KEY = os.environ.get("API_KEY")
    if API_KEY is None:
        raise MissingAPIKey

    def get_book_details(self):
        url = 'https://www.goodreads.com/book/show/{}.xml?key={}'.format(self.book_name, self.API_KEY)
        logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        try:
            resp = get(url)
            book_xml = xml.etree.ElementTree.fromstring(resp.content)
            for book in book_xml:
                title = book.findtext('./title') or ''
                average_rating = book.findtext('./average_rating') or ''
                ratings_count = book.findtext('./ratings_count') or ''
                num_pages = book.findtext('./num_pages') or ''
                image_url = book.findtext('./image_url') or ''
                publication_year = book.findtext('./publication_year') or ''
                authors = book.findtext('./authors/author/name') or ''
                book_dict = {"title": title, "average_rating": average_rating,
                             "ratings_count": ratings_count, "num_pages": num_pages, "image_url": image_url,
                             "publication_year": publication_year, "authors": authors}
            logging.info('Book: {}, result: {}'.format(self.book_name, book_dict))
            return book_dict
        except Exception as e:
            raise InvalidGoodreadsURL


Book_Object = GoodReadsAPIClient()
obj_dict = Book_Object.get_book_details()
print(obj_dict)
