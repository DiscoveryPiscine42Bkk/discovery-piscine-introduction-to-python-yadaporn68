def famous_births(figures):

    sorted_figures = sortded(figures,valnes(),key=lambda person: int(person["date_of_birth"]))

    for person in sorted_fingures:
        print(f'{person["name"]}is a great scientist born in {person["date_of_birth"]}.')

scientinsts = {
    "a": {"name": "G", "date_of_birth": "3333"},
    "b": {"name": "E", "date_of_birth": "6666"},
    "c": {"name": "N", "date_of_birth": "1000"},
    "d": {"name": "O", "date_of_birth": "2007"}
}

famous_births(scientists)