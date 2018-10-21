'''
A leap year calculator:
every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
'''

def is_leap_year(year):

    four = year % 4
    hundred = year % 100
    fourHundred = year % 400

    if fourHundred == 0:
        return True
    elif four == 0 and hundred == 0:
        return False
    elif four == 0:
        return True
    else:
        return False
