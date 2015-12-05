from enum import Enum


class Category(Enum):
    LifeConFirmation     = "安否確認"
    HelpObject           = "物資要請"
    AssistantRequest     = "救助"
    HelpRequest          = "支援要請"
    Emergency            = "緊急支援"
    LifeLine             = "ライフライン"
    TransPortation       = "交通機関"
    HouseInformation     = "住宅情報"
    HealthInformation    = "医療・福祉・健康相談"
    LifeCareInformation  = "生活支援・相談"
    NoSetting            = "NoSetting"

