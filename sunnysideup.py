import sdo

def sunny_side_up(lat, long):
    temperature = sdo.get_temperature(lat, long)
    energy_transfer = ((temperature-273)*1889.1)
    cooking_time_seconds = ((199.2*38)/energy_transfer)
    cooking_time_micros = cooking_time_seconds*1000000
    return(cooking_time_micros)

if __name__ == "__main__":
    print(sunny_side_up(0, 0))