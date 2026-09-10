from src.tasks.celery_app import celery_instance


@celery_instance.task
def task_1():
    print("я обычная таска")


@celery_instance.task(name="beat_task")
def task_2():
    print("я периодическая таска")
