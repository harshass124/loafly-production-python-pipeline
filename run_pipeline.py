
import logging

from loafly.extract import extract_orders
from loafly.transform import transform_orders
from loafly.load import load_orders

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("loafly.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("Pipeline started")

        # Extract
        raw_data = extract_orders()
        logger.info("Data extraction completed")

        # Transform
        transformed_data = transform_orders(raw_data)
        logger.info("Data transformation completed")

        # Load
        load_orders(transformed_data)

        logger.info("Pipeline completed successfully")

    except Exception:
        logger.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    main()

    