
# 9.4

try:
    raise Exception("OopsException")

except Exception as other:
    print(f'예외 발생:{other}')
    print("Caught an oops")
else:
    pass
