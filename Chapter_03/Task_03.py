motorcycle_list = ['Honda', 'Kawasaki', 'Harley Davidson', 'Simson', 'Mz',
                   'Yamaha', 'Suzuki']
first_message = "I would like to own %s motorcycle :)"

cars_list = ['Mercedes-Benz', 'BMW', 'Audi', 'Porshe', 'Ford', 'Rolls Royce',
                 'Ferrari']
second_message = "I would like to own %s car :)"

for x in motorcycle_list:
     print(first_message %x)

for x in cars_list:
    print(second_message %x)
