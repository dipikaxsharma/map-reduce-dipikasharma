import sys

thisKey = ""
thisValue = 0.0

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    name, cook_time = datalist

    if name != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = name 
      thisValue = 0.0
  
    # apply the aggregation function
    thisValue += float(cook_time)

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)