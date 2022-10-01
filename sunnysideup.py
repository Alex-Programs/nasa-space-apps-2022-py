def sunny_side_up(temperature):
    energy_transfer = ((temperature-273)*1889.1)
    cooking_time_seconds = ((199.2*38)/energy_transfer)
    cooking_time_micros = cooking_time_seconds*1000000
    return(cooking_time_micros)