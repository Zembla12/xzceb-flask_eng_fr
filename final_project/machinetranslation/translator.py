from deep_translator import MyMemoryTranslator

# Create an instance of MyMemory Translator
translator = MyMemoryTranslator()

def english_to_french(english_text):
    """
    Translate English to French.

    :param english_text: The English text to be translated.
    :type english_text: str
    :return: The translated French text.
    :rtype: str
    """
    french_text = translator.translate(english_text, 'fr')
    return french_text

def french_to_english(french_text):
    """
    Translate French to English.

    :param french_text: The French text to be translated.
    :type french_text: str
    :return: The translated English text.
    :rtype: str
    """
    english_text = translator.translate(french_text, 'en')
    return english_text

