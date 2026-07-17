from app.database.database import Base, engine
from app.database.models import Message

Base.metadata.create_all(bind=engine)

print("Database created successfully.")