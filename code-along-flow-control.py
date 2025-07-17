'''
our_number = 42
is_guessed = False
while not is_guessed:
    guess = int(input('Enter you guess: '))
    if guess == our_number:
        print('Hooray!')
        is_guessed = 'True'
    elif guess > our_number:
        print('Too high!')
    else:
        print('Too low!')
'''
'''
counter = 1
while counter < 20:
    if counter % 3 == 0 and counter % 5 == 0:
        counter += 1
        continue
        print(f'{counter}: Fizzbuzz')
    elif counter % 3 == 0:
        print(f'{counter}: Fizz')
    elif counter % 5 == 0:
        print(f'{counter}: Buzz')    
    counter+= 1
else:
    print('Done with while loop')
'''
'''
# for loop examples
loop_range = range(1,5)
for i in loop_range:
    print(f'{i}: {i * "*"}')
'''
loop_range = range(1,11)
for i in loop_range:
    print(f'Iteration {i}')

# for loop with list
fruits = ['apple', 'banana', 'cherry', 'pineapple', 'guava']
for i in fruits:
    print(f'Fruit : {i}')

numbers = [1, 111, 12, 34, 200]   

for value in numbers:
    if value > 20:
        print(value)