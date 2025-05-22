import datetime

log_file='log.txt'

timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M"%S')

with open(log_file,'a') as file:
    file.write(f'{timestamp} Script was executed')

print('The log is written')
