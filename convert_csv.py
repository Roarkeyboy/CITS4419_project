import csv

data_dir = ['data_2_9/','data_9_9/']
for curr_dir in data_dir:
    for ii in range (1,14):
        with open(curr_dir+str(ii)+'.txt', 'r') as in_file:
            stripped = (line.strip() for line in in_file)
            lines = (line.split(",") for line in stripped if line)
            with open(curr_dir+str(ii)+'.csv', 'w') as out_file:
                writer = csv.writer(out_file)
                writer.writerows(lines)
    
