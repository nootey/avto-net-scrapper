from apscheduler.schedulers.blocking import BlockingScheduler
from src.shared.config import scheduler_params
from src.internal.scraper import scrape
import pytz
from datetime import datetime

def start_scheduler():
    scheduler = BlockingScheduler()
    time_zone = pytz.timezone(scheduler_params['timezone'])

    if scheduler_params['hourly'] == 1:
        scheduler.add_job(scrape, 'cron', hour=f"*/{scheduler_params['interval_hour']}", minute=scheduler_params['start_minute'], args=[False], timezone=time_zone)
    else:
        scheduler.add_job(scrape, 'cron', minute=f"*/{scheduler_params['interval_minute']}", args=[False], timezone=time_zone)

    print('Scheduler started at {}'.format(datetime.now()))
    scheduler.start()
