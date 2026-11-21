
import os
import logging
import time

from dotenv import load_dotenv
from gateway import save_to_orders_api
from .config import RETRY_COUNT

load_dotenv()

logger = logging.getLogger(__name__)


def load_orders(data):

    api_key = os.getenv("LOAFLY_API_KEY")

    if not api_key:
        logger.warning("API key not found in environment")

    for row in data:
        order_id = row["order_id"]
        total = row["price"]

        for attempt in range(1, RETRY_COUNT + 1):
            try:
                response = save_to_orders_api(order_id, total)

                logger.info("Order %s saved successfully", order_id)
                break

            except ConnectionError as e:
                if attempt < RETRY_COUNT:
                    logger.warning(
                        "Attempt %s failed for order %s. Retrying...",
                        attempt,
                        order_id
                    )
                    time.sleep(2)
                else:
                    logger.error(
                        "Order %s failed after %s attempts: %s",
                        order_id,
                        RETRY_COUNT,
                        e
                    )

