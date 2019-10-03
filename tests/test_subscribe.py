import unittest
from app.models import Subscribe

class SubscribeTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Subscribe class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_subscribe = Subscribe(id =1,name= 'media', subscribe= 'this is good post',email = 'kampiremediatrice@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_subscribe,Subscribe))
        
if __name__ == '__main__':
    unittest.main()