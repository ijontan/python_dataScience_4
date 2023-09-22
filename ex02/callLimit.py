def callLimit(limit: int):
    """callLimit function"""
    count = 0

    def callLimiter(function):
        """callLimiter function"""
        def limit_function(*args: any, **kwds: any):
            """limit_function function"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
