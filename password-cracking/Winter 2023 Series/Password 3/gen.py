# opening the file in read mode
my_file = open("wordlist1.txt", "r")

out_file = open('out2.txt', 'a')
# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list = data.split("\n")
#print(data_into_list)

in_list_size = (len(data_into_list))
list1= data_into_list
list2 = data_into_list
list3 = data_into_list
a= 0
for x in list1:
    #print(x)
    for y in list2:
        #print(x + y + '\n')
        #out_file.write(x+y+"\n")
        for z in list3:
            print(x+y+z+"\n")
            out_file.write(x+y+z+"\n")
            



my_file.close()
out_file.close()