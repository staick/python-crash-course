# 8-14. Cars
def make_car(manufacturer, model, **infors):
    car_infor = {}
    car_infor['manufacturer'] = manufacturer
    car_infor['model'] = model
    for key, value in infors.items():
        car_infor[key] = value
    return car_infor

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
