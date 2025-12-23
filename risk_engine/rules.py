from enum import Enum

class RiskLevel(str, Enum):
    SAFE = "SAFE"
    DOUBTFUL = "DOUBTFUL"
    INSECURE = "INSECURE"


# Reglas iniciales (placeholder)
# Estas reglas luego se alimentarán con datos reales (CVEs)
DEFAULT_RULES = {
    "express": RiskLevel.SAFE,
    "lodash": RiskLevel.DOUBTFUL,
    "jsonwebtoken": RiskLevel.INSECURE
}
