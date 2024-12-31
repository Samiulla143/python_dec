tkts=[1,2,3,4,5]
print('Available Tickets', tkts)
user_inp = int(input('Enter quantity of tickets u wnanna buy:'))
for x in range(user_inp):
    ticket_num = int(input('enter ticket number:'))
    tkts.remove(ticket_num)
print('Available tkts', tkts)