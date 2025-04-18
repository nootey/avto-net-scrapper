import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.events import EVENT_JOB_ERROR, JobExecutionEvent
import pytz
import time
from src.shared.config import scheduler_params
from src.internal.scraper import scrape
from src.shared.log import logger

async def run_scrape_job():
    start = time.time()
    logger.info("Scheduled scrape triggered.")
    await scrape(init=False)
    end = time.time()
    logger.info(f"Scrape completed in {end - start:.2f} seconds.")

def handle_job_error(event: JobExecutionEvent):
    logger.error(f"Scheduled job failed: {event.exception}", exc_info=True)

async def start_scheduler() -> None:
    scheduler = AsyncIOScheduler()
    scheduler.add_listener(handle_job_error, EVENT_JOB_ERROR)

    time_zone = pytz.timezone(scheduler_params['timezone'])

    if scheduler_params['hourly'] == 1:
        scheduler.add_job(
            run_scrape_job,
            'cron',
            hour=f"*/{scheduler_params['interval_hour']}",
            minute=scheduler_params['start_minute'],
            timezone=time_zone
        )
    else:
        scheduler.add_job(
            run_scrape_job,
            'cron',
            minute=f"*/{scheduler_params['interval_minute']}",
            timezone=time_zone
        )

    scheduler.start()

    next_run = scheduler.get_jobs()[0].next_run_time
    logger.info(f"Scheduler started — next run at: {next_run.strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler shut down gracefully.")