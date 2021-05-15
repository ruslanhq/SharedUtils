from enum import Enum


class MaillerEnum(Enum):
    welcome = ['company', 'date']
    reset_password = ['password', 'recovery_link']
