import logging 

logger = logging.getLogger("App")

# Set the level of the logger. This is the global level of logging messages that will be handled.
logger.setLevel(logging.INFO)

# Create handlers
c_handler = logging.StreamHandler()  # For console
f_handler = logging.FileHandler("./app.log")  # For file
c_handler.setLevel(
    logging.INFO
)  # Console handler deals with warning and above levels
f_handler.setLevel(
    logging.INFO
)  # File handler deals with debug and above levels

# Create formatters and add them to the handlers
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)