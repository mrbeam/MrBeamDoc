import os

from octoprint_mrbeamdoc import DOC_ROOT_PATH


class MrBeamDoc:
    """
    This class gathers the naming convention and path location of all the files managed by this plugin.
    An instance of this class should be used to find the path of the file needed abstracting the implementation
    from the rest of the code.
    """

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
        return os.path.join(DOC_ROOT_PATH, 'docs')

    def get_file_name_with_extension(self):
        return '%(mrbeamdoc_type)s_%(mrbeam_model)s_%(language)s.%(extension)s' % {
            'mrbeamdoc_type': self.definition.mrbeamdoc_type.value,
            'mrbeam_model': self.definition.mrbeam_model.value,
            'language': self.language.value,
            "extension": self.extension}

    def get_file_reference(self):
        return os.path.join(self.get_folder(), self.get_file_name_with_extension())
