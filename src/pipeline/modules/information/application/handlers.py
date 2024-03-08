from src.pipeline.seedwork.application.handlers import Handler


class DomainEventHandler(Handler):
    @staticmethod
    def handle_data_complete(self, event):
        raise NotImplementedError()

    @staticmethod
    def handle_png_map_present(self, event):
        raise NotImplementedError()