from enum import Enum

class TargetEnum(Enum):
    User = "User"
    SingleTeam = "SingleTeam"
    UserAndAllTeamInRange = "UserAndAllTeamInRange"
    SingleEnemy = "SingleEnemy"
    RandomEnemy = "RandomEnemy"
    AllEnemyInRange = "AllEnemyInRange"
    Area = "Area"
    Battlefield = "Battlefield"