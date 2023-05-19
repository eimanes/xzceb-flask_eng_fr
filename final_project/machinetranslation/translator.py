"""
This module contains functions to translate text between English and French using IBM Watson Language Translator.
"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-05-19',  # current date as version
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Translate English text to French using IBM Watson Language Translator.

    Parameters:
    english_text (str): The English text to translate

    Returns:
    french_text (str): The translated French text
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translate French text to English using IBM Watson Language Translator.

    Parameters:
    french_text (str): The French text to translate

    Returns:
    english_text (str): The translated English text
    """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
