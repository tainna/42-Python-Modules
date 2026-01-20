def ft_count_harvest_recursive():
    target = int(input("Days until harvest: "))

    def loop(current_day):
        if current_day > target:
            print("Harvest time!")
            return
        else:
            print("Day", current_day)
            loop(current_day + 1)
         
    loop(1)