dc = {
        'saewookkang': 700,
        'corncheese': 850,
        'kkokkalcorn': 750
    }  

if 'homerunball' not in dc:
    dc['homerunball'] = 900

print(dc)

for i in dc:
    dc[i] += 100
    
print(dc)

if 'corncheese' in dc:
    del dc['corncheese']
if 'cheesecorn' not in dc:
    dc['cheesecorn'] = 950

print(dc)
