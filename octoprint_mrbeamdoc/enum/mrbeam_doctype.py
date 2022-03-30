from enum import Enum


class MrBeamDocType(Enum):
    """
    This enum represents the document type's we manage in this project.
    Each document can be in different languages and for different models of MrBeam devices
    """
    USER_MANUAL = 'UserManual'
    QUICKSTART_GUIDE = 'QuickstartGuide'
