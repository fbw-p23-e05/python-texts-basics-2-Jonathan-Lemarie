
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

last_letters = text[-10:]  
# putting the : after the amount desired in the bracket instead of before will take the last characters instead of the beginning of that variable.

print('Last ten characters:', last_letters)


# correction 

print('Last ten characters:', text[-10:])
# or

print(f'Last ten characters: {text[-10:]} ')
