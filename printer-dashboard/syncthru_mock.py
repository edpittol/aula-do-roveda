_TONER_LEVELS = {
    "192.168.1.10": 5,   # critical
    "192.168.1.11": 72,  # ok
    # 192.168.1.99 → None (inaccessible, not in map)
}


def get_toner(ip):
    return _TONER_LEVELS.get(ip, None)
