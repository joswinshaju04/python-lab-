def fibonacci(f):
    first_no=1
    second_no=0
    third_no=0
    for i in range (f):
        print(third_no,end=" ")
        third_no=first_no+second_no
        first_no=second_no
        second_no = third_no

