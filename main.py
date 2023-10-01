PLACEHOLDER = '[name]'

with open('Input/Names/invited_names.txt', 'r') as f:
    names = f.readlines()

with open('Input/Letters/starting_letter.txt', 'r') as file:
    old_invite = file.read()
    for name in names:
        new_invite = old_invite.replace(PLACEHOLDER, name.strip('\n'))
        with open(f'Output/ReadyToSend/invited_{name}', 'w') as new_file:
            new_file.write(new_invite)

