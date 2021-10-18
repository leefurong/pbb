import time

def time_reached(n, y, d, s, f, m):
    """
    m: 秒
    s: 时
    f: 分
    d: 天
    y: 月
    n: 年
    """
    return time.localtime().tm_sec >= m and time.localtime(
    ).tm_hour == s and time.localtime().tm_min == f and time.localtime(
    ).tm_mday == d and time.localtime().tm_mon == y and time.localtime(
    ).tm_year == n




if __name__=="__main__":
    pass