city_status = {
    "city": "Москва", 
    "temperature": "20"
}

print(city_status["city"])

city_status["temperature"] = 25

print(city_status)

print(city_status.get("country"))

city_status["country"] = "Россия"

print(city_status)

city_status["date"] = "27.05.2019"

print(city_status)

print(len(city_status))