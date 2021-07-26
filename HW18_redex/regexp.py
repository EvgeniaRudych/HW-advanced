import re

with open("django_success.log") as log_file:
    logfile = ''.join(log_file.read())
    res = re.sub(r'\[\d+\/\w+\/\d+\s(\d{2}:?){3}\]', '[XX/XXX/XXXX XX:XX:XX]', logfile)
    res = re.sub(r'\/admin\/', '****/****/****', res)
    with open('res.txt', 'w') as res_file:
        res_file.write(res)
        print(res_file)


exit(0)
