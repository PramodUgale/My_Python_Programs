r"""---------------------------------------------------------------
This program demonstrates usage of exec() function
----------------------------------------------------------------"""

def my_exec_func_with_file():
    r'''---------------------------------------------------------------
    This function reads python source file and pass it to exec function for
    execution
    ----------------------------------------------------------------'''
    data = open('sample.py','r')
    text = data.read()
    exec(text)
    data.close()

def my_exec_func_with_for():
    r'''---------------------------------------------------------------
    ----------------------------------------------------------------'''
    my_globals = {'my_int':4}
    my_locals = {'local_list':[1,2,3,4]}
    str = 'for i in local_list:\n print(i*my_int)'
    exec(str,my_globals,my_locals)

def my_exec_func():
    r'''---------------------------------------------------------------
    ----------------------------------------------------------------'''
    my_globals = {'my_int':3}
    my_locals = {'local_list':[1,2,3,4]}
    str = 'print(list(map(lambda x: x*my_int,local_list)))'
    exec(str,my_globals,my_locals)

def my_normal_func():
    r'''---------------------------------------------------------------
    ----------------------------------------------------------------'''
    my_int = 2
    local_list = [1,2,3,4]
    print(list(map(lambda x: x*my_int,local_list)))

def main():
    print('-------------------------------------')
    print('calling "my_normal_func()"....')
    my_normal_func()
    print('-------------------------------------')
    print('calling "my_exec_func()"....')
    my_exec_func()
    print('-------------------------------------')
    print('calling "my_exec_func_with_for()"....')
    my_exec_func_with_for()
    print('-------------------------------------')
    print('calling "my_exec_func_with_file()"....')
    my_exec_func_with_file()

if __name__ == '__main__':
    print("Hello!")
    main()
