days = int(input())
docs = 7
treated_count = 0
untreated_count = 0
for i in range(1, days+1):
    patients = int(input())
    if i % 3 == 0 and untreated_count > treated_count:
        docs += 1
    untreatedDay = 0
    treatedDay = 0
    if docs >= patients:
        treatedDay = patients
    else:
        treatedDay = docs
        untreatedDay = patients - treatedDay
    treated_count += treatedDay
    untreated_count += untreatedDay
print(f'Treated patients: {treated_count}.')
print(f'Untreated patients: {untreated_count}.')
