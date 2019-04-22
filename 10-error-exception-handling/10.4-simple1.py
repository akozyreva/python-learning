a = 1
b = 2
print(a)
print(B)

# and I can run pylint 10.4-simple1.py and see somth like this
# errors and styling problems
#  pylint 10.4-simple1.py
# ************* Module 10.4-simple1
# 10.4-simple1.py:1:0: C0103: Module name "4-simple1" doesn't conform to snake_case naming style (invalid-name)
# 10.4-simple1.py:1:0: C0111: Missing module docstring (missing-docstring)
# 10.4-simple1.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# 10.4-simple1.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
# 10.4-simple1.py:4:6: E0602: Undefined variable 'B' (undefined-variable)
# -------------------------------------
# Your code has been rated at -12.50/10
