def dedupe_preserve_order(items):
    return list(dict.fromkeys(items))
print(dedupe_preserve_order([3, 1, 3, 2, 1]))