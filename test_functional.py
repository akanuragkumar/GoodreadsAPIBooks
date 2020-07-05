# python test_functional.py 1764323.A_Name_to_Conjure_With
import unittest
from app import GoodReadsAPIClient


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        self.book_dict = {"title": 'A Name to Conjure With (Zarathandra, #1)', "average_rating": '3.27',
                          "ratings_count": '41', "num_pages": '',
                          "image_url": 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1265393623l/1764323._SY160_.jpg',
                          "publication_year": '1989', "authors": 'Donald Aamodt'}

    def runTest(self):
        book_object = GoodReadsAPIClient()
        obj_dict = book_object.get_book_details()
        self.assertEqual(self.book_dict, obj_dict)


unittest.TextTestRunner().run(FunctionalTests())
