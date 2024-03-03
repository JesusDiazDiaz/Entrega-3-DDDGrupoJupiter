from src.companies.seedwork.application.handlers import Handler


class DomainEventHandler(Handler):
    @staticmethod
    def handle_enriched_information(self, event):
        raise NotImplementedError()