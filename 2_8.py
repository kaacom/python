# test 03/04-2:45
f_name = input()
f = open(f_name, 'r')
all_line = f.read()
parts = all_line.split('\n')
parts_1 = filter(None, parts)
numbers = [int(P) for P in list(parts_1)]
summ_num = sum(numbers)
print(summ_num)
f.close()
