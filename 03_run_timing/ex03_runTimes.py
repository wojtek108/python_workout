def run_timing():
    number_of_runs = 0
    total_time = 0
    while True:
        one_run = input('Enter 10 km run time: ')
        if not one_run:
            break
        number_of_runs = number_of_runs + 1
        try:
            total_time = total_time + float(one_run)
        except ValueError:
            print('That is not a valid number')
            number_of_runs = number_of_runs - 1

    average_time = total_time / number_of_runs
    print(f'Average of {average_time: .2f} over {number_of_runs} runs')

run_timing()



