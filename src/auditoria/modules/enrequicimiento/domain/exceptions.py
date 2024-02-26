from src.auditoria.seedwork.domain.exceptions import FactoryException


class InvalidTypeInAuditDomainException(FactoryException):
    def __init__(self, message='The type of the audit must be a string'):
        self.__message = message

    def __str__(self):
        return str(self.__message)
