q = ["hello and word and back and front"]

result = []
for x in q:
    data = list(x.split())
    result.append([a for a in data if a != "and"])

print(result)

