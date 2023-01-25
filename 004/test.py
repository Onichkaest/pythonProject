people = [('Jack', 'Smith', 18), ('Mary', 'Gold', 20)]
for person in people:
    print(person)

for name, surname, age in people:
    print(name, surname, age)

x = 0
while x < 100:
    print('I can\'t stop!', x)
    x += 1  # will run up to 99

dist_to_target = 1567
current_pos = 0
step = 0.6
cnt = 0
while current_pos < dist_to_target:
    print(cnt)
    current_pos += step
    cnt += 1

for x in range(10):
    if x == 5:
        continue  # for x = 5 will skip
    print(x)

for x in range(10):
    if x == 5:
        continue
    if x == 8:
        break  # will stop the cycle
    print(x)

cnt = 0  # starts with 0
while True:
    print(cnt)
    if cnt == 100:
        break
    cnt += 1  # adds 1 each time it runs

# if 5 > 10:
#     pass  # will ignore
# elif 5 < 10:





