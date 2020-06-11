start_range = int(input())
end_range = int(input())
for num_to_check in range(start_range,end_range+1):
    if(num_to_check % 75 == 0) & (num_to_check % 100 == 0):
        print(num_to_check)