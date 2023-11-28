import os
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for key, value in student_scores.items():
    if value > 90:
        student_grades[key] = "Outstanding"
    elif value > 80:
        student_grades[key] = "Exceeds Expectation"
    elif value > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
#print(student_scores)
#print(student_grades)

travel_log = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Little", "Dijon"],
        "number_of_visits": 5
    },
    {
        "Country": "Germany",
        "cities_visites": ["Berlin", "Hamburg", "Stuttgart"],
        "number_of_visits": 5
    },
]
print(travel_log)
def add_new_country(country, number_of_visits, cities_visited):
    new_dict = {
        "Country": country,
        "cities_visited": cities_visited,
        "number_of_visits": number_of_visits
    }
    travel_log.append(new_dict)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
clear = input("Do you want to clear screen? ")
if clear == 'yes':
    os.system('clear')
