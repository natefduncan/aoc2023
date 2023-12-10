def read_input(file: str = "input.txt") -> str:
    with open(file, "r") as f:
        return f.read().strip()

def get_nums(line: str) -> list[int]:
    return [int(i) for i in line if i.isdigit()]

def get_calibration_value(nums: list[int]) -> int:
    return int(str(nums[0]) + str(nums[-1]))

def p1():
    data = read_input()
    nums_arr = [get_nums(line) for line in data.split("\n")]
    cal_values = [get_calibration_value(arr) for arr in nums_arr]
    sum_cal_values = sum(cal_values)
    print(f"D1.1: {sum_cal_values}")

WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 

def get_nums2(line: str) -> list[int]:
    out = []
    for i, c in enumerate(line):
        if c.isdigit():
            out.append(int(c))
        for j, word in enumerate(WORDS):
            if line[i:].startswith(word):
                out.append(j+1)
    return out

def p2():
    data = read_input()
    nums_arr = [get_nums2(line) for line in data.split("\n")]
    cal_values = [get_calibration_value(arr) for arr in nums_arr]
    sum_cal_values = sum(cal_values)
    print(f"D1.2: {sum_cal_values}")

def p2_test():
    data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    nums_arr = [get_nums2(line) for line in data.split("\n")]
    cal_values = [get_calibration_value(arr) for arr in nums_arr]
    sum_cal_values = sum(cal_values)
    print(f"D1.2t: {sum_cal_values}")


if __name__=="__main__":
    p1()
    p2()
    p2_test()
