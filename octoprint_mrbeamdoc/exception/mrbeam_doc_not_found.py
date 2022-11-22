class MrBeamDocNotFoundException(Exception):
    """Raised when the file requested is not found in the system"""

    def __init__(self, mrbeamdoc_type, mrbeam_model, language):
        super(MrBeamDocNotFoundException, self).__init__(
            'The MrBeamDocType requested -> %(mrbeamdoc_type)s does not exist in the specified mrbeam_model -> %(mrbeam_model)s and language -> %(language)s' % {
                'mrbeamdoc_type': mrbeamdoc_type, 'mrbeam_model': mrbeam_model, 'language': language})
