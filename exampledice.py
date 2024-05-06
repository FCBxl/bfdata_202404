import random
def dice(dice_number=2, faces=6):
    total = 0

    for n in range(dice_number):
        result = random.randint(1,faces)
        total += result
    return total
print(dice(faces=20))