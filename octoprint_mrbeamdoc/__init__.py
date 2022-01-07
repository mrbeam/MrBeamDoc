#!/usr/bin/env python
# coding=utf-8
import os
from enum import Enum

from __version import __version__

_ROOT = os.path.abspath(os.path.dirname(__file__))


class MrBeamDocNotFoundException(Exception):
    """Raised when the file requested is not found in the system"""

    def __init__(self, mrbeamdoc_type, mrbeam_model, language):
        super(MrBeamDocNotFoundException, self).__init__(
            'The MrBeamDocType requested -> %(mrbeamdoc_type)s does not exist in the specified mrbeam_model -> %(mrbeam_model)s and language -> %(language)s' % {
                'mrbeamdoc_type': mrbeamdoc_type, 'mrbeam_model': mrbeam_model, 'language': language})


def get_doc_path(mrbeamdoc_type, mrbeam_model, language, extension='pdf'):
    """
    mrbeamdoc_type MrBeamDocType: Enum containing all the types of documents we are owning as Strings
    mrbeam_model MrBeamModel: Enum containing all the existing mrbeam models as Strings
    language String: language in 2 character format. e.g. 'de', 'en', ...
    extension String: file format. e.g. 'pdf', ...

    Return MrBeamDoc containing the needed paths to the requested file
    raises MrBeamDocNotFoundException if the parameters are invalid or don't match any existing file
    """

    mrbeamdoc = MrBeamDocAvailable.get_mrbeamdoc_for(mrbeamdoc_type, mrbeam_model, language, extension)
    if mrbeamdoc == None:
        raise MrBeamDocNotFoundException(mrbeamdoc_type, mrbeam_model, language)

    return mrbeamdoc


def get_version():
    return __version__


class MrBeamDoc:
    def __init__(self, definition, language, extension='pdf'):
        self.definition = definition
        self.language = language
        self.extension = extension

    def __repr__(self):
        return 'MrBeamDoc(definition=%(definition)s, language=%(language)s, extension=%(extension)s)' % {
            'definition': repr(self.definition),
            'language': self.language.name,
            'extension': self.extension,
        }

    def get_folder(self):
        return os.path.join(_ROOT, 'docs')

    def get_file_name_with_extension(self):
        return '%(mrbeamdoc_type)s_%(mrbeam_model)s_%(language)s.%(extension)s' % {
            'mrbeamdoc_type': self.definition.mrbeamdoc_type.value,
            'mrbeam_model': self.definition.mrbeam_model.value,
            'language': self.language.value,
            "extension": self.extension}

    def get_file_reference(self):
        return os.path.join(self.get_folder(), self.get_file_name_with_extension())


class SupportedLanguage(Enum):
    GERMAN = 'de'
    ENGLISH = 'en'
    SPANISH = 'es'
    FRENCH = 'fr'
    ITALIAN = 'it'
    DUTCH = 'nl'
    FINNISH = 'fi'


class MrBeamDocType(Enum):
    USER_MANUAL = 'UserManual'
    QUICKSTART_GUIDE = 'QuickstartGuide'


class MrBeamModel(Enum):
    MRBEAM2 = 'mrbeam2'
    MRBEAM2_DC_R1 = 'mrbeam2_dc_r1'
    MRBEAM2_DC_R2 = "mrbeam2_dc_r2"
    DREAMCUT_ALIAS = 'dreamcut'
    DREAMCUT = 'mrbeam2_dc'
    DREAMCUT_S = "mrbeam2_dc_s"


class MrBeamDocDefinition:
    def __init__(self, mrbeamdoc_type, mrbeam_model, supported_languages, additionally_valid_models=[]):
        self.mrbeamdoc_type = mrbeamdoc_type
        self.mrbeam_model = mrbeam_model
        additionally_valid_models.append(mrbeam_model)
        self.valid_models = set(item for item in additionally_valid_models)
        self.supported_languages = set(item for item in supported_languages)

    def __repr__(self):
        return """MrBeamDocDefinition(mrbeamdoc_type=%(mrbeamdoc_type)s,
            mrbeam_model=%(mrbeam_model)s,
            valid_models=%(valid_models)s,
            supported_languages=%(supported_languages)s
        )""" % {
            'mrbeamdoc_type': self.mrbeamdoc_type.name,
            'mrbeam_model': self.mrbeam_model.name,
            'valid_models': ','.join(item.name for item in self.valid_models),
            'supported_languages': ','.join(item.name for item in self.supported_languages)
        }

    def is_valid_for_model(self, mrbeam_model):
        return mrbeam_model in self.valid_models

    def is_language_supported(self, language):
        return language in self.supported_languages

    def is_valid(self, mrbeamdoc_type, mrbeam_model, language):
        return self.mrbeamdoc_type == mrbeamdoc_type and self.is_valid_for_model(
            mrbeam_model) and self.is_language_supported(
            language)


class MrBeamDocAvailable:
    QUICKSTART_GUIDE = MrBeamDocDefinition(MrBeamDocType.QUICKSTART_GUIDE,
                                           MrBeamModel.MRBEAM2,
                                           [SupportedLanguage.GERMAN,
                                            SupportedLanguage.ENGLISH],
                                           additionally_valid_models=[MrBeamModel.MRBEAM2_DC_R1,
                                                                      MrBeamModel.MRBEAM2_DC_R2])

    QUICKSTART_GUIDE_DREAMCUT = MrBeamDocDefinition(MrBeamDocType.QUICKSTART_GUIDE,
                                                    MrBeamModel.DREAMCUT_ALIAS,
                                                    [SupportedLanguage.GERMAN,
                                                     SupportedLanguage.ENGLISH],
                                                    additionally_valid_models=[MrBeamModel.DREAMCUT,
                                                                               MrBeamModel.DREAMCUT_S])
    USER_MANUAL = MrBeamDocDefinition(MrBeamDocType.USER_MANUAL,
                                      MrBeamModel.MRBEAM2,
                                      [SupportedLanguage.GERMAN,
                                       SupportedLanguage.ENGLISH,
                                       SupportedLanguage.SPANISH,
                                       SupportedLanguage.FRENCH,
                                       SupportedLanguage.ITALIAN,
                                       SupportedLanguage.FINNISH],
                                      additionally_valid_models=[MrBeamModel.MRBEAM2_DC_R1,
                                                                 MrBeamModel.MRBEAM2_DC_R2])
    USER_MANUAL_DREAMCUT = MrBeamDocDefinition(MrBeamDocType.USER_MANUAL,
                                               MrBeamModel.DREAMCUT_ALIAS,
                                               [SupportedLanguage.GERMAN,
                                                SupportedLanguage.ENGLISH,
                                                SupportedLanguage.SPANISH,
                                                SupportedLanguage.FRENCH,
                                                SupportedLanguage.ITALIAN,
                                                SupportedLanguage.DUTCH],
                                               additionally_valid_models=[MrBeamModel.DREAMCUT,
                                                                          MrBeamModel.DREAMCUT_S])
    """Cache of definitions created, no need of refresh until update"""
    __DEFINITIONS_AVAILABLE = None

    def __init__(self):
        pass

    @staticmethod
    def get_mrbeamdoc_for(mrbeamdoc_type, mrbeam_model, language, extension='pdf'):
        if mrbeamdoc_type is None or mrbeam_model is None or language is None or extension != 'pdf':
            return None

        definitions_available = MrBeamDocAvailable.get_definitions_available_with_cache()

        return next(
            (MrBeamDoc(definition, language, extension=extension) for definition, definition_name in
             definitions_available if definition.is_valid(mrbeamdoc_type, mrbeam_model, language)), None)

    @staticmethod
    def get_mrbeam_definitions_for(mrbeam_model):
        definitions_available = MrBeamDocAvailable.get_definitions_available_with_cache()
        return [definition for definition, definition_name in definitions_available if
                definition.is_valid_for_model(mrbeam_model)]

    @staticmethod
    def get_definitions_available_with_cache():
        if MrBeamDocAvailable.__DEFINITIONS_AVAILABLE is None:
            MrBeamDocAvailable.__DEFINITIONS_AVAILABLE = MrBeamDocAvailable.get_definitions_available()
        return MrBeamDocAvailable.__DEFINITIONS_AVAILABLE

    @staticmethod
    def get_definitions_available():
        return [[getattr(MrBeamDocAvailable, attr), attr] for attr in dir(MrBeamDocAvailable) if
                not callable(getattr(MrBeamDocAvailable, attr)) and not attr.startswith("_")]
