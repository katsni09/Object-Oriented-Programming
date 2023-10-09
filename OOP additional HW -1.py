# Завдання 1:
#
# Створіть клас "Місто".
# Необхідно зберігати в полях класу:
# назву міста, назву регіону, назву країни, кількість жителів міста, поштовий індекс міста, телефонний код міста.
# Реалізуйте доступ до окремих полів (Інкапсуляція).
class City:
    def __init__(self, nameOfTheCity, nameOfTheRegion, nameOfTheCountry, population, postalCode, phoneCodeOfTheCity):
        self.__nameOfTheCity = nameOfTheCity
        self.__nameOfTheRegion = nameOfTheRegion
        self.__nameOfTheCountry = nameOfTheCountry
        self.__population = population
        self.__postalCode = postalCode
        self.__phoneCodeOfTheCity = phoneCodeOfTheCity
# Методы для изменения ввода данных
    def changenameOfTheCity (self, newNameOfTheCity):
        self.__nameOfTheCity = newNameOfTheCity
    def changenameOfTheRegion (self, newnameOfTheRegion):
        self.__nameOfTheRegion = newnameOfTheRegion
    def nameOfTheCountry (self, newnameOfTheCountry):
        self.__nameOfTheCountry = newnameOfTheCountry
    def population (self, newPopulation):
        self.__population= newPopulation
    def postalCode (self, newPostalCode):
        self.__postalCode= newPostalCode
    def phoneCodeOfTheCity (self, newPhoneCodeOfTheCity):
        self.__phoneCodeOfTheCity= newPhoneCodeOfTheCity

    def display_info(self):
        print(f" {self.__nameOfTheCity}\t {self.__nameOfTheRegion}\t {self.__nameOfTheCountry}\t {self.__population}\t {self.__postalCode}, {self.__phoneCodeOfTheCity}")

nameOfTheCity = City("Odesa", "Odesa Oblast", "Ukraine", "1 million", "61000", "+38066")
nameOfTheCity2example = City("Kyiv", "Kyiv Oblast", "Ukraine", "2 million", "61000", "+38099")
nameOfTheCity.display_info()
nameOfTheCity2example.display_info()