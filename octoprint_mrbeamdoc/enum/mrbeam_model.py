from enum import Enum


class MrBeamModel(Enum):
    """
    In this Enum we collect the different MrBeam models we have developed and the aliases by which we know them.
    """
    MRBEAM2 = 'mrbeam2'
    MRBEAM2_DC_R1 = 'mrbeam2_dc_r1'
    MRBEAM2_DC_R2 = "mrbeam2_dc_r2"
    DREAMCUT_ALIAS = 'dreamcut'
    DREAMCUT = 'mrbeam2_dc'
    DREAMCUT_S = "mrbeam2_dc_s"
