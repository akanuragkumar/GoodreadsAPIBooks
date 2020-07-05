# python test_unit.py 1764323.A_Name_to_Conjure_With
import unittest
from app import GoodReadsAPIClient


class TestObject(unittest.TestCase):
    def setUp(self):
        self.sys_args = '1764323.A_Name_to_Conjure_With'
        self.key = 'vOAW5NlDLXt00UcKuotxtg'

    def runTest(self):
        book_object = GoodReadsAPIClient()
        self.assertEqual(self.sys_args, book_object.book_name)
        self.assertEqual(self.key, book_object.API_KEY)


class TestValues(unittest.TestCase):
    def setUp(self):
        self.average_rating = '3.27'
        self.title = 'A Name to Conjure With (Zarathandra, #1)'
        self.ratings_count = '41'
        self.num_pages = ''
        self.image_url = 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1265393623l/1764323._SY160_.jpg'
        self.publication_year = '1989'
        self.authors = 'Donald Aamodt'

    def runTest(self):
        book_object = GoodReadsAPIClient()
        obj_dict = book_object.get_book_details()
        self.assertEqual(self.average_rating, obj_dict['average_rating'])
        self.assertEqual(self.title, obj_dict['title'])
        self.assertEqual(self.ratings_count, obj_dict['ratings_count'])
        self.assertEqual(self.num_pages, obj_dict['num_pages'])
        self.assertEqual(self.image_url, obj_dict['image_url'])
        self.assertEqual(self.publication_year, obj_dict['publication_year'])
        self.assertEqual(self.authors, obj_dict['authors'])


unittest.TextTestRunner().run(TestObject())
unittest.TextTestRunner().run(TestValues())
