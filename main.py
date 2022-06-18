import phonenumbers
from test import number
from phonenumbers import geocoder
country_name=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(country_name,"en"))
from phonenumbers import carrier
service_provider=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))
