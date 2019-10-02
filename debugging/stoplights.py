market_second = {'ns': 'green', 'ew': 'red'}


def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # assertions are for programmer errors or "sanity checks"
    assert 'red' in intersection.values(), 'Neighter light is red!'
    + str(intersection)


print('before: ' + str(market_second))
switchLights(market_second)
print('after: ' + str(market_second))
