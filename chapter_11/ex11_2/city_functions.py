def display_city_country(city, country, population=''):
    if population:
        message = f"{city.title()}, {country.title()} - population {population}"
    else:
        message = f"{city.title()}, {country.title()}"
    return message
