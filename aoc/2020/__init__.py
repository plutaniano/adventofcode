for day in range(1, 26):
    try:
        __import__(f"aoc.2020.day{day:02}", fromlist=["Solution"])
    except ImportError:
        pass
