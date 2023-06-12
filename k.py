reuso_values = []
limit = 64

for i in range(1, limit+1):
    if limit % i == 0:
        reuso_values.append(i)

print(reuso_values)
