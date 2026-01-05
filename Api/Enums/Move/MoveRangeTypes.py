from enum import Enum

class MoveRangeTypesEnum(Enum):
    FRONT = "X Grids In Front Of The User."
    ADJACENT = "X Adjacent Grids."
    AREA = "X Grids Around User."
    TARGET_IN_AREA = "Target Within X Grids Of The User."
    ALL_IN_RANGE = "X Grids Around The Target Including Target."
    ALL_IN_FRONT = "X Grids In Front Of The User"
    BATTLEFIELD = "Whole Battlefield."
    RANGED_OR_SPECIAL = "Whole Battlefield But Dice -1 Per 3 Grids Rounded Down."