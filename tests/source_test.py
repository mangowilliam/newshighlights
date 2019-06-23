import unittest
from app.source import Source
from app.articles import Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(1234,'Python Must Be Crazy','kenya','A thrilling new Python Series','business', 'http://uk.businessinsider.com/')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Article(1234,'Python Must Be Crazy','A thrilling new Python Series','business', 'http://uk.businessinsider.com/',"https://cbsnews1.cbsistatic.com/hub/i/r/2019/06/22/ebda1011-ab53-49a2-9e98-08f6f72690e5/thumbnail/1200x630/d7a656b3b73579940ae3ecc50313a841/800.jpg","2019-06-22T14:59:00Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Article))


if __name__ == '__main__':
    unittest.main()