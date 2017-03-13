aviation_data = [line.rstrip() for line in open('AviationData.txt')]

aviation_list=[]
for item in aviation_data:
    aviation_list.append(item.split('|'))
    
lax_code=[]

for row in aviation_list:
    
    for column in row:
        
        if column=='LAX94LA336':
            
            lax_code.append(row)
#Looping through each element in aviation_list is computationally expensive and cumbersome to write. It would have been better to convert the list in to a pandas dataframe and have searched in the dataframe using iloc


# linear time algorithm
for row in aviation_list:
    
    if 'LAX94LA336' in row:
        
        lax_code.append(row)
        
# constant time algorithm




aviation_dict_list=[]

for item in aviation_data:
    aviation_list.append(item.split('|'))