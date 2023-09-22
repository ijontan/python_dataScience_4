

def ft_mean(*args: any) -> float:
    """mean function"""
    return sum(args)/len(args)


def ft_median(*args: any) -> float:
    """median function"""
    return sorted(args)[len(args)//2]


def ft_quartile(*args: any) -> list:
    """quartile function"""
    first_q = sorted(args)[len(args)//4]
    third_q = sorted(args)[len(args)//4*3]
    return [float(first_q), float(third_q)]


def ft_var(*args: any) -> float:
    """var function"""
    mean = ft_mean(*args)
    return sum([(arg - mean)**2 for arg in args]) / len(args)


def ft_std(*args: any) -> float:
    """std function"""
    return ft_var(*args)**0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """statistics function"""
    for _, value in kwargs.items():
        try:
            assert len(args) > 0
            if value == "mean":
                print(f"mean: {ft_mean(*args)}")
            if value == "median":
                print(f"median: {ft_median(*args)}")
            if value == "quartile":
                print(f"quartile: {ft_quartile(*args)}")
            if value == "std":
                print(f"std: {ft_std(*args)}")
            if value == "var":
                print(f"var: {ft_var(*args)}")
        except ZeroDivisionError:
            print("Error: division by zero")
        except TypeError:
            print("Error: only numbers")
        except Exception:
            print("ERROR")
