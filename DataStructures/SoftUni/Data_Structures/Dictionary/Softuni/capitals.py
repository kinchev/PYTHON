country = input().split(", ")
capitals = input().split(", ")

zip_dict = list(zip(country, capitals))

[print(f'{k} -> {v}') for (k, v)in zip_dict]




# Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London
