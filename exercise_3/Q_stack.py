# In MoMo, push 
print("Momo Stack Operations")
MOMO_stack = []
def MOMO_push(items):
    MOMO_stack.append(items)
    
MOMO_push("PIN")
MOMO_push("AMOUNT")
MOMO_push("CONFIRM")
print(f"Momo Stack: {MOMO_stack} \n")

# Undo last.
print("Undo last operation:")
def MOMO_undo():
    if MOMO_stack:
        removed_item = MOMO_stack.pop()
        print(f"Removed From momo stack: {removed_item}")
    else:
        print("Stack is empty, nothing to undo.")
MOMO_undo()
print(f"after Undo, it remains: {MOMO_stack} \n")

# UR pushes ["Quiz1", "Quiz2", "Quiz3"].
print("UR Stack Operations")
UR_stack = []
def UR_push(items):
    UR_stack.append(items)
    print(f"Pushed to UR stack: {items}")

UR_push("Quiz1")
UR_push("Quiz2")
UR_push("Quiz3")
print(f"UR Stack: {UR_stack} \n")

# Pop two.
print("Pop two operations:")
def UR_pop():
    if UR_stack:
        for _ in range(2):
            removed_item = UR_stack.pop()
            print(f"Removed From UR stack: {removed_item}")
    else:
        print("Stack is empty, nothing to pop.")
UR_pop()
print(f"after Pop, it remains: {UR_stack} \n")

# Challenge: Reverse "RWANDA" using stack.
print('Challenge: Reverse "RWANDA" using stack.')
def reverse_string_using_stack(input_string):
    stack = []
    for char in input_string:
        stack.append(char)
    
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string
reversed_result = reverse_string_using_stack("RWANDA")
print(f'Reversed "RWANDA": {reversed_result} \n')
