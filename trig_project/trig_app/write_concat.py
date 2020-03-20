'''

tool to concatenate an sequential number
to the end of each line of the text file.
save the text file to a csv format then


'''
with open('intermarché.txt') as test_lines:
    count = 0
    for line in test_lines:
        count += 1
        data = [line.strip() + ' ' + str(count)] 
        with open('intermarche_v1.csv','a') as write_lines:
            for line1 in data:
                write_lines.write(line1+'\n')

