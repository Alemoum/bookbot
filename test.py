import sys 

my_book = sys.argv[1]

with open(my_book, 'r') as f:
    f_cont = f.read()

print(f_cont)