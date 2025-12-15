def update_profile(user_id, name, settings = None, is_active = True, tags = None):
    if settings is None:
        settings = {}
    if tags is None:
        tags = []
    update_profile = {
        "user_id": user_id,
        "name": name,
        "settings": settings,
        "is_active": is_active,
        "tags": tags
    }
    return update_profile

result = update_profile(101, "Анна")
print(result) 
result = update_profile(name="Борис", user_id=202, is_active=False)
print(result)
