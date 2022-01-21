from octoprint_mrbeamdoc.enum.mrbeam_doctype import MrBeamDocType
from octoprint_mrbeamdoc.enum.mrbeam_model import MrBeamModel
from octoprint_mrbeamdoc.enum.supported_languages import SupportedLanguage
from octoprint_mrbeamdoc.exception.mrbeam_doc_not_found import MrBeamDocNotFoundException
from octoprint_mrbeamdoc.model.mrbeam_doc import MrBeamDoc
from octoprint_mrbeamdoc.model.mrbeam_doc_definition import MrBeamDocDefinition


class MrBeamDocUtils:
    """
    Utils class to help organise the files we maintain in this project.
    There should be at least an instance of MrBeamDocDefinition per each MrBeamDocType.
    Every MrBeamModel should be represented only once per MrBeamDocType including here the additionally_valid_models.

    In order to create a new definition you just need to create a new class reference/static reference and the code will
    already start taking it into account.
    """

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
        """
        mrbeamdoc_type MrBeamDocType: Document type to be retrieved
        mrbeam_model MrBeamModel: MrBeamModel for which the document should be retrieved
        language String: language of the document in 2 character format. e.g. 'de', 'en', ...
        extension String: file format. e.g. 'pdf', ...

        Return MrBeamDoc instance representing the required parameters
        raises MrBeamDocNotFoundException if the parameters are invalid or don't match any existing definition
        """

        mrbeamdoc = MrBeamDocUtils._get_mrbeamdoc_for(mrbeamdoc_type, mrbeam_model, language, extension)
        if mrbeamdoc == None:
            raise MrBeamDocNotFoundException(mrbeamdoc_type, mrbeam_model, language)

        return mrbeamdoc

    @staticmethod
    def _get_mrbeamdoc_for(mrbeamdoc_type, mrbeam_model, language, extension='pdf'):
        if mrbeamdoc_type is None or mrbeam_model is None or language is None or extension != 'pdf':
            return None

        definitions_available = MrBeamDocUtils.get_definitions_available_with_cache()

        return next(
            (MrBeamDoc(definition, language, extension=extension) for definition, definition_name in
             definitions_available if definition.is_valid(mrbeamdoc_type, mrbeam_model, language)), None)

    @staticmethod
    def get_mrbeam_definitions_for(mrbeam_model):
        """
        Get all the definitions valid for a specific Mr Beam device.
        """

        definitions_available = MrBeamDocUtils.get_definitions_available_with_cache()
        return [definition for definition, definition_name in definitions_available if
                definition.is_valid_for_model(mrbeam_model)]

    @staticmethod
    def get_definitions_available_with_cache():
        if MrBeamDocUtils.__DEFINITIONS_AVAILABLE is None:
            MrBeamDocUtils.__DEFINITIONS_AVAILABLE = MrBeamDocUtils.get_definitions_available()
        return MrBeamDocUtils.__DEFINITIONS_AVAILABLE

    @staticmethod
    def get_definitions_available():
        return [[getattr(MrBeamDocUtils, attr), attr] for attr in dir(MrBeamDocUtils) if
                not callable(getattr(MrBeamDocUtils, attr)) and not attr.startswith("_")]
