def input_params():
    voice_in = int(input())
    voice_out = int(input())
    local = int(input())
    text_in = int(input())
    text_out = int(input())
    return [voice_in, voice_out, local, text_in, text_out]

def calculate_price(plan, params):
    price = 0
    for i in range(len(params)):
        price += params[i]*plan[i+1]
    return price if price > plan[0] else plan[0]

def check_cheapest(*plan):
    min_price = plan[0][1]
    index = 0
    for i in range(len(plan)):
        if plan[i][1] < min_price:
            min_price = plan[i][1]
            index = i
    print(plan[index][0])

plan_183 = [183, 0.08, 0.1393, 0.1349, 1.1287, 1.4803]
plan_383 = [383, 0.07, 0.1304, 0.1207, 1.1127, 1.2458]
plan_983 = [983, 0.06, 0.1087, 0.1018, 0.9572, 1.1243]
params = input_params()
# params = [10000,100,100,100,100]

price_183 = calculate_price(plan_183, params)
price_383 = calculate_price(plan_383, params)
price_983 = calculate_price(plan_983, params)
check_cheapest(['Type 183',price_183], ['Type 383',price_383], ['Type 983',price_983])