def best_stock(data):
    return max(data, key=data.get)



print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))
print(best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}))

# test_dict = {"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}
# print(test_dict.values())