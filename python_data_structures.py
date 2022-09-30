# Define the lists 
from gettext import _TranslationsReader


participants = ['Dan', 'Felix', 'Judy', 'Ayesha', 'Yu', 'David', 'Andrea', 'Christina', 'Kevin', 'Kinam', 'Li-Hsin', 'Matt', 'Nicole', 'Susann', 'Emily']
participants_2 = participants
participants_3 = participants.copy()

#Print the lists
print(participants)
print(participants_2)
print(participants_3)

#Append the list
participants.append('Alastair')
participants.append('Lance')

#Print the lists
print(participants)
print(participants_2)
print(participants_3)

#Select 3rd and 5th Participants
print(participants[2])
print(participants[4])

#Sort list and select 3rd and 5th participants
participants.sort()
print(participants)
print(participants[2])
print(participants[4])

# Select the first 2 letters of the string in the third value of your participants list
participants[3][:2]


# Iterate over the participants list and set the names to keys in a dictionary with the value as 'trainee’ or ‘trainer’ depending on thier role
course = {}

for name in participants:
    if name == 'David' or name == 'Andrea':
        course[name] = 'trainer'

    else:
        course[name] = 'trainee'

print(course)


#Use a for loop to iterate over your dictionary and print the values of the keys only if they are trainees

for name in course.keys():
    if course.get(name, 0) == 'trainee':
        print(name)

for name, position in course.items():
    if position == 'trainee':
        print(name)



# Define the tuple

ppts = ('Dan', 'Felix', 'Judy', 'Ayesha', 'Yu', 'David', 'Andrea', 'Christina', 'Kevin', 'Kinam', 'Li-Hsin', 'Matt', 'Nicole', 'Susann', 'Emily')
ppts_2 = ppts
ppts_3 = ppts.copy()

#Print the lists
print(ppts)
print(ppts_2)
print(ppts_3)

#Append the list
ppts.append('Alastair')
ppts.append('Lance')

#Print the lists
print(ppts)
print(ppts_2)
print(ppts_3)

#Select 3rd and 5th Participants
print(ppts[2])
print(ppts[4])

#Sort list and select 3rd and 5th participants
ppts.sort()
print(ppts)
print(ppts[2])
print(ppts[4])

# Select the first 2 letters of the string in the third value of your participants list
ppts[3][:2]
      



