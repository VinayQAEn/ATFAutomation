import configparser

config = configparser.RawConfigParser()
config.read("/Users/riyabakoria/ATPAutomation/Configuration/config.ini")

class ReadConfig:
    @staticmethod
    def get_name():
        return config.get('commondata', 'name')

    @staticmethod
    def get_email():
        return config.get('commondata', 'email')

    @staticmethod
    def get_phone():
        return config.get('commondata', 'phone')

    @staticmethod
    def get_address():
        return config.get('commondata', 'address')

    