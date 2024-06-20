from src.libs.db.session_manager import instance_session
from src.modules.task.models import Task
from src.libs.log_handler import LogHandler

logger = LogHandler()


class TaskRepository:
    @staticmethod
    def create_task(task: Task):
        try:
            with instance_session() as session:
                breakpoint()
                # new_task = Task.from_orm(task)
                # session.add(new_task)
                # session.commit()
                # session.close()

                logger.info("new task added")

        except Exception as err:
            logger.error(err)
