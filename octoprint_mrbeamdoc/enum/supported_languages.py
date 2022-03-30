from enum import Enum


class SupportedLanguage(Enum):
    """
    In this Enum we list all the language we support by at least one of the document types.
    BEWARE that not every language is supported by every document type
    """
    GERMAN = 'de'
    ENGLISH = 'en'
    SPANISH = 'es'
    FRENCH = 'fr'
    ITALIAN = 'it'
    DUTCH = 'nl'
    FINNISH = 'fi'
