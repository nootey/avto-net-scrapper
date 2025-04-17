from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR, JobExecutionEvent
import pytz
from datetime import datetime

from src.shared.config import scheduler_params
from src.internal.scraper import scrape
from src.shared.log import logger


def start_scheduler() -> None:
    scheduler = BlockingScheduler()
    time_zone = pytz.timezone(scheduler_params['timezone'])

    def job_wrapper():
        logger.info("Scheduled scrape triggered.")
        scrape(init=False)

    def handle_job_error(event: JobExecutionEvent):
        logger.error(f"Scheduled job failed: {event.exception}", exc_info=True)

    scheduler.add_listener(handle_job_error, EVENT_JOB_ERROR)

    if scheduler_params['hourly'] == 1:
        scheduler.add_job(
            job_wrapper,
            'cron',
            hour=f"*/{scheduler_params['interval_hour']}",
            minute=scheduler_params['start_minute'],
            timezone=time_zone
        )
    else:
        scheduler.add_job(
            job_wrapper,
            'cron',
            minute=f"*/{scheduler_params['interval_minute']}",
            timezone=time_zone
        )

    logger.info(f"Scheduler started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler shut down gracefully.")
