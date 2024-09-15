car_speed = int(input('The speed of the car (Type only numbers): '))
road_limit = int(80)
fine_price = float(7.00)


def fine_final_price():
    excess_speed = car_speed - road_limit
    final_price = excess_speed * excess_speed
    return final_price


if car_speed <= road_limit:
    print(f'You speed was {car_speed}km/h')
    print(f'The Road limit is {road_limit}km/h')
    print('Keep it up')

elif car_speed > road_limit:
    print(f'You speed was \033[1;31;m{car_speed}km/h\033[m')
    print(f'The road limit is {road_limit}km/h')
    print('You just received a fine')
    print(f'Fine price: ${fine_final_price()}')
input('')
