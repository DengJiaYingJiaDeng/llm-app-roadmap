import os


app_name = os.getenv("APP_NAME", "Default App")
api_key = os.getenv("API_KEY")

print(f"APP_NAME={app_name}")
print(f"API_KEY exists={api_key is not None}")
