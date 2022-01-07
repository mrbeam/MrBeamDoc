from unittest import TestCase

from octoprint_mrbeamdoc import get_doc_path, MrBeamDocAvailable, SupportedLanguage, MrBeamDocNotFoundException, \
    MrBeamModel, MrBeamDocType


class Test(TestCase):
    def test_happy_path_german(self):
        mrbeamdoc = get_doc_path(MrBeamDocType.QUICKSTART_GUIDE, MrBeamModel.MRBEAM2, SupportedLanguage.GERMAN)
        self.assertEquals('QuickstartGuide_mrbeam2_de.pdf', mrbeamdoc.get_file_name_with_extension())

    def test_happy_path_english(self):
        mrbeamdoc = get_doc_path(MrBeamDocType.USER_MANUAL, MrBeamModel.DREAMCUT, SupportedLanguage.ENGLISH)
        self.assertEquals('UserManual_dreamcut_en.pdf', mrbeamdoc.get_file_name_with_extension())

    def test_happy_path_additional_models(self):
        mrbeamdoc = get_doc_path(MrBeamDocType.USER_MANUAL, MrBeamModel.MRBEAM2_DC_R1, SupportedLanguage.FRENCH)
        self.assertEquals('UserManual_mrbeam2_fr.pdf', mrbeamdoc.get_file_name_with_extension())

    def test_none_extension(self):
        self.assertRaises(MrBeamDocNotFoundException,
                          get_doc_path,
                          MrBeamDocType.USER_MANUAL,
                          MrBeamModel.MRBEAM2_DC_R1,
                          SupportedLanguage.FRENCH,
                          extension=None)

    def test_empty_extension(self):
        self.assertRaises(MrBeamDocNotFoundException,
                          get_doc_path,
                          MrBeamDocType.USER_MANUAL,
                          MrBeamModel.MRBEAM2_DC_R1,
                          SupportedLanguage.FRENCH,
                          extension='')

    def test_blank_extension(self):
        self.assertRaises(MrBeamDocNotFoundException,
                          get_doc_path,
                          MrBeamDocType.USER_MANUAL,
                          MrBeamModel.MRBEAM2_DC_R1,
                          SupportedLanguage.FRENCH,
                          extension=' ')

    def test_when_not_pdf_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, get_doc_path,
                          MrBeamDocType.QUICKSTART_GUIDE,
                          MrBeamModel.DREAMCUT,
                          SupportedLanguage.ENGLISH,
                          'gif')

    def test_when_doc_available_and_language_not_available_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, get_doc_path,
                          MrBeamDocType.QUICKSTART_GUIDE,
                          MrBeamModel.DREAMCUT,
                          SupportedLanguage.FINNISH)

    def test_when_type_none_and_model_and_language_available_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, get_doc_path,
                          None,
                          MrBeamModel.MRBEAM2,
                          SupportedLanguage.ENGLISH)

    def test_when_model_none_and_type_and_language_available_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, get_doc_path,
                          MrBeamDocType.USER_MANUAL,
                          None,
                          SupportedLanguage.ENGLISH)

    def test_when_language_none_and_type_and_model_available_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, get_doc_path,
                          MrBeamDocType.USER_MANUAL,
                          MrBeamModel.MRBEAM2,
                          None)

    def test_when_language_available_and_type_and_model_none_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, get_doc_path,
                          None,
                          None,
                          SupportedLanguage.ENGLISH)

    def test_when_type_available_and_model_and_language_none_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, get_doc_path,
                          MrBeamDocType.USER_MANUAL,
                          None,
                          None)

    def test_when_doc_available_and_language_none_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, get_doc_path,
                          None,
                          MrBeamModel.MRBEAM2,
                          None)

    def test_when_type_model_and_language_none_then_raise_exception(self):
        self.assertRaises(MrBeamDocNotFoundException, get_doc_path,
                          None,
                          None,
                          None)

    def test_definitions_per_model(self):
        definitions = MrBeamDocAvailable.get_mrbeam_definitions_for(MrBeamModel.MRBEAM2)
        for definition in definitions:
            self.assertEquals(MrBeamModel.MRBEAM2, definition.mrbeam_model)
