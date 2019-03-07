import logging


def enable_console_debug_logging():  # pragma no cover (Function useful only outside test environment)
    """
    This function sets up a very simple logging configuration (log everything on standard output) that is useful for troubleshooting.
    """
    logger = logging.getLogger("fineract")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
