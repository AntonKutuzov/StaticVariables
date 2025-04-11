from functools import wraps
from typing import  Any, Dict


def static(static_vars: Dict[str, Any]):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        for a, p in static_vars.items():
            setattr(wrapper, a, p)

        return wrapper
    return decorator


def counter(
        start_with: int = 0,
        step: int = 1,
        inc: bool = True,
        min: int = 0,
        max: int = None
        ):

    def decorator(func):
        @static({'counter': start_with})
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            old_value = wrapper.counter
            wrapper.counter += step * (1 if inc else -1)

            if min is not None and wrapper.counter < min:
                wrapper.counter = old_value
            elif max is not None and wrapper.counter > max:
                wrapper.counter = old_value
            else:
                pass

            return result

        return wrapper
    return decorator


def flags(
        *flag_names: str,
        default: bool = False,
        ):

    def decorator(func):

        @static(dict([(name, default) for name in flag_names]))
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
    return decorator
