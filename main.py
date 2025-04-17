from src.internal.scheduler import start_scheduler
from src.internal.scraper import scrape
from datetime import datetime
import traceback

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    try:
        log("Starting initial scrape...")
        state = scrape(init=True)

        if state is not None:
            log("Initial scrape successful.")
            log("Starting scheduler...")
            start_scheduler()
        else:
            log("Initial scrape failed or returned no data. Scheduler not started.")

    except Exception as e:
        log("An unexpected error occurred!")
        traceback.print_exc()

if __name__ == "__main__":
    main()
