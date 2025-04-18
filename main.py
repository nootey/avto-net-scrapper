import sys
import asyncio
from src.internal.scheduler import start_scheduler
from src.internal.scraper import scrape
from src.shared.log import logger
from src.shared.config import params, scheduler_params, get_param_limits

async def main() -> None:

    param_limits = get_param_limits()
    brands = params["znamka"]
    selected_model = params["model"]
    is_all_brands = brands == [""] or len(brands) == 0
    is_all_models = selected_model == ""
    num_brands = len(brands)

    print()
    print("avto-net scrapper")
    print("-" * 40)

    print(f"Brand(s):      {'all' if is_all_brands else ', '.join(brands)}")
    print(f"Model(s):      {'all' if is_all_models else selected_model}")
    print(f"Max Pages:   {param_limits['max_pages']}")

    total_requests = num_brands * param_limits['max_pages']
    print(f"Estimated total requests:    {total_requests} per: {scheduler_params['interval_minute']} minute(s)")

    print("=" * 40)
    print()


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