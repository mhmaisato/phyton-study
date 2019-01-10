#calculate sin, cos and tan
import math
deg = float(input('Enter an angle: '))
rad = math.radians(deg)
print ('Sin for {}° is {:.4f}' .format(deg, math.sin(rad)))
print ('Cos for {}° is {:.4f}' .format(deg, math.cos(rad)))
print ('Tan for {}° is {:.4f}' .format(deg, math.tan(rad)))
