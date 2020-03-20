import csv
from trig_app.models import Denomination,Retailer


with open('carrefour.csv', 'r') as file:
    reader = csv.reader(file)

    for line in reader:
        #line = parse line to a list
        # add some custom validation\parsing for some of the fields

        foo = Denomination(denom_name=line)
        try:
            foo.save()
        except:
            # if the're a problem anywhere, you wanna know about it
            print("there was a problem with line", line) 