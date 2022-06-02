flag = 'byuctf{vivre_en_france_le_clavier_francais_est_le_meilleur_allez_azertyqwm}'

string = input("Entrez votre le mot de passe> ")

azertyString = ""
for i in string:

    if( i == 'q'):
        azertyString += 'a'

    elif( i == 'w'):
        
        azertyString +='z'
    elif( i == 'a'):
            
        azertyString +='q'
    elif( i == ';' or i ==  ':'):
            
        azertyString +='m'
    elif( i == 'z'):
            
        azertyString +='w'
    elif( i == 'm'):
            
        azertyString +=','
    elif (i == ','):
        azertyString += ';'
    elif(i == '_'):
        azertyString += '°'
    elif(i == '°'):
        azertyString += '_'
    elif(i == '8'):
            azertyString += '_'
    elif (i == 'z'):
        azertyString += 'w'
        
    else:
        azertyString += i


string = azertyString

ascii_values = []   
for i in range(0, len(flag)):
    if(i >= len(string)):
        stringValue = 0
    else:
        stringValue = ord(string[i])
    flagValue = ord(flag[i])
    ascii_values.append(flagValue -stringValue)

print(ascii_values)

if(flag == string and len(flag) == len(string)):
    print("The flag is - byuctf{vivre°en°frqnce°le°clqvier°frqncqis°est°le°;eilleur°qllew°qwertyaz;}")