num = int(input("Введите число от 1 до 100:"))
left = 1
right = 100
count = 0

while left <= right:
    count += 1
    center = (right + left) // 2
    if num == center:
        left = right = center
        break
    elif num > center:
        left = center + 1
    else:
        right = center - 1

print(count)
