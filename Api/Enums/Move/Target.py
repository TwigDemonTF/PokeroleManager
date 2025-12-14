from enum import Enum

class TargetEnum(Enum):
    User = "User"
    SingleTeam = "Single Team"
    UserAndAllTeamInRange = "User And Team In Range"
    SingleEnemy = "Single Enemy"
    RandomEnemy = "Random Enemy"
    AllEnemyInRange = "All Enemies In Range"
    Area = "Area"
    Battlefield = "Battlefield"