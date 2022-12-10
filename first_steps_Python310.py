"""
This Module contains a function
 - prints reverse hello world
 - select case test given by a variable
 - read a txt file and print

:Author         Diogo Pereira
:Created on     2022-11-02 
"""

def helloworld():
    msg ="hello world"
    msg = msg[::-1]
    print(msg)

def select_case_test(status_test):
    match status:
        case 50:
            print("Bad")
        case 40:
            print("GOOD")
        case _:
            print("All cases not listed above")

def test_open_file():
    #with this method the do not implicitly need close file  
    with open('test read file.txt') as f:
        text= f.read()
        print(text)



helloworld()
status_test = 40
select_case_test(status_test)
test_open_file()
