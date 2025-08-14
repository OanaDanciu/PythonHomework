import logging

# Creează logger principal
logger = logging.getLogger("math_service")
logger.setLevel(logging.INFO)

# Scrie în fișier
file_handler = logging.FileHandler("math_service.log")
file_handler.setLevel(logging.INFO)

# Scrie în consolă
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Format de log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adaugă handler-ele la logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
