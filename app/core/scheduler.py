from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.start()


def remove_job(job_id: str):
    try:
        scheduler.remove_job(job_id)
    except Exception:
        pass
