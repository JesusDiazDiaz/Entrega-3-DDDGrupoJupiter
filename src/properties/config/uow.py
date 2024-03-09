from src.properties.config.db import db
from src.properties.seedwork.infrastructure.uow import UnitOfWork, Batch


class SQLAlchemyUnitOfWork(UnitOfWork):

    def _clear_batches(self):
        self._batches = list()

    def __init__(self):
        self._batches: list[Batch] = list()

    def __enter__(self) -> UnitOfWork:
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()

    @property
    def savepoints(self):
        return list[db.session.get_nested_transaction()]

    @property
    def batches(self) -> list[Batch]:
        return self._batches

    def commit(self):
        for batch in self.batches:
            lock = batch.lock
            batch.operation(*batch.args, **batch.kwargs)

        db.session.commit()

        super().commit()

    def rollback(self, savepoint=None):
        if savepoint:
            savepoint.rollback()
        else:
            db.session.rollback()

        super().rollback()

    def savepoint(self):
        db.session.begin_nested()