def cool():

    def super_cool():
        return 'I am very cool'

    return super_cool


some_func = cool()
print(some_func())
