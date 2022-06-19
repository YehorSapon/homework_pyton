'''HW digital clock.'''

import datetime
import os
from time import sleep
from time import strftime

while True:
        
        time_string = strftime("%H:%M:%S")
        hour1 = time_string[0:1]
        hour2 = time_string[1:2]
        minutes1 = time_string[3:4]
        minutes2 = time_string[4:5]
        secundes1 = time_string[6:7]
        secundes2 = time_string[7:8]
        
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
        

        digital_clock = [
                        digits[hour1],
                        digits[hour2],
                        digits[minutes1],
                        digits[minutes2],
                        digits[secundes1],
                        digits[secundes2]
                        ]

        d1 = digital_clock[0]
        d2 = digital_clock[1]
        d3 = digital_clock[2]
        d4 = digital_clock[3]
        d5 = digital_clock[4]
        d6 = digital_clock[5]
        for i in range(6):
                if ((int(secundes2)) % 2) == 0: 
                        print(d1[i] + d2[i] + first_dots[i] + d3[i] + d4[i] + first_dots[i] + d5[i] + d6[i])
                else:
                        print(d1[i] + d2[i] + second_dots[i] + d3[i] + d4[i] + second_dots[i] + d5[i] + d6[i])
        sleep(0.5)
        os.system('cls')
