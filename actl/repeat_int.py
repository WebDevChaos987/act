def repeat(action, nt):
    """
    Executes a given function multiple times.
    """
    for i in range(nt):
        action()
