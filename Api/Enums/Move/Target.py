from enum import Enum

class TargetEnum(Enum):
    USER = "User"
    SINGLE_TEAM = "Single Team"
    USER_AND_ALL_IN_RANGE = "User And Team In Range"
    SINGLE_ENEMY = "Single Enemy"
    RANDOM_ENEMY = "Random Enemy"
    ALL_ENEMY_IN_RANGE = "All Enemies In Range"
    AREA = "Area"
    BATTLEFIELD = "Battlefield"