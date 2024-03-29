import unittest
from app.models import Blog

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog(id=3,title = 'life',blog='post',user_id= 2)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))
if __name__ == '__main__':
    unittest.main()