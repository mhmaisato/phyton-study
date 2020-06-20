#radar
#read a car speed, if upper 80km/h, show a message informing that receive a fine
veloc = float(input('Enter car`s speed: '))
if veloc > 80:
    print ('Your speed is upper than 80km/h. \nYou receive a fine.')
    fine = (veloc - 80) * 7.00
    print ('You have to pay R$.'.format(fine))
else:
    print ('Congrats you are driving safety.')

