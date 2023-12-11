from dataclasses import dataclass
from typing import Tuple

def read_input(file: str = "input.txt") -> str:
    with open(file, "r") as f:
        return f.read().strip()

@dataclass
class Card:
    win: list[int]
    nums: list[int] 

    def matches(self):
        return sum([1 for i in self.nums if i in self.win])

    def score(self):
        output = 0
        for num in self.nums:
            if num in self.win:
                if output == 0:
                    output = 1
                else:
                    output *= 2
        return output

def parse_card(line: str) -> Card:
    win_str, nums_str = line.split(":")[1].strip().split("|")
    win_str = win_str.strip()
    nums_str = nums_str.strip()
    win = [int(i) for i in win_str.split(" ") if i]
    nums = [int(i) for i in nums_str.split(" ") if i]
    return Card(win, nums)

def parse_data(data) -> list[Card]: 
    return [parse_card(i) for i in data.split("\n") if i]

def p1_test():
    data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    output = sum([i.score() for i in parse_data(data)])
    print(f"p1_test: {output}")

def p1():
    data = read_input()
    output = sum([i.score() for i in parse_data(data)])
    print(f"p1: {output}")

def p2_test():
    data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    cards = parse_data(data)
    cards_dict = {i: 1 for i in range(len(cards))}
    for i in range(len(cards)):
        matches = cards[i].matches()
        for j in range(matches):
            if cards_dict.get(i+j+1):
                cards_dict[i+j+1] += cards_dict[i]
    output = sum(cards_dict.values())
    print(f"p1_test: {output}")

def p2():
    data = read_input()
    cards = parse_data(data)
    cards_dict = {i: 1 for i in range(len(cards))}
    for i in range(len(cards)):
        matches = cards[i].matches()
        for j in range(matches):
            if cards_dict.get(i+j+1):
                cards_dict[i+j+1] += cards_dict[i]
    output = sum(cards_dict.values())
    print(f"p1: {output}")

if __name__=="__main__":
    p1_test()
    p1()
    p2_test()
    p2()
