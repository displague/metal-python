from enum import Enum


class PlanDeploymentTypesItem(str, Enum):
    ON_DEMAND = "on_demand"
    SPOT_MARKET = "spot_market"

    def __str__(self) -> str:
        return str(self.value)
