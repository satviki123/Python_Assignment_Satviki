def aggregate_weather_data(records):
    city_data={} # Dictionary to store aggregated data for each city

    for record in records: # Validations
        city=record.get('city')
        temperature=record.get('temperature')
        humidity=record.get('humidity')

        if city not in city_data:
            city_data[city]={'total_temp': 0, 'total_humidity': 0, 'count': 0}

        if temperature is not None:
            city_data[city]['total_temp']+=temperature
        if humidity is not None:
            city_data[city]['total_humidity']+=humidity
        
        city_data[city]['count']+=1
         
    average_weather={}     # Dictionary to store average weather data for each city
    for city, data in city_data.items():   # Finding Aggregations 
        avg_temp=data['total_temp']/data['count'] if data['count'] > 0 else None
        avg_humidity=data['total_humidity']/data['count'] if data['count'] > 0 else None
        average_weather[city]={
            'average_temperature':avg_temp,
            'average_humidity':avg_humidity
        }

    return average_weather
    
# Main Function
if _name_ == "_main_":
    records = [
        {'city': 'Palakol','temperature': 75,'humidity': 60},
        {'city': 'Palakol','temperature': 80},
        {'city': 'Bhimavaram','humidity': 50},
        {'city': 'Bhimavaram','temperature': 85,'humidity': 55},
        {'city': 'Tanuku','temperature': 70,'humidity': 65},
        {'city': 'Tanuku','humidity': 70}
    ]
    
    print(aggregate_weather_data(records))