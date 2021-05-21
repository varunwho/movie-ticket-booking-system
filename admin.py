from main_edit import user
import csv
import os
from texttable import Texttable
clear = lambda: os.system('cls')
import itertools
from datetime import time
from datetime import datetime
import pyfiglet
import sys
import time as t
accessKey = 'admin@123'
class Admin(user):
    def modify_location(self):
        clear()
        result1= pyfiglet.figlet_format("Edit City".center(40))
        print(result1)

        Tab = Texttable()
        Tab.add_rows([['Press', 'Option'], ['1','To Remove city'],['2', 'Add City']])
        print(Tab.draw())
        choice = input()
        while choice not in ['1','2']:
            choice = input('Enter 1 or 2: ')

        final = [['City']]
        add = []
        if choice == '1':
            clear()
            while True:
                result1= pyfiglet.figlet_format("Delete City".center(40))
                print(result1)
                with open('city.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file, delimiter = ',')
                    for line in csv_reader:
                        for i in line:
                            self.locations.append(i)
                            add.append(i)
                            final.append(add)
                            add = []

                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())

                city = input('Enter the name of location to be deleted: ')

                with open('city.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    while city not in lines[0]:
                        city = input('Enter the name of location to be deleted: ')
                    lines[0].remove(city)
                f.close()
                with open('city.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()
                final = [['City']]
                add = []

                with open('theaters.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    for i in lines:
                        if i[0] == city:
                            lines.remove(i)
                f.close()

                with open('theaters.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()
                self.locations = []
                final = [['City']]
                add = []

                print('City deleted Sucessfully! ')
                choice = input('Want to delete more cities (y/n)?: ')
                while choice not in ['y','n','yes','no']:
                    choice = input(('Enter valid choice: ')).lower()
                if choice in ['n', 'no']:
                    break

        elif choice == '2':
            clear()
            while True:
                result1= pyfiglet.figlet_format("Add City".center(40))
                print(result1)
                final = [['City']]
                add = []
                print('Cities in the file: ')
                with open('city.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file, delimiter = ',')
                    for line in csv_reader:
                        for i in line:
                            self.locations.append(i)
                            add.append(i)
                            final.append(add)
                            add = []


                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())


                city = input('Enter the name of the city to be added: ')
                while city in self.locations:
                    city = input('Enter the name of the city to be added: ')


                choice = input('Continue (y/n)?: ')
                while choice not in ['y','n','yes','no']:
                    choice = input(('Enter valid choice: ')).lower()
                while choice in ['no', 'n']:
                    city = input('Enter the name of the city to be added: ')
                    choice = input('Continue (y/n)?: ')
                    while choice not in ['y','n','yes','no']:
                        choice = input(('Enter valid choice: ')).lower()

                with open('city.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    while city in lines[0]:
                        city = input('Enter the name of location to be added: ')
                    lines[0].append(city)
                f.close()
                with open('city.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                with open('theaters.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    city = [city]
                    lines.append(city)
                f.close()
                with open('theaters.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()
                self.locations = []
                print('City added Sucessfully! ')
                choice = input('Want to add more cities (y/n)?: ')
                while choice not in ['y','n','yes','no']:
                    choice = input(('Enter valid choice: ')).lower()
                if choice in ['n', 'no']:
                    break



    def modify_Movies(self):
        clear()
        result1= pyfiglet.figlet_format("Edit Movies".center(40))
        print(result1)

        movies = []
        Tab = Texttable()
        Tab.add_rows([['Press', 'Option'], ['1','To Add Movies'],['2', 'To delete Movies']])
        print(Tab.draw())
        choice = input()
        while choice not in ['1','2']:
            choice = input('Enter 1 or 2: ')



        if choice == '1':
            clear()
            result1= pyfiglet.figlet_format("Add Movies".center(40))
            print(result1)
            while True:
                count = 0
                print('Existing movies : ')
                final = [['Movie']]
                add = []
                with open('movies.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file)
                    for line in csv_reader:
                        if line == []:
                            continue
                        count += 1
                        movies.append(line[0])
                        add.append(line[0])
                        final.append(add)
                        add = []


                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())

                num = count
                info = []
                movie = input('Enter the name of the movie to be added: ').lower()
                while movie in movies:
                    movie = input('Enter the name of the movie to be added: ')
                info.append(movie)
                clear()
                rating = input('Enter the rating of the movie (1-100): ')
                check = list(range(101))
                check = [str(i) for i in check]
                while rating not in check:
                    rating = input('Enter valid rating: ')
                info.append(rating)
                clear()
                genre = input('Enter genre: ')
                info.append(genre)
                clear()
                language = input('Enter language: ')
                info.append(language)
                clear()
                release = input('Enter release date (YYYY/MM/D): ')
                info.append(release)
                clear()
                print('Running time: ')
                hrs = input('Enter hours: ')
                check = list(range(1, 25))
                check = [str(i) for i in check]
                while hrs not in check:
                    hrs = input('Enter valid hours: ')

                min = input('Enter mins: ')
                check = list(range(1, 61))
                check = [str(i) for i in check]
                while min not in check:
                    min = input('Enter valid mins: ')
                run = hrs + 'h ' + min + 'min'
                info.append(run)
                clear()
                advisary = input('Enter advisory (U/UA/A): ')
                while advisary not in ['U', 'UA', 'A']:
                    advisary = input('Enter valid advisory: ')
                info.append(advisary)
                clear()

                time = ['08:00:00','11:00:00','09:00:00','14:00:00','16:00:00','20:00:00','22:50:00']
                with open('movies.csv', 'a', newline = '') as new_file:
                    csv_writer = csv.writer(new_file, delimiter = ',')
                    csv_writer.writerow(info)

                read_file.close()


                count = num

                with open('time.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    for i in range(len(lines)):

                        theater = lines[i][0]
                        count += 1
                        if count == num + 1:
                            lines.insert(i,[theater])
                            count = 1

                    for line in lines:
                        if len(line) == 1:
                            line.append(movie)
                            for i in time:
                                line.append(i)

                f.close()
                with open('time.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                count = num
                days = []
                with open('Date.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)

                    for line in lines:
                        for i in range(len(line)):
                            if i not in [0,1]:
                                days.append(line[i])


                f.close()

                count = num

                with open('Date.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    for i in range(len(lines)):

                        theater = lines[i][0]
                        count += 1
                        if count == num + 1:
                            lines.insert(i,[theater])
                            count = 1

                    for line in lines:
                        if len(line) == 1:
                            line.append(movie)
                            for i in days:
                                line.append(i)
                                break

                f.close()
                with open('Date.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                print('Movie Succesfully added ')

                choice = input('Want to edit more movies (y/n)?: ')
                while choice not in ['y','n','yes','no']:
                    choice = input(('Enter valid choice: ')).lower()
                if choice in ['n', 'no']:
                    break

        elif choice == '2':

            clear()
            result1= pyfiglet.figlet_format("Delete Movies".center(40))
            print(result1)
            while True:
                movies = []
                final = [['Movie']]
                add = []
                print('Existing movies : ')
                with open('movies.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file)
                    csv_reader = list(csv_reader)
                    for line in csv_reader:
                        if line == []:
                            continue
                        movies.append(line[0])
                        add.append(line[0])
                        final.append(add)
                        add = []

                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())
                read_file.close()

                movie = input('\n Enter the name of the movie to be deleted: ').lower()
                while movie not in movies:
                    movie = input('\nEnter the valid movie name: ').lower()

                with open('movies.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    for line in lines:
                        if line == []:
                            continue
                        if line[0] == movie:
                            lines.remove(line)

                with open('movies.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                with open('time.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    for line in lines:
                        if line[1] == movie:
                            lines.remove(line)

                f.close()
                with open('time.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                with open('Date.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    for line in lines:
                        if line[1] == movie:
                            lines.remove(line)

                f.close()
                with open('Date.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()
                print('Movie Deleted successfully ')
                choice = input('Want to delete more movies (y/n)?: ')
                while choice not in ['y','n','yes','no']:
                    choice = input('Enter valid choice: ').lower()
                if choice in ['n', 'no']:
                    break

    def modify_theatres(self):
        clear()
        result1= pyfiglet.figlet_format("Modify Theater".center(40))
        print(result1)
        Tab = Texttable()
        Tab.add_rows([['Press', 'Option'], ['1','To Add Theaters'],['2', 'To delete Theaters']])
        print(Tab.draw())
        choice = input()
        while choice not in ['1','2']:
            choice = input('Enter 1 or 2: ')


        if choice == '1':
            clear()
            result1= pyfiglet.figlet_format("Add Theaters".center(40))
            print(result1)
            while True:
                final = [['City']]
                add = []
                time = ['08:00:00','11:00:00','09:00:00','14:00:00','16:00:00','20:00:00','22:50:00']
                movies = []
                with open('movies.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file)
                    csv_reader = list(csv_reader)
                    for line in csv_reader:
                        if line == []:
                            continue
                        movies.append(line[0])
                read_file.close()

                with open('city.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file, delimiter = ',')
                    for line in csv_reader:
                        for i in line:
                            self.locations.append(i)
                            add.append(i)
                            final.append(add)
                            add = []

                read_file.close()
                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())
                read_file.close()

                city = input('Enter city: ')
                while city not in self.locations:
                    city = input('Enter supported city: ')

                final = [['Theater']]
                add = []
                print('Existing Theaters : ')
                with open('theaters.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file)
                    for line in csv_reader:
                        if line == []:
                            break

                        for i in range(len(line)):
                            if line[0] == city:
                                if i != 0:
                                    add.append(line[i])
                                    final.append(add)
                                    add = []

                read_file.close()
                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())
                read_file.close()

                theater = input('Enter name of theatre to be added: ')

                with open('theaters.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)

                    for line in lines:
                        while theater in line:
                            print('Theater already exists ')
                            theater = input('Enter name of theatre to be added: ')

                for i in lines:
                    for j in i:
                        if j == city:
                            i.append(theater)
                            break

                writer = csv.writer(open('theaters.csv', 'w', newline = ''))
                writer.writerows(lines)

                with open('time.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)

                    line = []

                    for movie in movies:
                        line.append(theater)
                        line.append(movie)
                        for j in time:
                            line.append(j)
                        lines.append(line)
                        line = []


                f.close()
                with open('time.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                with open('Date.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)

                    line = []

                    for movie in movies:
                        line.append(theater)
                        line.append(movie)
                        line.append('7')
                        lines.append(line)
                        line = []


                f.close()
                with open('Date.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()
                final = [['City']]
                add = []
                print('Theater added Sucessfully ')
                choice = input('Want to add more Theaters (y/n)?: ')
                while choice not in ['y','n','yes','no']:
                    choice = input(('Enter valid choice: ')).lower()
                if choice in ['n', 'no']:
                    break


        elif choice == '2':

            clear()
            result1= pyfiglet.figlet_format("Delete Theaters".center(40))
            print(result1)
            while True:
                final = [['City']]
                add = []
                with open('city.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file, delimiter = ',')
                    for line in csv_reader:
                        for i in line:
                            self.locations.append(i)
                            add.append(i)
                            final.append(add)
                            add = []

                read_file.close()
                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())
                read_file.close()

                city = input('Enter city ')
                while city not in self.locations:
                    city = input('Enter supported city ')

                final = [['Theater']]
                add = []
                print('Existing Theaters : ')
                with open('theaters.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file)
                    for line in csv_reader:
                        if line == []:
                            break

                        for i in range(len(line)):
                            if line[0] == city:
                                if i != 0:
                                    add.append(line[i])
                                    final.append(add)
                                    add = []

                read_file.close()
                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())
                read_file.close()



                r = csv.reader(open('theaters.csv'))
                lines = list(r)
                check = False
                while check == False:
                    theater = input('Enter name of theatre to be removed: ')
                    for i in lines:
                        if theater in i and i[0] == city:
                            check = True
                    if check == True:
                        break
                    else:
                        print('Invalid theater ')

                for i in lines:
                    for j in i:
                        if j == city:
                            i.remove(theater)
                            break

                writer = csv.writer(open('theaters.csv', 'w', newline = ''))
                writer.writerows(lines)

                with open('time.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)

                for i in range(3):
                    for line in lines:
                        if line == []:
                            break
                        if line[0] == theater:
                            lines.remove(line)

                f.close()
                with open('time.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                with open('Date.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)

                for i in range(3):
                    for line in lines:
                        if line == []:
                            break
                        if line[0] == theater:
                            lines.remove(line)

                f.close()
                with open('Date.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                print('Theater deleted Sucessfully ')
                choice = input('Want to delete more Theaters (y/n)?: ')
                while choice not in ['y','n','yes','no']:
                    choice = input(('Enter valid choice: ')).lower()
                if choice in ['n', 'no']:
                    break



    def Modify_food(self):
        clear()
        result1= pyfiglet.figlet_format("Edit Food".center(40))
        print(result1)
        from texttable import Texttable
        choice = 'y'
        while choice in ['y','yes']:
            mod  = []
            final = [['Press', 'Action'],[1, 'Add Food item'],[2,'Remove Food item']]


            loged = Texttable()
            loged.add_rows(final)
            print(loged.draw())
            choice = input('Enter your choice : ')
            while choice not in ['1', '2']:
                choice = input('Enter valid choice : ')
            def read_food(data, sub):
                prices = []
                with open('food.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file)
                    for line in csv_reader:
                        if line == []:
                            break
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

            def showFood():
                from texttable import Texttable
                print('Existing Food Menu ')
                data = [['Item', 'Small', 'Medium', 'Large']]
                final = read_food(data, 'Iced-Tea')


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

            if choice == '1':
                clear()
                result1= pyfiglet.figlet_format("Add Food".center(40))
                print(result1)
                showFood()
                choice = 'y'
                if choice in ['y', 'yes']:
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
                    mod.append(sub)
                    while pre == False:
                        item = input('\nEnter item to be added to ' + sub + ': ')
                        with open('food.csv', 'r') as read_file:

                            csv_reader = csv.reader(read_file)
                            lines = list(csv_reader)
                            for line in lines:
                                while item in line:
                                    print('Item already exists ')
                                    item = input('\nEnter item to be added to ' + sub + ': ')

                        mod.append(item)
                        with open('food.csv', 'r') as read_file:

                            csv_reader = csv.reader(read_file)
                            for line in csv_reader:
                                if line == []:
                                    break
                                if line[0] == sub:
                                    pre = True
                                    if sub in ['Iced-Tea','Cold Coffee','Popcorn','Rolls']:
                                        small = input(f'Enter the price of small sized {sub}: ')
                                        medium = input(f'Enter the price of medium sized {sub}: ')
                                        large = input(f'Enter the price of large sized {sub}: ')
                                        mod.append(small)
                                        mod.append(medium)
                                        mod.append(large)
                                        break

                                    elif sub in ['Ice Creams']:
                                        single = input(f'Enter the price of single scooped {sub}: ')
                                        double = input(f'Enter the price of double scooped {sub}: ')
                                        cone = input(f'Enter the price of cone {sub}: ')
                                        mod.append(single)
                                        mod.append(double)
                                        mod.append(cone)
                                        break

                                    else:
                                        price = input('Enter Price: ')
                                        mod.append(price)
                                        break
                            if pre == True:
                                break
                    with open('food.csv', 'r') as f:
                        r = csv.reader(f)
                        lines = list(r)
                        lines.append(mod)
                    f.close()
                    with open('food.csv','w', newline = '') as f:
                        writer = csv.writer(f)
                        writer.writerows(lines)
                    f.close()

                    print('Food item added successfully: ')
                    choice = input('Want to add more food (y/n)? ')
                    while choice not in ['y','n','yes','no']:
                        choice = input(('Enter valid choice: ')).lower()
                    if choice in ['n', 'no']:
                        break

            elif choice == '2':

                clear()
                result1= pyfiglet.figlet_format("Delete Food".center(40))
                print(result1)
                showFood()
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
                        item = input('\nEnter item from ' + sub + ' to be deleted: ')
                        with open('food.csv', 'r') as read_file:

                            csv_reader = csv.reader(read_file)
                            for line in csv_reader:
                                if line == []:
                                    break
                                if line[0] == sub:
                                    if line[1] == item:

                                        pre = True

                            if pre == True:
                                break
                    with open('food.csv', 'r') as f:
                        r = csv.reader(f)
                        lines = list(r)

                        for i in lines:

                            if i[1] == item:
                                lines.remove(i)
                                pre = True
                                break

                    f.close()
                    with open('food.csv','w', newline = '') as f:
                        writer = csv.writer(f)
                        writer.writerows(lines)
                    f.close()

                    print('Food item deleted successfully: ')
                    choice = input('Want to delete more food (y/n)?: ')
                    while choice not in ['y','n','yes','no']:
                        choice = input(('Enter valid choice: ')).lower()
                    if choice in ['n', 'no']:
                        break

    def Modify_date(self):
        while True:
            clear()
            result1= pyfiglet.figlet_format("Edit Date".center(40))
            print(result1)
            final = [['City']]
            add = []
            with open('city.csv', 'r') as read_file:
                csv_reader = csv.reader(read_file, delimiter = ',')
                for line in csv_reader:
                    for i in line:
                        self.locations.append(i)
                        add.append(i)
                        final.append(add)
                        add = []

            read_file.close()
            Tab = Texttable()
            Tab.add_rows(final)
            print(Tab.draw())
            read_file.close()

            city = input('Enter city: ')
            while city not in self.locations:
                city = input('Enter supported city: ')


            final = [['Theater']]
            add = []
            print('Existing Theaters : ')
            theaters = []
            with open('theaters.csv', 'r') as read_file:
                csv_reader = csv.reader(read_file)
                for line in csv_reader:
                    if line == []:
                        break

                    for i in range(len(line)):
                        if line[0] == city:
                            if i != 0:
                                add.append(line[i])
                                theaters.append(line[i])
                                final.append(add)
                                add = []

            read_file.close()
            Tab = Texttable()
            Tab.add_rows(final)
            print(Tab.draw())
            read_file.close()
            final = [['Movie']]
            add = []
            movies = []

            theater = input('Enter name of theater: ')
            while theater not in theaters:
                theater = input('Enter valid theater: ')
            print('Existing movies : ')
            with open('movies.csv', 'r') as read_file:
                csv_reader = csv.reader(read_file)
                for line in csv_reader:
                    if line == []:
                        continue
                    add.append(line[0])
                    final.append(add)
                    movies.append(line[0])
                    add = []

            read_file.close()
            Tab = Texttable()
            Tab.add_rows(final)
            print(Tab.draw())
            read_file.close()

            movie = input('Enter Movie: ')
            while movie not in movies:
                movie = input('Enter valid Movie: ')

            times = {}
            count = 1
            now = datetime.now().time()
            with open('Date.csv', 'r') as read_file:
                csv_reader = csv.reader(read_file, delimiter = ',')
                for line in csv_reader:
                    if line[0] == theater and line[1] == movie:
                        match = True
                        for i in range(len(line)):
                            if i not in [0,1]:
                                number = int(line[2])

            read_file.close()
            print(f'Number of Running days for {movie} in {theater} : {number} ')
            change = input('Enter new number of running days: ')

            while change not in ['1', '2', '3', '4', '5', '6', '7']:
                print('\nDays cannot be zeroes or more than seven\n')
                change = input('Enter new number of running days : ')

            with open('Date.csv', 'r') as f:
                r = csv.reader(f)
                lines = list(r)
                for line in lines:
                    if line[0] == theater and line[1] == movie:
                        for i in range(len(line)):
                            if i not in [0,1]:
                                line[i] = change

            f.close()
            with open('Date.csv','w', newline = '') as f:
                writer = csv.writer(f)
                writer.writerows(lines)
            f.close()

            print('Day added successfully ')
            choice = input('Want to add more Days (y/n)?: ')
            while choice not in ['y','n','yes','no']:
                choice = input(('Enter valid choice: ')).lower()
            if choice in ['n', 'no']:
                break

    def Modify_time(self):
        clear()
        result1= pyfiglet.figlet_format("Edit Time".center(40))
        print(result1)
        from datetime import time
        from datetime import datetime
        choice = 'y'
        while choice in ['y','yes']:
            mod  = []
            final = [['Press', 'Action'],[1, 'Add Time'],[2,'Remove Time']]

            loged = Texttable()
            loged.add_rows(final)
            print(loged.draw())
            choice = input('Enter your choice : ')
            while choice not in ['1', '2']:
                choice = input('Enter valid choice : ')

            if choice == '1':
                clear()
                result1= pyfiglet.figlet_format("Add Time".center(40))
                print(result1)
                final = [['City']]
                add = []
                with open('city.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file, delimiter = ',')
                    for line in csv_reader:
                        for i in line:
                            self.locations.append(i)
                            add.append(i)
                            final.append(add)
                            add = []

                read_file.close()
                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())
                read_file.close()

                city = input('Enter city: ')
                while city not in self.locations:
                    city = input('Enter supported city: ')


                match = False
                while match == False:

                    final = [['Theater']]
                    add = []
                    print('Existing Theaters : ')
                    with open('theaters.csv', 'r') as read_file:
                        csv_reader = csv.reader(read_file)
                        csv_reader = list(csv_reader)
                        for line in csv_reader:
                            if line == []:
                                break

                            for i in range(len(line)):
                                if line[0] == city:
                                    if i != 0:
                                        add.append(line[i])
                                        final.append(add)
                                        add = []

                    read_file.close()
                    Tab = Texttable()
                    Tab.add_rows(final)
                    print(Tab.draw())
                    read_file.close()
                    final = [['Movie']]
                    add = []
                    theater = input('Enter name of theatre: ')
                    print('Existing movies : ')
                    with open('movies.csv', 'r') as read_file:
                        csv_reader = csv.reader(read_file)
                        csv_reader = list(csv_reader)
                        for line in csv_reader:
                            if line == []:
                                continue
                            add.append(line[0])
                            final.append(add)
                            add = []

                    read_file.close()
                    Tab = Texttable()
                    Tab.add_rows(final)
                    print(Tab.draw())
                    read_file.close()

                    movie = input('Enter Movie: ')
                    times = {}
                    count = 1
                    now = datetime.now().time()
                    with open('time.csv', 'r') as read_file:
                        csv_reader = csv.reader(read_file, delimiter = ',')
                        for line in csv_reader:
                            if line[0] == theater and line[1] == movie:
                                match = True
                                for i in range(len(line)):
                                    if i not in [0,1]:
                                        ti = datetime.strptime(line[i],'%H:%M:%S').time()
                                        times[str(count)] = ti
                                        count += 1

                    read_file.close()

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

                print('Enter Time to be added ')
                Hours = input('Enter Hours: ')
                check = list(range(0,24))
                check = [str(i) for i in check]
                while Hours not in check:
                    Hours = input('Enter valid Hours (0-23): ')
                check = list(range(0,60))
                check = [str(i) for i in check]
                min = input('Enter minutes: ')
                while min not in check:
                    min = input('Enter valid min (0 - 60): ')
                time = Hours + ':' + min + ':' + '00'
                time = datetime.strptime(time,'%H:%M:%S').time()
                out = False
                with open('time.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    for line in lines:

                        if out:
                            break
                        if line[0] == theater and line[1] == movie:
                            for i in range(len(line)):
                                if i not in [0,1]:
                                    ti = datetime.strptime(line[i],'%H:%M:%S').time()
                                    if time < ti:
                                        line.insert(i,time)
                                        out = True
                                        break

                f.close()
                with open('time.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                print('Time added successfully ')
                choice = input('Want to add more Time (y/n)?: ')
                while choice not in ['y','n','yes','no']:
                    choice = input(('Enter valid choice: ')).lower()
                if choice in ['n', 'no']:
                    break
            elif choice == '2':
                clear()
                result1= pyfiglet.figlet_format("Delete Time".center(40))
                print(result1)
                final = [['City']]
                add = []
                with open('city.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file, delimiter = ',')
                    for line in csv_reader:
                        for i in line:
                            self.locations.append(i)
                            add.append(i)
                            final.append(add)
                            add = []

                read_file.close()
                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())
                read_file.close()

                city = input('Enter city: ')
                while city not in self.locations:
                    city = input('Enter supported city: ')

                final = [['Theater']]
                add = []
                print('Existing Theaters : ')
                with open('theaters.csv', 'r') as read_file:
                    csv_reader = csv.reader(read_file)
                    for line in csv_reader:
                        if line == []:
                            break

                        for i in range(len(line)):
                            if line[0] == city:
                                if i != 0:
                                    add.append(line[i])
                                    final.append(add)
                                    add = []

                read_file.close()
                Tab = Texttable()
                Tab.add_rows(final)
                print(Tab.draw())
                read_file.close()
                match = False
                while match == False:
                    final = [['Movie']]
                    add = []
                    theater = input('Enter name of theatre: ')
                    print('Existing movies : ')
                    with open('movies.csv', 'r') as read_file:
                        csv_reader = csv.reader(read_file)
                        for line in csv_reader:
                            if line == []:
                                continue
                            add.append(line[0])
                            final.append(add)
                            add = []

                    read_file.close()
                    Tab = Texttable()
                    Tab.add_rows(final)
                    print(Tab.draw())
                    read_file.close()

                    movie = input('Enter Movie: ')
                    times = {}
                    count = 1
                    now = datetime.now().time()
                    with open('time.csv', 'r') as read_file:
                        csv_reader = csv.reader(read_file, delimiter = ',')
                        for line in csv_reader:
                            if line[0] == theater and line[1] == movie:
                                match = True
                                for i in range(len(line)):
                                    if i not in [0,1]:
                                        ti = datetime.strptime(line[i],'%H:%M:%S').time()
                                        times[str(count)] = ti
                                        count += 1

                    read_file.close()
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

                print('Enter Time to be deleted: ')
                ID = input('Enter ID ')
                while ID not in times.keys():
                    ID = input('Enter ID: ')

                time = times[ID]

                out = False
                with open('time.csv', 'r') as f:
                    r = csv.reader(f)
                    lines = list(r)
                    for line in lines:
                        if out:
                            break
                        if line[0] == theater and line[1] == movie:
                            for i in range(len(line)):
                                if i not in [0,1]:
                                    ti = datetime.strptime(line[i],'%H:%M:%S').time()
                                    if time == ti:
                                        line.remove(line[i])
                                        out = True
                                        break

                f.close()
                with open('time.csv','w', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                f.close()

                print('Time deleted successfully ')
                choice = input('Want to delete more Time (y/n)?: ')
                while choice not in ['y','n','yes','no']:
                    choice = input(('Enter valid choice: ')).lower()
                if choice in ['n', 'no']:
                    break

if __name__ == '__main__':
    result1 = pyfiglet.figlet_format("BOOK  MY ".center(40))
    result2= pyfiglet.figlet_format("CINEMA".center(40))
    print(result1)
    print(result2)
    final = [['Press', 'Action'],[1, 'admin'],[2,'user']]

    loged = Texttable()
    loged.add_rows(final)
    print(loged.draw())

    while True:
        choice = input('Enter your choice: ')

        while choice not in ['1', '2']:
            choice = input('Enter your choice (1 or 2): ')
        choice = int(choice)


        if choice == 2:
            final = [['Press', 'Action'],[1, 'Sign Up'],[2,'Login']]

            loged = Texttable()
            loged.add_rows(final)
            print(loged.draw())
            while True:
                choice = input('Enter your choice : ')
                while choice not in ['1', '2']:
                    choice = input('Enter your choice (1 or 2) : ')

                choice = int(choice)
                clear()

                # Login function
                if choice == 2:
                    result1= pyfiglet.figlet_format("Login".center(40))
                    print(result1)
                    while True:
                        check = False
                        while True:
                            ID = input('input ID: ')
                            with open('new_login.csv', 'r') as read_file:
                                fieldnames = ['ID']
                                csv_reader = csv.DictReader(read_file, fieldnames = fieldnames)
                                for line in csv_reader:
                                    if ID == line['ID']:
                                        check = True
                                        break
                                if check == False:
                                    print('Login ID doesn\'t exist !!')
                                    continue
                                else:
                                    break
                        password = input('Input password ')

                        # To check if the userID and password is present in the file
                        try:
                            check = False
                            with open('new_login.csv', 'r') as read_file:
                                fieldnames = ['ID', 'password']
                                csv_reader = csv.DictReader(read_file, fieldnames = fieldnames)
                                for line in csv_reader:
                                    if ID == line['ID'] and password == line['password']:
                                        print('Login sucessfull !!!')
                                        check = True
                                        break
                                if check == False:
                                    print('Invalid login ')
                                    continue
                                else:
                                    break
                        except FileNotFoundError:
                            print('First SignUp !!')
                            choice = 1

                    break

                # Signup function :
                if choice == 1:
                    result1= pyfiglet.figlet_format("Sign Up".center(40))
                    print(result1)
                    while True:
                        ID = input('Enter your user ID : ')
                        flag = False
                        try:
                            with open('new_login.csv', 'r') as read_file:
                                fieldnames = ['ID']
                                csv_reader = csv.DictReader(read_file, fieldnames = fieldnames)
                                for line in csv_reader:
                                    if ID == line['ID']:
                                        print('Username already taken ')
                                        flag = True
                                        break
                                if flag == True:
                                    continue
                                break
                            break

                        except FileNotFoundError:
                            pass



                    while True:
                        password = input('Set your password : ')
                        config = input('Confirm Your password : ')
                        if password == config:
                            PASSWORD = {'ID' : ID,
                                        'password' : password}
                            print('Account successfully setup ')
                            break
                        else:
                            print('Passwords didn\'t match')
                            continue

                    # To append the user ID and password in the file
                    with open('new_login.csv', 'a', newline = '') as new_file:
                        fieldnames = ['ID', 'password']
                        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames ,delimiter = ',')
                        csv_writer.writerow(PASSWORD)
                    break
                else:
                    print('Enter valid choice: ')
                    continue

            use = user()
            clear()
            use.select_location()
            clear()
            use.select_movies_time()
            clear()
            choice = use.select_theatre()
            while choice in ['n', 'no']:
                choice = use.select_theatre()
            clear()
            choice = use.select_date()
            while choice in ['n', 'no']:
                choice = use.select_date()
            clear()
            choice = use.select_time()
            while choice in ['n', 'no']:
                choice = use.select_time()
            clear()
            use.select_seats()
            t.sleep(5)
            use.food_menu()

            use.payment()
            use.Ticket()
            print('Your ticket has been booked ')
            break

        # admin
        elif choice == 1:
            password = input('Enter Password ')
            while password != accessKey:
                print('\n Incorrect Password\n')
                password = input('Enter Password ')

            result1= pyfiglet.figlet_format("Admin".center(40))
            print(result1)

            a = Admin()

            while True:
                Tab = Texttable()
                Tab.add_rows([['Press', 'Option'], ['1','To edit location'],['2', 'To edit movie'],['3', 'To edit Theater'],['4', 'To edit food menu'],['5', 'To edit timings'],['6', 'To edit Date'],['7', 'Exit']])
                print(Tab.draw())
                choice = input()
                while choice not in ['1','2','3','4','5','6','7']:
                    choice = input('Enter valid choice ').lower()
                if choice == '1':
                    clear()
                    a.modify_location()
                elif choice == '2':
                    clear()
                    a.modify_Movies()
                elif choice == '3':
                    clear()
                    a.modify_theatres()
                elif choice == '4':
                    clear()
                    a.Modify_food()
                elif choice == '5':
                    clear()
                    a.Modify_time()
                elif choice == '6':
                    clear()
                    a.Modify_date()
                elif choice == '7':

                    sys.exit()

        else:
            print('Enter valid choice ')
            continue
