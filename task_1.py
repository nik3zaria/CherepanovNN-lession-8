import re
from re import *
x = {}
email_address_user = input('Введите свою почту: ')

def processing_user_mail(email_address_user):
    pattern = compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
    getting_the_email_address = ''.join(re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', email_address_user))
    is_valid = pattern.match(email_address_user)
    if is_valid:
        mail_name = getting_the_email_address.split('@')[:-1]
        mail_name = ''.join(mail_name)
        domain_name = re.split('[@|.]', getting_the_email_address)[1:2]
        domain_name = ''.join(domain_name)
        email_domain_and_name = dict({'username:': mail_name, 'domain:': domain_name})
        print(email_domain_and_name)
    else:
        print('Указан неверный email')


processing_user_mail(email_address_user)
