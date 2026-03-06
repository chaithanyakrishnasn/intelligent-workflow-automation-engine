from enum import Enum


class ActionType(str, Enum):
    LOG = "log"


class TriggerType(str, Enum):
    WEBHOOK = "webhook"
    TIMER = "timer"
