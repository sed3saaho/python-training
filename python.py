cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13_960_000,
        'language': 'japanese',
        'famouse landmark': 'tokyo tower',
        'currency': 'Japanese Yen (JPY)',
        'fact': 'Tokyo is the most populous metropolitan area in the world, with over 37 million people living in its greater region.',
    },
    'paris': {
        'country': 'france',
        'population': 2_160_000,
        'language': 'french',
        'famouse landmark': 'eiffel tower',
        'currency': 'Euro(EUR)',
        'fact': 'The Eiffel Tower was originally meant to be a temporary structure for the 1889 Worlds Fair — it was almost torn down afterward!',

    },
    'nairobi': {
        'country': 'kenya',
        'population': 4_400_000,
        'language': 'swahili and english',
        'famouse landmark': 'nairobi national park',
        'currency': 'Kenyan Shilling (KES)',
        'fact': 'The city s iconic Times Square was named after The New York Times newspaper in 1904.'

    },
}
for city, city_info in cities.items():
    print(f"\nBelow are the details of {city.upper()}, City")
    country = city_info['country']
    population = city_info['population']
    language = city_info['language']
    famouse_landmark = city_info['famouse landmark']
    currency = city_info['currency']
    fact = city_info['fact']
    print(f"\tIts a city in {country.title()}")
    print(f"\tThe population in this {city.title()} is roughly {population}")
    print(f"\tThe popular language in {city.title()} is {language.title()}")
    print(f"\tThe famouse landmark in {city.title()} is {famouse_landmark.title()}")
    print(f"\tThe currency used is {currency}")
    print(f"\tAnd a common fact about {city.title()} is: {fact}")