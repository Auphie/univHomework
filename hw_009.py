def get_price_Discount(fruit):
    #['unit_price','step1_discount','step2_discount','step3_discount']
    if fruit == 'apple':
        bucket = [30, 0.95, 0.9, 0.8]
    elif fruit == 'kiwi':
        bucket = [70, 0.9, 0.85, 0.75]
    elif fruit == 'pineapple':
        bucket = [40, 0.85, 0.8, 0.8]
    return bucket

def countPrice(fruit, x):
    bucket = get_price_Discount(fruit)
    if x == 0:
        return 0
    elif x < 11:
        return bucket[0] * x
    elif x < 16:
        return bucket[0] * bucket[1] * x
    elif x < 21:
        return bucket[0] * bucket[2] * x
    else:
        return bucket[0] * bucket[3] * x

def finalDiscount(total_price, total_qty):
    if total_qty >= 30:
        return total_price * 0.87
    else:
        return total_price

total_price = 0
qty_apple = int(input())
total_price += countPrice('apple', qty_apple)
qty_kiwi = int(input())
total_price += countPrice('kiwi', qty_kiwi)
qty_pineapple = int(input())
total_price += countPrice('pineapple', qty_pineapple)
total_qty = qty_apple + qty_kiwi + qty_pineapple
final_price = int(finalDiscount(total_price, total_qty))
print(final_price)