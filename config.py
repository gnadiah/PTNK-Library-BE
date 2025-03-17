from dotenv import dotenv_values

env = dotenv_values(".env")

# Database configurations
DB_USER = env.get("DB_USER")
DB_PASS = env.get("DB_PASS")
DB_HOST = env.get("DB_HOST")
DB_PORT = env.get("DB_PORT")
DB_NAME = env.get("DB_NAME")

# JWT configurations
JWT_SECRET = env.get("JWT_SECRET")
JWT_ALGORITHM = env.get("JWT_ALGORITHM")

print(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
