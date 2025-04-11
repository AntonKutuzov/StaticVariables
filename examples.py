from StaticVars import static, counter, flags

# ============================================================================================= using `static` decorator
print('---=== Using `@static()` decorator ===---')
'''
Static decorator has one parameter 'static_vars' of type Dict[str, Any]. The strings passed as keys will become 
function's attributes, and the values of the dict will be their default values.
'''

@static({'i': 5})
def func():
    func.i += 1
    return func.i

print('func.i =', func.i)
print('call 1:', func())
print('call 2:', func())
print('call 3:', func())
print('func.i =', func.i)

# ============================================================================================ using `counter` decorator
print('\n---=== Using `@counter()` decorator ===---')
"""
Counter decorator is a special application of the @static() decorator. It has the following attributes:
start_with: int = 0     # the value we start counting from
step: int = 1           # the step we are counting with (1–2–3– with step 1, or 1–3–5– with step 2 and so on)
inc: bool = True        # 'inc' stands for 'increment'. True if the value of counter is increasing, False for opposite
min: int = None         # minimum value of counter. If counter gets lower, it stays at the closest possible value
max: int = None         # maximum value of counter. If counter gets higher, it stays at the closest possible value
"""

print('Only even numbers from 2 to 20 by using "step=2" and "start_with=2": ', end='')

@counter(start_with=2, step=2)
def count_calls():
    return count_calls.counter

print(*[count_calls() for _ in range(10)])

@counter()
def count_calls2():
    if count_calls2.counter >= 5:
        return True
    else:
        return False

print('Change the value from False to True when counted 5 times')
print([count_calls2() for _ in range(10)])
# try making maximum value smaller than 10 and see what happens. At max less than 5 (not including), all values
# will turn to False

# ============================================================================================== using `flags` decorator
print('\n---=== Using `@flags()` decorator ===---')
"""
Flags is another extension of @static() decorator, which allows creating flags with predefined boolean values. Try 
uncommenting the "return" values and see what happens.
"""

print('The three flags are "called", "intermediate" and "ended"')

@flags('called', 'intermediate', 'ended')
def func2():
    print(f'The three flags: {func2.called} {func2.intermediate} {func2.ended}')
    func2.called = True
    # return

    print('Some definitely important stuff to do...')
    print(f'The three flags: {func2.called} {func2.intermediate} {func2.ended}')
    func2.intermediate = True
    # return

    print('Some other definitely important stuff to do...')
    print(f'The three flags: {func2.called} {func2.intermediate} {func2.ended}')
    func2.ended = True
    # return

    print(f'The three flags: {func2.called} {func2.intermediate} {func2.ended}')

func2()
print(func2.called, func2.intermediate, func2.ended)
