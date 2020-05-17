import unittest
from src.main.utils.nlp_conversion_util import NLPConversionUtil

class TestNLPConversionUtil(unittest.TestCase):

    starting_dict = {"ab": "cd"}

    def test_filter_stop_words_and_punctuation(self):
        word_list = ['abcd', "a", "'", "austin"]
        self.assertEqual(2, len(NLPConversionUtil.remove_stop_words_and_punctuation(word_list)))

    def test_filter_duplicates_from_list(self):
        word_list = ['abcd', "a", "'", "austin", "austin"]
        self.assertEqual(4, len(NLPConversionUtil.remove_duplicates_from_list(word_list)))
        word_list = ['abcd', "a", "'", "austin"]
        self.assertEqual(4, len(NLPConversionUtil.remove_duplicates_from_list(word_list)))

    def test_filter_token_list_by_type(self):
        word_list = [{"type":'PERSON'}, {"type":'ORG'}, {"type":'ORG'}]
        self.assertEqual(1, len(NLPConversionUtil.filter_token_list_by_type(word_list, "PERSON")))

    def test_remove_punctuation_from_text(self):
        sample_str = "My name's austin"
        self.assertEqual("My names austin", NLPConversionUtil.remove_punctuation_from_text(sample_str))

    def test_remove_duplicates_from_dict_list(self):
        sample_dict = [{"type": "name", "value": "Austin"}, {"type":"name", "value": "Jesse"}, {"type":"name", "value": "Jesse"}]
        self.assertEqual(2, len(NLPConversionUtil.remove_duplicates_from_dict_list_based_on_key(sample_dict)))

    def test_filter_tokens_get_unique_text(self):
        sample_dict = [{"type": "PERSON", "text": "Austin"}, {"type":"ORG", "text": "Jesse"},
                       {"type":"ORG", "text": "Jesse"}, {"type":"NOT_IMPORTANT", "text": "Jesse"}]
        response, token_set, token_concat_str = NLPConversionUtil.filter_tokens_get_unique_text(sample_dict, {"PERSON"})
        self.assertEqual(response, [{'type': 'PERSON', 'text': 'Austin'}])
        self.assertEqual(token_set, {'Austin'})
        self.assertEqual(token_concat_str, 'Austin')

    def test_append_to_existing_dict(self):
        expected = {"ab": "ce"}
        response = NLPConversionUtil.append_to_existing_dict("ab", "ce", self.starting_dict)
        self.assertEqual(expected, response)




if __name__ == '__main__':
    unittest.main()
