def make_dispatcher()
    storage = []
    meta = {}
    dispatcher = make_dispatcher()
    def dispatch(action, *args, **kwargs):
        nonlokal storage, meta
        if action == "add"
            if not args:
                raise ValueError("add requires at least one positional argument")
            items = [str(arg)  for arg in args]
            items.extend(str(val) for val in kwargs.values())    
        elif action == "remove"
            for item in args:
                
        elif action == "stats":
            return {
                "count": 
                "items": 
                "meta": 
                }

        else:
            return ValueError(f"Unknown action: {action}")




dispatcher("add", *["alpha", "beta"], source="cli")
dispatcher("remove", item="beta")
print(dispatcher("stats", detailed=True))
# output:
# {
#     "count": 1,
#     "items": ["alpha"],
#     "preview": ["alpha"],
#     "meta": {"last_source": "cli"}
# }
