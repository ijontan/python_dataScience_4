

def ft_mean(*args: any) -> float:
    """mean function"""
    return sum(args)/len(args)


def ft_median(*args: any) -> float:
    """median function"""
    s_args = sorted(args)
    if len(args) % 2 == 0:
        return (s_args[len(args)//2-1] + s_args[len(args)//2])/2
    return s_args[len(args)//2]


def ft_quartile(*args: any) -> list:
    """quartile function"""
    s_args = sorted(args)
    first_q = s_args[len(args)//4]
    third_q = s_args[len(args)//4*3]
    if len(args) % 2 == 0:
        first_q = (s_args[len(args)//4-1] + s_args[len(args)//4])/2
        third_q = (s_args[len(args)//4*3-1] + s_args[len(args)//4*3])/2
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
