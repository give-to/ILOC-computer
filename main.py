import re

memory = {}
registers = {}


# 定义 ILOC 操作对应的函数
def loadI(value, reg):
    registers[reg] = value


def load(reg1, reg2):
    registers[reg2] = memory[registers[reg1]]


def store(reg1, reg2):
    memory[registers[reg2]] = registers[reg1]


def add(reg1, reg2, reg3):
    registers[reg3] = registers[reg1] + registers[reg2]


def sub(reg1, reg2, reg3):
    registers[reg3] = registers[reg1] - registers[reg2]


def mult(reg1, reg2, reg3):
    registers[reg3] = registers[reg1] * registers[reg2]


def lshift(reg1, reg2, reg3):
    registers[reg3] = registers[reg1] << registers[reg2]


def rshift(reg1, reg2, reg3):
    registers[reg3] = registers[reg1] >> registers[reg2]


def output(value):
    print(f"mem({value}) = {memory.get(value, 0)}")


# 处理每一行指令
def execute_instruction(instruction):
    # parts = instruction.split("\s")
    parts = re.split('[\s,(=>)]+', instruction)
    operation = parts[0]

    if operation == "loadI":
        value = int(parts[1])
        reg = parts[2]
        loadI(value, reg)
    elif operation == "load":
        reg1 = parts[1]
        reg2 = parts[2]
        load(reg1, reg2)
    elif operation == "store":
        reg1 = parts[1]
        reg2 = parts[2]
        store(reg1, reg2)
    elif operation == "add":
        reg1 = parts[1]
        reg2 = parts[2]
        reg3 = parts[3]
        add(reg1, reg2, reg3)
    elif operation == "sub":
        reg1 = parts[1]
        reg2 = parts[2]
        reg3 = parts[3]
        sub(reg1, reg2, reg3)
    elif operation == "mult":
        reg1 = parts[1]
        reg2 = parts[2]
        reg3 = parts[3]
        mult(reg1, reg2, reg3)
    elif operation == "lshift":
        reg1 = parts[1]
        reg2 = parts[2]
        reg3 = parts[3]
        lshift(reg1, reg2, reg3)
    elif operation == "rshift":
        reg1 = parts[1]
        reg2 = parts[2]
        reg3 = parts[3]
        rshift(reg1, reg2, reg3)
    elif operation == "output":
        value = int(parts[1])
        output(value)


with open("input_1", 'r') as f_input:
    instructions = f_input.readlines()
    # 执行所有指令
    for instruction in instructions:
        execute_instruction(instruction)
