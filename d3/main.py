from __future__ import annotations
from typing import Tuple, Optional
from dataclasses import dataclass
import re

PART_NUMBER_RE = re.compile(r"(\d+)")
SYMBOL_RE = re.compile(r"([^\.\d])")

@dataclass
class Symbol:
    text: str
    line: int
    loc: int

    def near_parts(self, parts: list[PartNumber]) -> list[PartNumber]:
        output = []
        for part in parts:
            if abs(self.line - part.line) <= 1 and (abs(part.span[0] - self.loc) <= 1 or abs(part.span[1] - self.loc - 1) <= 1):
                output.append(part)
        return output

@dataclass
class PartNumber:
    text: str 
    line: int
    span: tuple[int, int]

    def near_symbol(self, symbols: list[Symbol]) -> Tuple[bool, Optional[Symbol]]:
        for symbol in symbols:
            if abs(symbol.line - self.line) <= 1 and (abs(self.span[0] - symbol.loc) <= 1 or abs(self.span[1] - symbol.loc - 1) <= 1):
                return (True, symbol)
        else:
            return (False, None)

def find_part_numbers(line: str, line_no: int) -> list[PartNumber]:
    output = []
    for match in PART_NUMBER_RE.finditer(line): 
        output.append(
            PartNumber(
                text=match.group(), 
                line=line_no, 
                span=match.span()
            )
        )
    return output

def find_symbols(line: str, line_no: int) -> list[Symbol]:
    output = []
    for match in SYMBOL_RE.finditer(line): 
        output.append(
            Symbol(
                text=match.group(), 
                line=line_no, 
                loc=match.span()[0]
            )
        )
    return output


def read_input(file_path: str = "input.txt"):
    with open(file_path, "r") as f:
        return f.read()

def parse_data(data: str) -> Tuple[list[PartNumber], list[Symbol]]:
    parts = []
    symbols = []
    for i, line in enumerate(data.split("\n")):
        if line:
            parts += find_part_numbers(line, i)
            symbols += find_symbols(line, i)
    return (parts, symbols)


def p1_test(): 
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    parts, symbols = parse_data(data)  
    output = 0
    for part in parts:
        near_bool, symbol = part.near_symbol(symbols)
        if near_bool:
            output += int(part.text)
    print(f"p1_test: {output}")

def p1():
    data = read_input()
    parts, symbols = parse_data(data)  
    output = 0
    for part in parts:
        near_bool, symbol = part.near_symbol(symbols)
        if near_bool:
            output += int(part.text)
    print(f"p1: {output}")

def p2_test():
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    parts, symbols = parse_data(data)
    output = 0
    for symbol in symbols:
        near_parts = symbol.near_parts(parts)
        if len(near_parts) == 2:
            p1, p2 = near_parts
            if symbol.text == "*":
                output += int(p1.text) * int(p2.text)
    print(f"p2_test: {output}")

def p2():
    data = read_input()
    parts, symbols = parse_data(data)
    output = 0
    for symbol in symbols:
        near_parts = symbol.near_parts(parts)
        if len(near_parts) == 2:
            p1, p2 = near_parts
            if symbol.text == "*":
                output += int(p1.text) * int(p2.text)
    print(f"p2: {output}")

if __name__=="__main__":
    p1_test()
    p1()
    p2_test()
    p2()

