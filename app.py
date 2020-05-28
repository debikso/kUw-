continentName = {
    "Africa": ["Nigeria", "Ghana", "South Africa"],
    "Europe": ["Belgium", "Germany", "France"],
    "South America": ["Brazil", "Peru", "Argentina"],
    "Australia": ["French Polynesia", "Fiji", "New Zealand"],
    "North America": ["Canada", "Mexico", "Jamaica"],
    "Asia": ["Thailand", "Singapore", "Vietnam"],

}

total_case_numbers = {
    "Africa": [37230, 15433, 687, 21100],
    "Europe": [420254, 241114, 46050, 133090],
    "South America": [497248, 203438, 26654, 267156],
    "Australia": [1582, 1531, 21, 30],
    "North America": [153871, 91620, 13827, 48424],
    "Asia": [35328, 18076, 80, 17172]
}

cases = ["affected", "discharged", "deaths", "active"]

welcome = "You are welcome to your daily corona virus report channel."
print(welcome)
print("There are three countries per continent available in this report.")

inquiry = input("\nWhich continent's report will you like to see?: ")

for (key, value), (key2, value2) in zip(continentName.items(), total_case_numbers.items()):
    if inquiry == key:
        print(key, value)
        print(key2, value2)
        print(cases)
# this code is meant to print max and min countries in the continent
        print(max(total_case_numbers, key=total_case_numbers.get))
        print(min(total_case_numbers, key =total_case_numbers.get))
# This is what i could come up with, not satisfied with it though but ..