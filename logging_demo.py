import logging


def do_logging(log_file_name):

    # Basic logger
    logging.basicConfig(level=logging.INFO, filename=log_file_name, filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s"
                        )
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")

    x = 21766
    logging.info(f"The value of x is {x}")

    try:
        1 / 0
    except ZeroDivisionError:
        logging.error("ZeroDivError", exc_info=True)

    # Custom logger using name of program (__name__)
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler("custom.log")
    formatter = logging.Formatter("%(module)s : %(name)s - %(funcName)s - %(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Started")


print("Old School Logging.....")
do_logging("log.log")
