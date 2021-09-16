import unittest
import camelcase


class TestCamelCase(unittest.TestCase):


    # Tests for strange inputs like ints, floats, and None
    def test_camelcase_strange_inputes(self):
        self.assertFalse(camelcase.camel_case(1))
        self.assertFalse(camelcase.camel_case(None))
        self.assertFalse(camelcase.camel_case(1.25))


    # Basic sensible test
    def test_camelcase_setnence_string(self):
        self.assertEqual('helloWorld', camelcase.camel_case('Hello World'))


    # Test with single words
    def test_camelcase_single_worlds(self):
        self.assertEqual('word', camelcase.camel_case('Word'))
        self.assertEqual('a', camelcase.camel_case('a'))
        self.assertEqual('a', camelcase.camel_case('A'))
        self.assertEqual('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', camelcase.camel_case('aaaAAAAaaaaaaaaaaaaAAAAaaaaaaaaaaa'))


    # Test strings with integers in them
    def test_camelcase_strings_with_integers(self):
        self.assertEqual('1', camelcase.camel_case('1'))
        self.assertEqual('12345', camelcase.camel_case('12345'))
        self.assertEqual('12345', camelcase.camel_case('1 2 3 4 5'))
        self.assertEqual('thisIsAStringWith1', camelcase.camel_case('This is a string with 1'))
        self.assertEqual('1ThisIsAString', camelcase.camel_case('1 This is a string'))
        self.assertEqual('thisIsAStringWithMany111111111', camelcase.camel_case('This is a string with many 111 111 111'))


    # Test punctuation at the beginning, end and inbetween.
    def test_camelcase_strings_with_punctuation(self):
        self.assertEqual('word!', camelcase.camel_case('Word!'))
        self.assertEqual('thisIsATest!', camelcase.camel_case('This is a test!'))
        self.assertEqual('thisIsATest!', camelcase.camel_case('This is a test !'))
        self.assertEqual('thisIsATest!!!', camelcase.camel_case('This is a test ! ! !'))
        self.assertEqual('helloWorldI\'mYourWildProgram', camelcase.camel_case('Hello World i\'m your wild program')) # An interesting problem here, still thinking of a fix
        self.assertEqual('chch!Ch!!Ch!Cherry!Bomb', camelcase.camel_case('CHCH ! CH! !CH ! CHERRY ! BOMB!'))
        self.assertEqual('!chch!Ch!!Ch!Cherry!Bomb', camelcase.camel_case('!CHCH ! CH! !CH ! CHERRY ! BOMB!'))
        self.assertEqual('!Chch!Ch!!Ch!Cherry!Bomb', camelcase.camel_case('! CHCH ! CH! !CH ! CHERRY ! BOMB !'))
        self.assertEqual('!Chch!Ch!!Ch!Che!rry!Bomb', camelcase.camel_case('! CHCH ! CH! !CH ! CHE!RRY ! BOMB!'))


    # Test with floats in the string
    def test_camelcase_strings_with_float(self):
        self.assertEqual('1.001', camelcase.camel_case('1.001'))
        self.assertEqual('1.001IsAFloat', camelcase.camel_case('1.001 is a float'))
        self.assertEqual('float1.001', camelcase.camel_case('Float 1.001'))
    

    # Test with blank spaces, newlines, tabs
    def test_camelcase_strings_with_blank_space(self):
        self.assertEqual('', camelcase.camel_case(''))
        self.assertEqual('', camelcase.camel_case(' '))
        self.assertEqual('', camelcase.camel_case('\t')) #Test if input was Tab
        self.assertEqual('', camelcase.camel_case('          '))
        self.assertEqual('thisSentenceContainsAlotOfSpaces', camelcase.camel_case('This sentence  contains  alot    of  spaces'))
        self.assertEqual('helloWorld', camelcase.camel_case(' Hello World '))
        self.assertEqual('helloWorld', camelcase.camel_case('               Hello         World              '))
        self.assertEqual('helloWorld', camelcase.camel_case('\nHello World\n'))
    

    # Test with emojis
    def test_camelcase_strings_with_emojis(self):
        self.assertEqual('😀😃😄😁😆😅', camelcase.camel_case('😀😃😄 😁😆😅'))
        self.assertEqual('😀😃😄!😁😆😅', camelcase.camel_case('😀😃😄 !😁😆😅'))
        self.assertEqual('!😀😃😄😁😆😅', camelcase.camel_case('! 😀😃😄 😁😆😅'))
        self.assertEqual('😀😃😄😁😆😅', camelcase.camel_case('😀 😃 😄 😁 😆 😅'))
        self.assertEqual('😀Emoji😃😄😁😆😅', camelcase.camel_case('😀      emoji       😃😄 😁😆 😅'))


if __name__ == '__main__':
    unittest.main()