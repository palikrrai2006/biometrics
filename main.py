from database.user_repository import save_user

save_user("TestUser", [0.1, 0.2, 0.3])
print("MongoDB Connected Successfully")
Remove-Item config,database,services,utils -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item app.py,main.py,b.py,README.md,requirements.txt,.env -Force -ErrorAction SilentlyContinue
