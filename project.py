def exchange(nums, index):
    result = nums[index + 1:] + nums[:index + 1]
    return result


def max_even_odd(nums, text):
    max_num = -99999999999
    last_index = None
    if text == "odd":
        for index, num in enumerate(nums):
            if num % 2 != 0:
                if num >= max_num:
                    max_num = num
                    last_index = index
    elif text == "even":
        for index, num in enumerate(nums):
            if num % 2 == 0:
                if num >= max_num:
                    max_num = num
                    last_index = index
    if not last_index and last_index != 0:
        last_index = "No matches"
    return last_index


def min_even_odd(nums, text):
    min_num = 99999999999
    last_index = None
    if text == "odd":
        for index, num in enumerate(nums):
            if num % 2 != 0:
                if num <= min_num:
                    min_num = num
                    last_index = index
    elif text == "even":
        for index, num in enumerate(nums):
            if num % 2 == 0:
                if num <= min_num:
                    min_num = num
                    last_index = index
    if not last_index and last_index != 0:
        last_index = "No matches"
    return last_index


def first_even_odd(nums, text, index):
    first_nums = []
    counter = 0
    if text == "odd":
        for i in nums:
            if 0 < index <= len(nums):
                if i % 2 != 0 and counter < index:
                    first_nums.append(i)
                    counter += 1
            else:
                first_nums = "Invalid count"
    elif text == "even":
        for i in nums:
            if 0 < index <= len(nums):
                if i % 2 == 0 and counter < index:
                    first_nums.append(i)
                    counter += 1
            else:
                first_nums = "Invalid count"
    return first_nums


def last_even_odd(nums, text, index):
    last_nums = []
    counter = 0
    if text == "odd":
        for i in nums[::-1]:
            if 0 < index <= len(nums):
                if i % 2 != 0 and counter <= index:
                    last_nums.append(i)
                    counter += 1
            else:
                last_nums = "Invalid count"
    elif text == "even":
        for i in nums[::-1]:
            if 0 < index <= len(nums):
                if i % 2 == 0 and counter <= index:
                    last_nums.append(i)
                    counter += 1
            else:
                last_nums = "Invalid count"
    if last_nums != "Invalid count":
        last_nums = last_nums[::-1]
    return last_nums


nums = [int(i) for i in input().split()]

command = input()
while command != "end":
    line = command.split()
    name_function = line[0]

    if name_function == "exchange":
        if 0 <= int(line[1]) < len(nums):
            nums = exchange(nums, int(line[1]))
        else:
            print("Invalid index")
    elif name_function == "max":
        print(max_even_odd(nums, line[1]))
    elif name_function == "min":
        print(min_even_odd(nums, line[1]))
    elif name_function == "first":
        print(first_even_odd(nums, line[2], int(line[1])))
    elif name_function == "last":
        print(last_even_odd(nums, line[2], int(line[1])))

    command = input()
print(nums)
