import unittest
from src.main.tagging_algos.tagging_base_handler import TaggingBaseHandler

class TestTaggingBaseHandler(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        super(TestTaggingBaseHandler, self).setUpClass()
        self.base_handler = TaggingBaseHandler()

    def test_get_person_tags(self):
        sample = {'text': 'Cam Bedrosian', 'type': 'PERSON', 'start_char': 13, 'end_char': 19}
        response = self.base_handler.get_person_tags(sample)
        print("AYOO", response)
        valid_response = [{'type': 'person', 'value' :'Cam Bedrosian'}]
        self.assertCountEqual(response, valid_response)


    def test_generate_tags_non_specific(self):
        sample = "Hello this is Austin Marchese and this is the Banter Podcast."
        response = self.base_handler.get_basic_tags(sample)
        print(response)
        self.assertEqual(response, [])

if __name__ == '__main__':
    unittest.main()
