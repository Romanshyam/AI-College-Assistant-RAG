import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

print("Loaded:", key is not None)
print("First 5 characters:", key[:5] if key else None)
print("Length:", len(key) if key else 0)