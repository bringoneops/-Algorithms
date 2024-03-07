import matplotlib.pyplot as plt

# Operations to perform on the stack
operations = ['PUSH(4)', 'PUSH(1)', 'PUSH(3)', 'POP()', 'PUSH(8)', 'POP()']
stack = []  # Simulating the stack
states = []  # To store the state of the stack after each operation

# Perform the operations and store the state
for op in operations:
    if 'PUSH' in op:
        number = int(op.split('(')[1].split(')')[0])
        stack.append(number)
    elif 'POP' in op and stack:
        stack.pop()
    states.append(stack.copy())

# Visualization
fig, axs = plt.subplots(1, len(states), figsize=(15, 3))
for i, state in enumerate(states):
    axs[i].barh(range(len(state)), [1] * len(state))
    axs[i].set_yticks(range(len(state)))
    axs[i].set_yticklabels(reversed(state))
    axs[i].set_title(operations[i])
    axs[i].invert_yaxis()
    for spine in axs[i].spines.values():
        spine.set_visible(False)
    axs[i].get_xaxis().set_visible(False)
    axs[i].get_yaxis().set_ticks_position('none')
plt.tight_layout()
plt.show()
