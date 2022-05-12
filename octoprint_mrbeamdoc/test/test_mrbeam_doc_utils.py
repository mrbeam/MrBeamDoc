from unittest import TestCase

from mock import patch

from octoprint_mrbeamdoc.enum.mrbeam_doctype import MrBeamDocType
from octoprint_mrbeamdoc.enum.mrbeam_model import MrBeamModel
from octoprint_mrbeamdoc.enum.supported_languages import SupportedLanguage
from octoprint_mrbeamdoc.exception.mrbeam_doc_not_found import MrBeamDocNotFoundException
from octoprint_mrbeamdoc.utils import mrbeam_doc_utils
from octoprint_mrbeamdoc.utils.mrbeam_doc_utils import MrBeamDocUtils


class TestMrBeamDocUtils(TestCase):
    def tearDown(self):
        # Needed since otherwise the cache is not initialised after the test ran with patch mocking
        reload(mrbeam_doc_utils)

    def test_happy_path_german(self):
        mrbeamdoc = MrBeamDocUtils.get_mrbeamdoc_for(MrBeamDocType.QUICKSTART_GUIDE, MrBeamModel.MRBEAM2,
                                                     SupportedLanguage.GERMAN)
        self.assertEquals('QuickstartGuide_mrbeam2_de.pdf', mrbeamdoc.get_file_name_with_extension())

    def test_happy_path_english(self):
        mrbeamdoc = MrBeamDocUtils.get_mrbeamdoc_for(MrBeamDocType.USER_MANUAL, MrBeamModel.DREAMCUT,
                                                     SupportedLanguage.ENGLISH)
        self.assertEquals('UserManual_dreamcut_en.pdf', mrbeamdoc.get_file_name_with_extension())

    def test_happy_path_additional_models(self):
        mrbeamdoc = MrBeamDocUtils.get_mrbeamdoc_for(MrBeamDocType.USER_MANUAL, MrBeamModel.MRBEAM2_DC_R1,
                                                     SupportedLanguage.FRENCH)
        self.assertEquals('UserManual_mrbeam2_fr.pdf', mrbeamdoc.get_file_name_with_extension())

    def test_none_extension(self):
        self.assertRaises(MrBeamDocNotFoundException,
                          MrBeamDocUtils.get_mrbeamdoc_for,
                          MrBeamDocType.USER_MANUAL,
                          MrBeamModel.MRBEAM2_DC_R1,
                          SupportedLanguage.FRENCH,
                          extension=None)

    def test_empty_extension(self):
        self.assertRaises(MrBeamDocNotFoundException,
                          MrBeamDocUtils.get_mrbeamdoc_for,
                          MrBeamDocType.USER_MANUAL,
                          MrBeamModel.MRBEAM2_DC_R1,
                          SupportedLanguage.FRENCH,
                          extension='')

    def test_blank_extension(self):
        self.assertRaises(MrBeamDocNotFoundException,
                          MrBeamDocUtils.get_mrbeamdoc_for,
                          MrBeamDocType.USER_MANUAL,
                          MrBeamModel.MRBEAM2_DC_R1,
                          SupportedLanguage.FRENCH,
                          extension=' ')

    def test_when_not_pdf_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, MrBeamDocUtils.get_mrbeamdoc_for,
                          MrBeamDocType.QUICKSTART_GUIDE,
                          MrBeamModel.DREAMCUT,
                          SupportedLanguage.ENGLISH,
                          'gif')

    def test_when_doc_available_and_language_not_available_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, MrBeamDocUtils.get_mrbeamdoc_for,
                          MrBeamDocType.QUICKSTART_GUIDE,
                          MrBeamModel.DREAMCUT,
                          SupportedLanguage.FINNISH)

    def test_when_type_none_and_model_and_language_available_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, MrBeamDocUtils.get_mrbeamdoc_for,
                          None,
                          MrBeamModel.MRBEAM2,
                          SupportedLanguage.ENGLISH)

    def test_when_model_none_and_type_and_language_available_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, MrBeamDocUtils.get_mrbeamdoc_for,
                          MrBeamDocType.USER_MANUAL,
                          None,
                          SupportedLanguage.ENGLISH)

    def test_when_language_none_and_type_and_model_available_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, MrBeamDocUtils.get_mrbeamdoc_for,
                          MrBeamDocType.USER_MANUAL,
                          MrBeamModel.MRBEAM2,
                          None)

    def test_when_language_available_and_type_and_model_none_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, MrBeamDocUtils.get_mrbeamdoc_for,
                          None,
                          None,
                          SupportedLanguage.ENGLISH)

    def test_when_type_available_and_model_and_language_none_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, MrBeamDocUtils.get_mrbeamdoc_for,
                          MrBeamDocType.USER_MANUAL,
                          None,
                          None)

    def test_when_doc_available_and_language_none_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, MrBeamDocUtils.get_mrbeamdoc_for,
                          None,
                          MrBeamModel.MRBEAM2,
                          None)

    def test_when_doc_available_and_language_none_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, MrBeamDocUtils.get_mrbeamdoc_for,
                          None,
                          None,
                          None)

    def test_definitions_per_model(self):
        definitions = MrBeamDocUtils.get_mrbeam_definitions_for(MrBeamModel.MRBEAM2)
        for definition in definitions:
            self.assertEquals(MrBeamModel.MRBEAM2, definition.mrbeam_model)

    @patch('octoprint_mrbeamdoc.utils.mrbeam_doc_utils.MrBeamDocUtils.get_definitions_available')
    def test_cache_is_used_definitions_per_model(self, get_definitions_available_mock):
        MrBeamDocUtils.get_mrbeam_definitions_for(MrBeamModel.MRBEAM2)
        MrBeamDocUtils.get_mrbeam_definitions_for(MrBeamModel.MRBEAM2_DC_R1)
        MrBeamDocUtils.get_mrbeam_definitions_for(MrBeamModel.MRBEAM2_DC_R2)
        MrBeamDocUtils.get_mrbeam_definitions_for(MrBeamModel.DREAMCUT)
        MrBeamDocUtils.get_mrbeam_definitions_for(MrBeamModel.DREAMCUT_S)
        self.assertEquals(get_definitions_available_mock.call_count, 1)
