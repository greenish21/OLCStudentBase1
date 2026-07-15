egg_code = ['1UK42211','2FR9292','1UK29292','0NL24555','0NL93933']
valid = 0
check = 0 # 1) Moved check outside loop
for i in range(len(egg_code)):
    if len(egg_code[i]) > 7:
        check += 1
    if egg_code[i][0] in [0,1,2,3]: # 4) Added missing commas
        check += 1
    if egg_code[i][1:3].isalpha(): # 2) Missing bracket
        check += 1
    if egg_code[i][3:].isdigit(): # 3) Missing bracket
        check += 1
    if check == 3:
        valid = 1
if valid == 1: # 7) Changed to 1
    print("Codes for the entire batch of eggs are valid.")
    # Collate the number of eggs sampled according to farm method
    farm_method_eggs = [0,0,0,0]
    for j in range(len(egg_code)):
        farm_method_eggs[egg_code[j][0]] += 1
    farm_method = ['Organic','Free Range','Barn','Cage']
    for k in range(len(egg_code)):
        print("Number of {0} eggs: {1}".format(farm_method[k],farm_method_eggs[k]))
    # Collate the number of eggs sampled according to country of origin
    countries = ['UK', 'FR', 'NL']
    countries_eggs = [0,0,0]
    for m in range(len(egg_code)):
        for n in range(len(countries)):
            if egg_code[m][:2] == countries[n]:
                countries_eggs[m] += 1 # 5) Indentation error
    for p in range(len(countries_eggs)):
        print("Number of {0} eggs: {1}".format(countries[p], countries_eggs[p]))
else: # 6) Missing colon
    print("Invalid egg codes found for this batch of eggs.")
    print("No data will be presented.")