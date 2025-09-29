class Model:                   
    def __init__(self, name , value):
        self.value = value       
        self.name = name

def view(model):
    print('\033[0;35m')
    print('---------------------------------')
    print('update name: ' + model.name)
    print('update value: ' + str(model.value))
    print('---------------------------------')
    print('\033[0;37m')

def controller():
    n = input('name is: ')
    v = input('value is: ')
    return Model(n,v)

# main loop
while True:
    model = Model('default', 0)
    model = controller()
    view(model)