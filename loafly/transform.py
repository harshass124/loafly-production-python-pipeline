
import logging
from .config import DISCOUNT_RATE

logger = logging.getLogger(__name__)


def transform_orders(data):
    transformed_data = []

    for row in data:
        try:
            raw_price = row.get("price")

            if raw_price is None or not str(raw_price).strip():
                raise ValueError("Price is missing")

            price = float(str(raw_price).replace(",", "").strip())

            discounted_price = price * (1 - DISCOUNT_RATE)

            row["price"] = discounted_price
            transformed_data.append(row)

        except (ValueError, TypeError, AttributeError) as e:
            logger.warning(
                "Skipping order %s due to invalid price: %s",
                row.get("order_id", "Unknown"),
                e
            )

        finally:
            logger.debug("Price processing attempt completed")

    return transformed_data
