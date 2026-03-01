from sqlalchemy import create_engine

engine = create_engine("postgresql://admin:12345@localhost:5432/skill_engine_db")

try:
    connection = engine.connect()
    print("Database connected successfully.")
    connection.close()
except Exception as e:
    print("Connection failed:", e)