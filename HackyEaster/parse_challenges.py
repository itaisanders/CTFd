import os

years = ['2021', '2022', '2023', '2024']
challenges_no_files = []
challenges_with_files = []

for year in years:
    challenges_folders = os.listdir(f'/workspaces/CTFd/HackyEaster/{year}/')
    for folder in challenges_folders:
        #challenge_props = open(f'/workspaces/CTFd/HackyEaster/{year}/{folder}/challenge.properties')
        #challenge_props.read()
        
        props_dict = {}
        print(f'{year}/{folder}')
        with open(f'/workspaces/CTFd/HackyEaster/{year}/{folder}/challenge.properties', 'r') as f:
            for line in f:
                # print(line)
                if line != '\n':
                    key, value = line.strip().split('=')
                    props_dict[key] = value
        # print(props_dict)

        # GET DESCRIPTION
        description = f"![{props_dict['title']}](https://raw.githubusercontent.com/PhilippSieber/hackyeaster-{year}/master/challenges/{folder}/banner.jpg)\n\n"
        description += open(f'/workspaces/CTFd/HackyEaster/{year}/{folder}/text.md').read()
        description += f'\n\n\n----\nCreated by `{props_dict["author"]}` for `Hacky Easter {year}`'
        #print(description)

        # DOWNSIZE CATEGORIES - ONLY ONE ALLOWED
        category = ''

        # GET HINTS
        hint = ""
        if os.path.exists(f'/workspaces/CTFd/HackyEaster/{year}/{folder}/hint.md'):
            # print(f'found: {year}/{folder}/hint.md')
            hint = f"{open(f'/workspaces/CTFd/HackyEaster/{year}/{folder}/hint.md').read()}"
            # print(challenge)
        # name,description,category,value,type,state,max_attempts,flags,tags,hints,type_data
        challenge = [props_dict['title'], rf'{description}', props_dict['categories'], f'{props_dict["points"]}', 'standard', 'visible', '0', props_dict['flag'],'',hint,'']
        # print(challenge)

        if os.path.exists(f'/workspaces/CTFd/HackyEaster/{year}/{folder}/files/'):
            #print("challenge has file!")
            challenges_with_files.append(challenge)
        else:
            #print("no files in challenge")
            challenges_no_files.append(challenge)

#print (challenges_no_files)
#print (challenges_with_files)

import json
no_files_csv_file_path = f'/workspaces/CTFd/HackyEaster/challenges-without-files.csv'
csv_header = 'name,description,category,value,type,state,max_attempts,flags,tags,hints,type_data'
no_files_csv_file = open(no_files_csv_file_path, 'w')
no_files_csv_file.write(f'{csv_header}\n')
for challenge in challenges_no_files:
    i = 0
    for value in challenge:
        no_files_csv_file.write(json.dumps(value))
        i += 1
        if i <= 10:
            no_files_csv_file.write(',')
    no_files_csv_file.write('\n')


        
        


