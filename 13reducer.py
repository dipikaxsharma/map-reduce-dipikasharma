s = open(r"C:\Users\S530527\Documents\44517\map-reduce-dipikasharma\foodprepsort.txt","r")
out = r"C:\Users\S530527\Documents\44517\map-reduce-dipikasharma\foodprepreduce.txt"



thisKey = ""
thisValue = 0
data_dict = {}

for line in s:
    line_data = line.split('\t')
    name,prep_time = line_data[0], line_data[3].rstrip()
    if prep_time in data_dict.keys():
        data_dict[prep_time] +=1
    else:
        data_dict[prep_time] = 1

with open(out, 'w') as f: 
    for key, value in data_dict.items():
        f.write('%s:%s\n' % (key, value))

s.close()