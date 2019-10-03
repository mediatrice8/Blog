import unittest
from app.models import Comment

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment(id =1, usernames = 'nana',comment= 'this is good post',blog_id=2,user_id= 3)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))    
if __name__ == '__main__':
    unittest.main()