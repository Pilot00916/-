def global_function():
    msg = 1

    def local_function():
        nonlocal msg
        msg = 2
    local_function()
    return msg
