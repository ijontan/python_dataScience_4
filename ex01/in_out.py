def square(x: int | float) -> int | float:
    """square function"""
    return x**2


def pow(x: int | float) -> int | float:
    """pow function"""
    return x**x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        value = x
        for _ in range(count):
            value = function(value)
        return value
    return inner
