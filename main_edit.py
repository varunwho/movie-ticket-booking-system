import csv
import datetime
from datetime import date,time
import pyfiglet
from tabulate import _table_formats, tabulate
import os
import time
from sinchsms import SinchSMS
import random
from texttable import Texttable
import itertools
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import string
clear = lambda: os.system('cls')
# Class that contains user modules

class user(object):

    def __init__(self):
        self.location = ''
        self.gold_price = 250
        self.silver_price = 150
        self.food_price = 0
        self.food_item = []
        self.selected_seats = []
        self.total = 0
        self.locations = []
        self.theatre = ''
        self.time = None
        self.date = None
        self.movie = ''
        self.email = ''
        self.bookingId = ''
        self.num_seats = 0

# Module to select location
    def select_location(self):
        result1= pyfiglet.figlet_format("Location: ".center(40))
        print(result1)
        welcome = 'Book My Cinema'
        print(welcome.center(40, '*'))

        # Reads the city.csv to get cities

        with open('city.csv', 'r') as read_file:
            csv_reader = csv.reader(read_file, delimiter = ',')
            for line in csv_reader:
                for i in line:
                    self.locations.append(i)
        for location in self.locations:
            print(location.upper())
        print()

        # Enter city and check if the city is present in the file

        while True:
            print('Enter your City: ')
            self.location = input().lower()
            if self.location not in self.locations:
                print('Enter valid location!!: ')
                continue
            else:
                break

# Module to select movies
    def select_movies_time(self):
        def select_movies():
            clear()
            result1= pyfiglet.figlet_format("Select Movie: ".center(40))
            print(result1)
            movies = {}
            # Storing the contents of the movies file in movies dictionary
            with open('movies.csv', 'r') as read_file:
                csv_reader = list(csv.reader(read_file))
                for line in csv_reader:
                    if line == []:
                        continue
                    movies[line[0]] = {}
                    movies[line[0]]['name'] = line[0]
                    movies[line[0]]['Rating'] = line[1]
                    movies[line[0]]['genre'] = line[2]
                    movies[line[0]]['language'] = line[3]
                    movies[line[0]]['release'] = line[4]
                    movies[line[0]]['length'] = line[5]
                    movies[line[0]]['advisory'] = line[6]
            final = [['Movies']]
            add = []

            print('Movies Now Showing'.title())
            print()
            for dictmovie in movies.keys():
                add.append(dictmovie.title())
                final.append(add)
                add = []

            Cinema = Texttable()
            Cinema.add_rows(final)
            print(Cinema.draw())

            # Enter the movie and check if the movie is present in the movies dictionary

            movie = input('Enter your movie: ').lower()
            while movie not in movies.keys():
                movie = input('Enter valid movie name!!!: ')
            movie = movie.upper()

            print(pyfiglet.figlet_format(movie.center(40)))
            self.movie = movie.lower()

            final = []
            add = []

            # Displaying the movies information table
            for dictmovie in movies.values():
                if dictmovie['name'] == movie.lower():
                    for attribute, info in dictmovie.items():
                        if attribute != 'location' and attribute != 'name':
                            add.append(attribute)
                            add.append(info)
                            final.append(add)
                            add = []
            Cinema = Texttable()
            Cinema.add_rows(final)
            print(Cinema.draw())

            # Asks the user if they want to book tickets for the movie
            # if user enters n/no the loop continues
            choice = input(('Book tickets? (y/n): ')).lower()
            while choice not in ['y','n','yes','no']:
                choice = input(('Enter a valid choice: ')).lower()
            return choice

        choice = select_movies()

        while choice in ['n', 'no']:
            choice = select_movies()

    # To select date:
    def select_date(self):
        with open('Date.csv', 'r') as read_file:
            csv_reader = csv.reader(read_file, delimiter = ',')
            for line in csv_reader:
                if line[0] == self.theatre and line[1] == self.movie:
                    for i in range(len(line)):
                        if i not in [0,1]:
                            number = line[2]

        read_file.close()

        result1= pyfiglet.figlet_format("Select Date".center(40))
        print(result1)
        d = date.today()
        dates = []
        day = datetime.datetime.now()

        final = [['ID', 'Day','Date']]
        add = []
        number = int(number)
        for i in range(number):
            add.append(i+1)
            add.append(day.strftime("%A"))
            add.append(d)
            final.append(add)
            add = []
            dates.append(d)
            d += datetime.timedelta(days = 1)
            day += datetime.timedelta(days = 1)



        Day = Texttable()
        Day.add_rows(final)
        print(Day.draw())

        day_choice = input(f'Select your date (Enter 1-{number}): ')
        check = list(range(1, number + 1))
        check = [str(i) for i in check]

        while day_choice not in check:
            day_choice = input(f'Select your date from 1-{number}: ')

        day_choice = int(day_choice)

        self.date = dates[day_choice - 1]

        choice = input(('Continue? (y/n): ')).lower()
        while choice not in ['y','n','yes','no']:
            choice = input(('Enter valid choice!!!: ')).lower()
        return choice

    def select_time(self):
        result1= pyfiglet.figlet_format("Select Time".center(40))
        print(result1)
        d = date.today()
        from datetime import time
        from datetime import datetime

        # Times is a dictionary to store movie times

        times = {}
        count = 1
        now = datetime.now().time()

        # Reads the time.csv file to read time corresponding to the movie and the theater
        with open('time.csv', 'r') as read_file:
            csv_reader = csv.reader(read_file, delimiter = ',')
            for line in csv_reader:
                if line[0] == self.theatre and line[1] == self.movie:
                    for i in range(len(line)):
                        if i not in [0,1]:
                            ti = datetime.strptime(line[i],'%H:%M:%S').time()
                            times[str(count)] = ti
                            count += 1

        read_file.close()
        # If the movie is in the current day
        # Then enter the available time in the dictionary times_edit
        if self.date == d:
            times_edit = {}
            count = 1
            final = [['ID', 'Time']]
            add = []
            for index, time in times.items():
                if time > now:
                    times_edit[str(count)] = time
                    add.append(count)
                    add.append(time)
                    final.append(add)
                    add = []
                    count += 1
            times = times_edit

        # Else show all the time

        else:
            count = 1
            final = [['ID', 'Time']]
            add = []
            for index, time in times.items():
                add.append(count)
                add.append(time)
                final.append(add)
                count += 1
                add = []

        Time = Texttable()
        Time.add_rows(final)
        print(Time.draw())

        user_time = input(f'Enter your time (1-{len(times)}): ')
        check = list(range(1, len(times) + 1))
        check = [str(i) for i in check]
        # To check if the user entered the correct option
        while user_time not in check:
            user_time = input(f'Enter time from (1-{len(times)}): ')

        # To convert the time and date entered by the user into string
        self.time = str(times[user_time])
        self.date = str(self.date)

        print(f'Selected movie time - {user_time}')
        choice = input('continue? (y/n): ')
        while choice not in ['y','n','yes','no']:
            choice = input(('Enter valid choice: ')).lower()
        return choice

    def select_theatre(self):
        clear()
        result1= pyfiglet.figlet_format("Select Theater".center(40))
        print(result1)
        theatres = {}

        # Read the theaters.csv file to dispaly the available theaters
        with open('theaters.csv', 'r') as read_file:
            csv_reader = csv.reader(read_file, delimiter = ',')
            for line in csv_reader:
                theatres[line[0]] = []
                for i in line:
                    if i != line[0]:
                        theatres[line[0]].append(i)
        read_file.close()
        final = [['ID', 'Theater']]
        add = []

        #
        for i, theatre in enumerate(theatres[self.location]):
            add.append(i + 1)
            add.append(theatre)
            final.append(add)
            add = []

        Theaters = Texttable()
        Theaters.add_rows(final)
        print(Theaters.draw())

        check = list(range(1, len(theatres[self.location]) + 1))
        check = [str(i) for i in check]
        theatre = input('Select theatre ID: ')
        while theatre not in check:
            theatre = input('Enter valid theatre ID!!!: ')
        theatre = int(theatre)
        self.theatre = theatres[self.location][theatre - 1]
        print(self.theatre)
        choice = input(f'Preffered theatre: {theatre} Continue? (y/n): ')
        while choice not in ['y','n','yes','no']:
            choice = input(('Enter valid choice!!!: ')).lower()
        return choice

    def select_seats(self):
        clear()
        result1= pyfiglet.figlet_format("Select Seats".center(40))
        print(result1)

        seats = [['.' for i in range(10)] for j in range(10)]
        try:
            with open('book.csv', 'r') as read_file:
                fieldnames = ['movie','city','theatre','day','time','seats']
                csv_reader = csv.DictReader(read_file, fieldnames = fieldnames)

                for line in csv_reader:
                    if line['movie'] == self.movie and line['city'] == self.location and line['theatre'] == self.theatre and line['day'] == self.date and line['time'] == self.time:
                        row = int(line['seats']) // 10
                        cols = int(line['seats']) % 10
                        seats[row][cols] = '*'
        except FileNotFoundError:
            pass

        print(' ', end = '')
        for i in range(10):
            print(i, end = ' ')
        print("\033[1;33;40m")
        for i in range(10):
            if i == 2:
                print("\033[1;37;40m")
            print(str(i), end = '')
            for j in range(10):
                print(seats[i][j], end = ' ')
            print()
        print("\033[1;33;40mGOLD : Rs 250")
        print("\033[1;37;40mSILVER : RS 150")

        check = list(range(1, 7))
        check = [str(i) for i in check]
        tickets = input('''Enter number of tickets (Max 6): ''')
        while tickets not in check:
            tickets = input('''Enter number of tickets (Max 6): ''')

        tickets = int(tickets)
        self.num_seats = tickets

        for i in range(tickets):
            while True:
                print('Enter seat number (row,column): ')
                seat = input()
                seat = "".join(seat.split())
                while len(seat) != 3:
                    seat =  input('Enter valid seat: ')
                while ',' not in seat and len(seat) != 3:
                    seat = input('Enter (row,column): ')
                row_check = list(range(10))
                row_check = [str(i) for i in row_check]
                col_check = list(range(10))
                col_check = [str(i) for i in col_check]
                seat = seat.split(',')
                row, cols = seat[0], seat[1]



                if row not in row_check and cols not in col_check:
                    continue
                row, cols = int(row), int(cols)

                if seats[row][cols] == '*':
                    continue
                break

            seats[row][cols] = '*'
            self.selected_seats.append((row, cols))
            seatID = row * 10 + (cols)
            if seatID < 20:
                self.total += self.gold_price
            else:
                self.total += self.silver_price
            seater = {
              'movie' : self.movie,
              'city' : self.location,
              'theatre':self.theatre,
              'day':self.date,
              'time':self.time,
              'seats': seatID
            }
            with open('book.csv', 'a', newline = '') as new_file:
                fieldnames = ['movie','city','theatre','day','time','seats']
                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames ,delimiter = ',')
                csv_writer.writerow(seater)

            print(' ', end = '')
            for i in range(10):
                print(i, end = ' ')
            print()
            print("\033[1;33;40m")
            for i in range(10):
                if i == 2:
                    print("\033[1;37;40m")
                print(str(i), end = '')
                for j in range(10):
                    print(seats[i][j], end = ' ')
                print()


    def food_menu(self):
        clear()
        meal = input('Do you wanna a grab a bite (y/n)?: ')
        while meal not in ['y','n','yes','no']:
            meal = input(('Enter valid choice!!: ')).lower()
        if meal in ['n', 'no']:
            return

        if meal in ['y', 'yes']:
            from texttable import Texttable
            def read_food(data, sub):
                prices = []
                with open('food.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file)
                    for line in csv_reader:
                        if line[0] == sub:
                            for i in range(len(line)):
                                if i != 0:
                                    prices.append(line[i])
                            data.append(prices)
                            prices = []
                temp = data[0]
                del data[0]
                data.sort()
                k = list(data for data,_ in itertools.groupby(data))
                data = k
                data.insert(0, temp)
                return data
                return data

            result1 = pyfiglet.figlet_format('Food Menu'.center(40))
            print(result1)

            data = [['Item', 'Small', 'Medium', 'Large']]
            final = read_food(data, 'Iced-Tea')

            price = 0
            print("Iced-Tea:-")

            IcedTea = Texttable()
            IcedTea.add_rows(final)
            print(IcedTea.draw())

            data = [['Item', 'Small', 'Medium', 'Large']]
            final = read_food(data, 'Cold Coffee')

            i=1
            while (i<=4):
                i=i+1
                print()


            print('Cold Coffee:-')
            from texttable import Texttable
            ColdCoffee = Texttable()
            ColdCoffee.add_rows(final)
            print(ColdCoffee.draw())


            i=1
            while (i<=4):
                i=i+1
                print()


            data = [['Item', 'Price']]
            final = read_food(data, 'Aerated Drinks (200 ml)')



            print ("Aerated Drinks (200 ml):-")
            from texttable import Texttable
            AeratedDrinks = Texttable()
            AeratedDrinks.add_rows(final)
            print(AeratedDrinks.draw())



            i=1
            while (i<=4):
                i=i+1
                print()

            data = [['Item', 'Price']]
            final = read_food(data, 'Mineral Water')



            print ("Mineral Water:-")
            from texttable import Texttable
            MineralWater = Texttable()
            MineralWater.add_rows(final)
            print(MineralWater.draw())


            i=1
            while (i<=4):
                i=i+1
                print()

            data = [['Item', 'Price']]
            final = read_food(data, 'Hot Beverages (80 ml)')

            print ("Hot Beverages (80 ml):-")
            from texttable import Texttable
            HotBeverages = Texttable()
            HotBeverages.add_rows(final)
            print(HotBeverages.draw())


            i=1
            while (i<=4):
                i=i+1
                print()

            data = [['Item', 'Small', 'Medium', 'Large']]
            final = read_food(data, 'Popcorn')


            print ("Popcorn:-")
            from texttable import Texttable
            Popcorn = Texttable()
            Popcorn.add_rows(final)
            print(Popcorn.draw())



            i=1
            while (i<=4):
                i=i+1
                print()


            data = [['Item', 'Price']]
            final = read_food(data, 'Appetizers')


            print ("Appetizers:-")
            from texttable import Texttable
            Appetizers = Texttable()
            Appetizers.add_rows(final)
            print(Appetizers.draw())


            i=1
            while (i<=4):
                i=i+1
                print()

            data = [['Item', 'Small', 'Medium', 'Large']]
            final = read_food(data, 'Rolls')

            print ("Rolls:-")
            from texttable import Texttable
            Rolls = Texttable()
            Rolls.add_rows(final)
            print(Rolls.draw())



            i=1
            while (i<=4):
                i=i+1
                print()

            data = [['Item', 'Price']]
            final = read_food(data, 'Special Combos')

            print ("Special Combos:-")
            from texttable import Texttable
            SpecialCombos = Texttable()
            SpecialCombos.add_rows(final)
            print(SpecialCombos.draw())



            i=1
            while (i<=4):
                i=i+1
                print()

            data = [['Item', 'Single Scoop', 'Double Scoop', 'Cone']]
            final = read_food(data, 'Ice Creams')

            print ("Ice Creams:-")
            from texttable import Texttable
            IceCream = Texttable()
            IceCream.add_rows(final)
            print(IceCream.draw())
            choice = 'y'

            while choice in ['y', 'yes']:
                pre = False
                while pre == False:
                    sub = input('Enter submenu: ')

                    with open('food.csv', 'r') as read_file:

                        csv_reader = csv.reader(read_file)
                        for line in csv_reader:
                            if line == []:
                                break
                            if line[0] == sub:
                                pre = True
                                break
                    if pre == True:
                        break
                pre = False
                while pre == False:
                    item = input('\nEnter item from ' + sub + ': ')
                    with open('food.csv', 'r') as read_file:

                        csv_reader = csv.reader(read_file)
                        for line in csv_reader:
                            if line == []:
                                break
                            if line[0] == sub:
                                if line[1] == item:
                                    quantity = input('Enter quantity ')
                                    while quantity not in ['0','1', '2', '3', '4', '5', '6', '7']:
                                        quantity = input('Control yourself and enter quantity : ')

                                    quantity = int(quantity)
                                    pre = True
                                    if sub in ['Iced-Tea','Cold Coffee','Popcorn','Rolls']:

                                        Tab = Texttable()
                                        Tab.add_rows([['Press', 'Option'], ['1','To order Small'],['2', 'To order Medium'],['3', 'To order Large']])
                                        print(Tab.draw())
                                        choice = input()
                                        while choice not in ['1','2','3']:
                                            choice = input('Enter 1 or 2 or 3: ')

                                        if choice == '1':
                                            add = int(line[2]) * quantity
                                            price += add
                                            break

                                        elif choice == '2':
                                            add = int(line[3]) * quantity
                                            price += add
                                            break

                                        elif choice == '3':
                                            add = int(line[4]) * quantity
                                            price += add
                                            break

                                    elif sub in ['Ice Creams']:
                                        Tab = Texttable()
                                        Tab.add_rows([['Press', 'Option'], ['1','To order Single Scoop'],['2', 'To order Double Scoop'],['3', 'To order Cone']])
                                        print(Tab.draw())
                                        choice = input()
                                        while choice not in ['1','2','3']:
                                            choice = input('Enter 1 or 2 or 3: ')

                                        if choice == '1':
                                            add = int(line[2]) * quantity
                                            price += add
                                            break

                                        elif choice == '2':
                                            add = int(line[3]) * quantity
                                            price += add
                                            break

                                        elif choice == '3':
                                            add = int(line[4]) * quantity
                                            price += add
                                            break
                                    else:
                                        add = int(line[2]) * quantity
                                        price += add
                                        break
                                    pre = True
                        if pre == True:
                            break
                self.food_item.append(item)
                self.food_price += price
                self.total += self.food_price
                choice = input('Order more? (y/n): ')
                while choice not in ['y','n','yes','no']:
                    choice = input(('Enter valid choice: ')).lower()
                if choice in ['n', 'no']:
                    print(self.food_item)
                    break
                pre = False


    def payment(self):

        def otp():
            self.email = input('Enter your email Address: ')
            number = input('Enter your mobile number: ')
            while len(number) != 10 and number not in ['7702167946']:
                number = input('Input valid mobile number: ')
            number = '+91' + number
            otp = random.randrange(1000,9999,2)
            otp = str(otp)
            message = f'Book My Cinema never calls you asking for OTP. OTP is confidential. For security reasons, do not share this OTP with anyone. Your OTP is {otp} '
            client = SinchSMS('660367af-18ff-42ca-89d2-8856dcba78dd','fijjTkW5jkuaCARwJlGnKA==')

            print("Sending '%s' to %s" % ('OTP', number))
            response = client.send_message(number, message)
            message_id = response['messageId']

            response = client.check_status(message_id)
            while response['status'] != 'Successful':
                time.sleep(1)
                response = client.check_status(message_id)

            u_otp = input('Enter the 4 digit otp: ')

            while u_otp != otp:
                u_otp = input('Enter valid 4 digit otp!!: ')

            print('OTP matched!!')

        print("\033[1;31;40m")
        result1= pyfiglet.figlet_format("Booking summary".center(0))
        print(result1)
        print("\033[1;37;40m")
        format_list = list(_table_formats.keys())
        table = [["Movie", self.movie],["Theatre", self.theatre], ["Date",self.date],["Time",self.time],["seats",self.selected_seats], ["Total", self.total]]
        print(tabulate(table, tablefmt='grid'))
        print('\033[1;31;40mAmount Payable - ' + str(self.total) + '\033[1;37;40m')

        result1= pyfiglet.figlet_format("Payment Options".center(0))
        print(result1)

        format_list = list(_table_formats.keys())
        table = [["1", "Credit/Debit card"],["2", "Mobile wallet"],["3","UPI"]]
        headers = ['Press', 'Payment method']
        print(tabulate(table, headers,tablefmt='pipe'))

        choice = input()
        while choice not in ['1', '2', '3']:
            choice = input('Enter valid payment method: ')
        clear()

        # Credit card block:
        if choice == '1':
            today = date.today()
            result1= pyfiglet.figlet_format("Credit Card".center(0))
            print(result1)
            card_num = input('Enter card number: ')
            while len(card_num) != 16:
                card_num = input('Enter valid card number!!: ')
            card_name = input('Name on the card: ')
            print('Enter expiry date: ')
            check = list(range(1, 13))
            check = [str(i) for i in check]
            month = input('Enter month: ')

            while month not in check:
                month = input('Enter valid month: ')
            month  = int(month)

            check = ['2019', '2020', '2021', '2022', '2023', '2024']
            year = input('Enter year: ')
            while year not in check:
                year = input('Enter valid year: ')

            year = int(year)

            while month <= today.month and year == today.year:
                print('Enter valid expiry date: ')
                check = list(range(1, 13))
                check = [str(i) for i in check]
                month = input('Enter month: ')

                while month not in check:
                    month = input('Enter valid month: ')
                month  = int(month)

                check = ['2019', '2020', '2021', '2022', '2023', '2024']
                year = input('Enter year: ')
                while year not in check:
                    year = input('Enter valid year: ')

                year = int(year)

            cvv = input('Enter cvv: ')
            while len(cvv) != 3:
                cvv = input('Enter cvv: ')
            clear()
            otp()
            clear()
            print("Your transaction is underway, Don't refresh: ")
            time.sleep(5)
            print('Transaction Sucessfull!!')

        # Mobile wallet block
        elif choice == '2':
            result1= pyfiglet.figlet_format("Mobile Wallet".center(0))
            print(result1)
            format_list = list(_table_formats.keys())
            table = [["1", "PayTm"],["2", "PayPal"], ["3","FreeCharge"]]
            headers = ['Press', 'Mobile wallet']
            print(tabulate(table, headers,tablefmt='pipe'))
            choice = input()
            while choice not in ['1', '2', '3']:
                choice = input('Enter valid mobile wallet: ')

            print('Redirecting...')

            time.sleep(5)
            clear()

            if choice == '1':
                result1 = pyfiglet.figlet_format("PayTm".center(40))
                print(result1)
            elif choice == '2':
                result1 = pyfiglet.figlet_format("PayPal".center(40))
                print(result1)
            elif choice == '3':
                result1 = pyfiglet.figlet_format("FreeCharge".center(40))
                print(result1)

            print(f'Book my Cinema order                          Rs {self.total}')

            choice = input('Proceed? (y/n) ').lower()
            while choice not in ['y','n','yes','no']:
                choice = input('Enter valid choice: ').lower()
            if choice in ['n', 'no']:
                return choice
            otp()
            print('Your transaction is underway, Don\'t refresh')
            time.sleep(5)
            print('Your Transaction is Sucessfull!! ')

        # UPI Block
        elif choice == '3':
            result1= pyfiglet.figlet_format("UPI".center(40))
            print(result1)

            options = ['PayTm', 'Amazon Pay','PhonePe','BHIM']
            print('Enter upi payment option ')
            upi = Texttable()
            upi.add_rows([['ID', 'Options'],['1','PayTm'],['2','Amazon Pay'],['3','PhonePe'],['4','BHIM']])
            print(upi.draw())
            upi = input()
            while upi not in ['1','2','3','4']:
                upi = input('Enter valid choice: ')
            mode = options[int(upi) - 1]
            result1 = pyfiglet.figlet_format(mode.center(40))
            print(result1)
            UPI = input('Enter UPI pin: ')
            while len(UPI) != 6:
                UPI = input('Enter valid UPI pin: ')


            print('Enter Bank ID: ')
            Bank = Texttable()
            Bank.add_rows([['ID', 'Bank'],['1','HDFC Bank'],['2','Axis Bank'],['3','SBI Bank'],['4','Yes Bank'],['5','IDFC Bank']])
            print(Bank.draw())
            bank = input()
            while bank not in ['1','2','3','4','5']:
                bank = input('Enter valid choice: ')
            otp()
            print('Your transaction is underway, Don\'t refresh')
            time.sleep(5)
            print('Your Transaction is Sucessfull!! ')


    def Ticket(self):

        print('Your movie ticket will be sent to your mail. Please wait...')
        num = str(random.randint(1000,9999))
        # Generating booking ID
        letters = string.ascii_lowercase
        alpha = ''.join(random.choice(letters) for i in range(4)).upper()
        self.bookingId = num + alpha
        try:
            smtp_server = "smtp.gmail.com"
            port = 465  # For starttls
            sender_email = "bookmycinema2@gmail.com"
            password = "Bookmycinema@123"
            receiver_email = self.email
            message = MIMEMultipart("alternative")
            message["Subject"] = "Booking Confirmation from Book My Cinema"
            message["From"] = sender_email
            message["To"] = receiver_email

        # Create the plain-text and HTML version of your message (The format of our ticket)
            text = """\
            Hi,
            Thanks, your ticket booking confirmed."""

            html = """\
            <!DOCTYPE html>
            <html>
            <body>
                <font style='font-size: 14px;font-weight: bold;color: #0E0014;'>
                <table bgcolor="#38E798" border=0 style='font-family:"Comic Sans MS", Courier, monospace; font-size:100%'>
                <tr><td colspan="2" align="center" bgcolor="white" height="40"><font style='font-family:"Brush Script MT";font-size: 38px;color:#F62E0E;font-weight: bold;'>Book My Cinema</font></td></tr>
                <tr> <td colspan="2" align="center" bgcolor="#000000" height="40"><font style='font-family:"Comic Sans MS";font-size: 18px;font-weight: bold;color:#FFFFFF;'>Your Booking is confirmed</h3></td></tr>
                <tr><td align="right">Booking ID:</td><td>{bookingId:}</td></tr>
                <tr><td align="right">Movie:</td><td>{movie:}</td></tr>
                <tr><td align="right">Date:</td><td>{date:}</td></tr>
                <tr><td align="right">Theatre:</td><td>{theater:}</td></tr>
                <tr><td align="right">No of seat:</td><td>{num:}</td></tr>
                <tr><td align="right">Screen:</td><td>{screen:}</td></tr>
                <tr><td align="right">Seat No:</td><td>{seats:}</td></tr>
                <tr><td align="right">Total Amount(INR)</td><td>{total:}</td></tr>
                </table>
                </font>

    </body>
    </html>"""

            html=html.format(bookingId = self.bookingId ,movie = self.movie.title(), num = self.num_seats, seats = self.selected_seats,date = self.date,time = self.time,theater = self.theatre, screen = random.randint(1,7), total = self.total)

        # Turn these into plain/html MIMEText objects

            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)
             # Create a secure SSL context
            context = ssl.create_default_context()
            # Try to log in to server and send email
            try:
        # TODO: Send email here
                with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
            except Exception as e:
        # Print any error messages to stdout
                print(e)
            finally:
                server.quit()
        except smtplib.SMTPServerDisconnected:
            pass
