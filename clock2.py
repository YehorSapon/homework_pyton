'''HW digital clock.'''

import datetime
from time import strftime

now = datetime.datetime.now()
time_string = strftime("%H:%M:%S")
hour1 = time_string[0:1]
hour2 = time_string[1:2]
minutes1 = time_string[3:4]
minutes2 = time_string[4:5]
secundes1 = time_string[6:7]
secundes2 = time_string[7:8]
print(hour1 + hour2 + ':' + minutes1 + minutes2 + ':' + secundes1 + secundes2)

zero = [
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B'
        ]

one = [
        '\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1C\u2B1B'
        ]

two = [
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B'
        ]

tre = ['\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
       '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
       '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
       '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
       '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
       '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B'
       ]
        
four = [
        '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B'
        ]

five = [
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B'
        ]

six = [
       '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
       '\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B',
       '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
       '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
       '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
       '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B'
       ]

seven = [
         '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
         '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
         '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
         '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
         '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
         '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B'
        ]
        
eight = [
         '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
         '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
         '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
         '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
         '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
         '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B'
         ]
        
nine = [
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B',
        '\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B'
        ]
        
first_dots = [
              '\u2B1B',
              '\u2B1C',
              '\u2B1B',
              '\u2B1B',
              '\u2B1C',
              '\u2B1B'
              ]

second_dots = [
               '\u2B1B',
               '\u2B1B',
               '\u2B1B',
               '\u2B1B',
               '\u2B1B',
               '\u2B1B'
               ]

digits = {
        "0": zero,
        "1": one,
        "2": two,
        "3": tre,
        "4": four,
        "5": five,
        "6": six,
        "7": seven,
        "8": eight,
        "9": nine,
        }
dots = {
        ":": first_dots,
        " ": second_dots,
        }

digital_clock = [
                 digits[hour1],
                 digits[hour2],
                 digits[minutes1],
                 digits[minutes2],
                 digits[secundes1],
                 digits[secundes2]
                 ]
for i in range(8):
        print(digital_clock = [
                                digits[hour1[i]],
                                digits[hour2[i]],
                                digits[minutes1[i]],
                                digits[minutes2[i]],
                                digits[secundes1[i]],
                                digits[secundes2[i]]
                                ])
