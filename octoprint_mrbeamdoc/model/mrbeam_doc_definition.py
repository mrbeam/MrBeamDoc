class MrBeamDocDefinition:
    """
    This class is meant to gather within the code what documents we are holding on in this project.

    This helps us organise and keep track of which document is implemented for which Mr Beam model and
    for which languages this document exists.

    Args:
        mrbeamdoc_type (MrBeamDocType): Document type for which this definition is valid
        mrbeam_model (MrBeamModel): Mr Beam model or alias for which this definition is valid
        supported_languages (List[SupportedLanguage]): Languages for which the combination of MrBeamDocType and MrBeamModel is available
        additionally_valid_models (List[MrBeamModel], optional):  additionally valid Mr Beam models that can be represented by this very same definition
    """

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
        return (self.mrbeamdoc_type == mrbeamdoc_type) and self.is_valid_for_model(
            mrbeam_model) and self.is_language_supported(language)
