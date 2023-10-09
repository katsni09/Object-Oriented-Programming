# Завдання 2:
#
# Створіть клас "Країна".
# Необхідно зберігати в полях класу: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни, назву столиці, назву міст країни.
# Реалізуйте доступ до окремих полів (Інкапсуляція).
class Country:
    def __init__(self, nameOfTheCountry, nameOfTheContinent, population, phoneCodeOfTheCountry, nameOfTheCapitalCity,
                 someCitiesOfTheCountry):
        self.__nameOfTheCountry = nameOfTheCountry
        self.__nameOfTheContinent = nameOfTheContinent
        self.__population = population
        self.__phoneCodeOfTheCountry = phoneCodeOfTheCountry
        self.__nameOfTheCapitalCity = nameOfTheCapitalCity
        self.__someCitiesOfTheCountry = someCitiesOfTheCountry

    # Методы для изменения ввода данных
    def setnameOfTheCountry(self, newNameOfTheCountry):
        self.__nameOfTheCountry = newNameOfTheCountry

    def setnameOfTheContinent(self, newNameOfTheContinent):
        self.__nameOfTheContinent = newNameOfTheContinent

    def setpopulation(self, newPopulation):
        self.__population = newPopulation

    def setphoneCodeOfTheCountry(self, newPhoneCodeOfTheCountry):
        self.__phoneCodeOfTheCountry = newPhoneCodeOfTheCountry

    def setnameOfTheCapitalCity(self, newNameOfTheCapitalCity):
        self.__nameOfTheCapitalCity = newNameOfTheCapitalCity

    def setsomeCitiesOfTheCountry(self, newSomeCitiesOfTheCountry):
        self.__someCitiesOfTheCountry = newSomeCitiesOfTheCountry

    def display_info(self):
        print(
            f" {self.__nameOfTheCountry}\t {self.__nameOfTheContinent}\t {self.__population}\t {self.__phoneCodeOfTheCountry}\t {self.__nameOfTheCapitalCity}, {self.__someCitiesOfTheCountry}")


nameOfTheCountry = Country("Ukraine", "Europe", "40 million", "+380", "Kyiv", "Kharkov, Mariupol, Sumy")
nameOfTheCountry2example = Country("Canada", "North America", "40 million", "+1", "Ottawa", "Montreal, Windsor, Toronto")
nameOfTheCountry.display_info()
nameOfTheCountry2example.display_info()

