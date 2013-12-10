
def validate_height_weight(value):
    try:
        value =  float(value)
    except TypeError:
        raise Exception()
        return
    return value

def convert_height_inches_to_metres(height):
    try:
        height = validate_height_weight(height)
    except Exception:
        print "Height could not be converted from imperial to metric"

    height = Conversion.INCHES_TO_M * height 
    return height


def convert_pounds_to_kg(weight):
    try:
        weight = validate_height_weight(weight)
    except Exception:
        print "Weight could not be converted from imperial to metric"

    weight = Conversion.POUNDS_TO_KILOS * weight
    return weight



def henry_oxford_bmr(height,weight,age,gender):
    calPerDay = 0
    if age <= 0 or height <= 0 or  weight <= 0 or gender not in [0,1] :
            raise Exception("User details are invalid")
        
    if gender == 0:
        if age >= 0 and age < 3 :
            calPerDay = (28.2 * weight) + (895 * height) - 371
        elif age >= 3 and age < 10 :
            calPerDay = (15.1 * weight) + (72.4 * height) + 306
        elif age >= 10 and age < 18:
            calPerDay = (15.6 * weight) + (266 * height) + 299
        elif age >= 18 and age < 30:
            calPerDay = (14.4 * weight) + (313 * height) + 113
        elif age >= 30 and age < 60:
            calPerDay = (11.4 * weight) + (541 * height) - 137
        elif age >= 60:
            calPerDay = (11.4 * weight) + (541 * height) - 256
    elif gender == 1:
        if age >= 0 and age < 3:
            calPerDay = (30.4 * weight) + (703 * height) - 287
        elif age >= 3 and age < 10 :
            calPerDay = (15.9 * weight) + (210 * height) + 349
        elif age >= 10 and age < 18:
            calPerDay = (9.4 * weight) + (249 * height) + 462
        elif age >= 18 and age < 30:
            calPerDay = (10.4 * weight) + (615 * height) - 282
        elif age >= 30 and age < 60:
            calPerDay = (8.18 * weight) + (502 * height) - 11.6
        elif age >= 60:
            calPerDay = (8.52 * weight) + (421 * height) + 10.7

    return calPerDay

def BMI(height, weight):
    return weight / (height * height)

def main():
    age = 20
    height = 71
    weight = 185
    gender = 0

    height = convert_height_inches_to_metres(height)
    print "HEIGHT: " + str(height)

    weight = convert_pounds_to_kg(weight)
    print "WEIGHT: " + str(weight)

    calPerDay = henry_oxford_bmr(age = 20, height = height, weight = weight, gender = 0)
    print "BMR: " + str(calPerDay)

    bmi = BMI(height, weight)
    print "BMI :" + str(bmi)

main()
