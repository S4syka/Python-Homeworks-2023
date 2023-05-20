def unpack(l):
    res = []

    for item in l:
        if isinstance(item, dict):
            for key, value in item.items():
                res = res + unpack([key, value])
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            res = res + unpack(item)
        else:
            res.append(item)

    return res