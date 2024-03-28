# def rec(items, capacity):
#     if len(items) = 0:
#         return 0
#     else:
#         maximum = 0
#         for item in items:
#             pass

def bnb(items, capacity):
    items = sorted(items, key=lambda x: x[2] / x[1])
    return items

if __name__ == '__main__':
    capacity = 9

    # Utility, weight
    items = [
        (1, 20, 3),
        (2, 16, 2),
        (3, 24, 5),
        (4, 14, 4),
        (5, 9, 2)
    ]
