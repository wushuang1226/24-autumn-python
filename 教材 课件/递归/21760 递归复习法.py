from functools import lru_cache
@lru_cache(maxsize=None)
def study_time(n):
    if n == 1 or n == 2:
        return n
    return n + study_time(n - 1) + study_time(n - 2)

#输入略