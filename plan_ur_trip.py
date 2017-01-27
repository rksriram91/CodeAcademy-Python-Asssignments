def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if(city == 'Charlotte'):
        return 183
    elif(city == 'Tampa'):
        return 220
    elif(city == 'Pittsburgh'):
        return 222
    elif(city == 'Los Angeles'):
        return 475
    else:
        print 80

def rental_car_cost(days):
    if(days < 3):
        return days*40
    elif(days >= 3 and days <7):
        return (days*40-20)
    elif(days >= 7):
        return (days*40-50)
    else:
        print "Enter a valid number greater than 0"
        
def trip_cost(city,days,spending_money):
    total_cost=hotel_cost(days)+rental_car_cost(days)+plane_ride_cost(city)+spending_money
    return total_cost


print trip_cost("Los Angeles", 5, 600)