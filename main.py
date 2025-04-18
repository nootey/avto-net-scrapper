# main.py
import sys
import asyncio
from src.internal.scheduler import start_scheduler
from src.internal.scraper import scrape
from src.shared.log import logger

async def main() -> None:
    try:
        logger.info("Starting initial scrape...")
        state = await scrape(init=True)

        if state is not None:
            logger.info("Initial scrape successful.")
            logger.info("Starting scheduler...")
            await start_scheduler()
        else:
            logger.warning("Scrape process failed or returned no data. Scheduler not started.")
            sys.exit(1)
    except Exception:
        logger.exception("An unexpected error occurred during main execution.")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())