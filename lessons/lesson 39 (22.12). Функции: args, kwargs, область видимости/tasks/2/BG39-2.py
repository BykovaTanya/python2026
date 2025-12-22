def prepare_request(**kwargs):
    if endpoint is _____:
        raise ValueError("endpoint is required")

    allowed_keys = {'timeout', 'retries'}

     for key, value in kwargs.items():
    control_params = {
        "endpoint": endpoint,
        "control": {
            "timeout": 5, 
            "retries": 3
        },
        "payload": {}
    }
    return control_params

 

print(prepare_request(endpoint="/stats", data=[1, 2]))

# output:
# {
#     "endpoint": "/stats",
#     "control": {"timeout": 5, "retries": 3},
#     "payload": {"data": [1, 2]}
# }

print(prepare_request(endpoint="/sync", timeout=10, retries=0, mode="fast"))
    
