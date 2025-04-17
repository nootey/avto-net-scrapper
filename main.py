import sys

from src.internal.scheduler import start_scheduler
from src.internal.scraper import scrape
from src.shared.log import logger

def main() -> None:
    try:
        logger.info("Starting initial scrape...")
        state = scrape(init=True)

        if state is not None:
            logger.info("Initial scrape successful.")
            logger.info("Starting scheduler...")
            start_scheduler()
        else:
            logger.warning("Scrape process failed or returned no data. Scheduler not started.")
            sys.exit(1)
    except Exception as e:
        logger.exception("An unexpected error occurred during main execution.")
        sys.exit(1)


if __name__ == "__main__":
    main()