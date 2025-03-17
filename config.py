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
JWT_REFRESH_SECRET = env.get("JWT_REFRESH_SECRET")
JWT_ALGORITHM = env.get("JWT_ALGORITHM")
JWT_EXPIRE_MINUTES = int(env.get("JWT_EXPIRE_MINUTES"))
JWT_REFRESH_EXPIRE_DAYS = int(env.get("JWT_REFRESH_EXPIRE_DAYS"))
JWT_TOKEN_TYPE = env.get("JWT_TOKEN_TYPE")
