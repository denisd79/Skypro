from address import Address
from mailing import Mailing

# Создание адресов
to_address = Address("123456", "Город1", "Улица1", "Дом1", "Квартира1")
from_address = Address("654321", "Город2", "Улица2", "Дом2", "Квартира2")

# Создание почтового отправления
mailing = Mailing(to_address, from_address, 100, "TRACK123")

# Вывод информации о почтовом отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")