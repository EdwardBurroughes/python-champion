from collections import defaultdict

dicty1 = {"hello": "world"}
dicty2 = {"gerald": "was-here"}

# old methods for merging dicts
print({**dicty1, **dicty2})

merged = dicty1.copy()
for key, values in dicty2.items():
    merged[key] = values

print(merged)
# both methods don't change the dict inplace can use update for this.
# however this does not return the merged output. Incomes "|" operater and "|="

# regular union
print(dicty1 | dicty2)
# inplace merge
dicty1 |= dicty2
print(dicty1)

# Benefit of using union operator is they maintain dictionary type object e.g. default-dict, OrderDicts etc
europe = defaultdict(lambda: "", {"Norway": "Oslo", "Spain": "Madrid"})
africa = defaultdict(lambda: "", {"Egypt": "Cairo", "Zimbabwe": "Harare"})

# maintains dict type
print(europe | africa)

# converts to a regular dict
print({**europe, **africa})