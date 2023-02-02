print("pascal programming")
print("pascal is a programming language from the 70s that was developed for teaching how to program because of its simplicity. ")
print("\n")
print("there is a flag stored in a string variable named, 'FLAG', your responsibility is to find a way to print it out to the console using a pascal instruction with proper syntax. Good luck!")
incommand = input("Enter Command Here:\n")
flag = "byuctf{i_l34rn3d_h0w_2_writeln_w1th_p4sc41}"
whale = """                                    ','. '. ; : ,','
                                      '..'.,',..'
                                         ';.'  ,'
                                          ;;
                                          ;'
                            :._   _.------------.___
                    __      :__:-'                  '--.
             __   ,' .'    .'             ______________'.
           /__ '.-  _\___.'          0  .' .'  .'  _.-_.'
              '._                     .-': .' _.' _.'_.'
       snd       '----'._____________.'_'._:_:_.-'--'"""
if incommand == "writeln(FLAG);":
    print(flag)
  
elif incommand == "spoutingwhale":
    print(whale)  

else:
    print("That is not the way to print to the console in pascal")
#Here is the link I used for a refrence for the print to console instruction https://www.tutorialspoint.com/pascal/pascal_strings.htm#:~:text=The%20string%20in%20Pascal%20is,upon%20the%20system%20and%20implementation.