

#This program Determines The day you were born when you enter you name according to the day you were born



def day(name):
    if name in ['kojo', 'kwadwo','adwoa']:
        return  'Monday '
    elif name in ['kobby','kwabena','abena']:
        return 'Tuesday '
    elif name in ['kwaku','qwaku', 'akua','ekua']:
        return  'Wednesday '
    elif name in ['yaw', 'yaa','yaayaa']:
        return 'Thursday '
    elif name in ['kofi', 'fii', 'afia','efua','efia']:
        return 'Friday'
    elif name in ['kwame','kuame','ama']:
        return 'Saturday '
    elif  name in ['kwasi','kuasi','esi','akos','akosua']:
        return 'Sunday'
    else:
        return 'Input not valid'


def main():
    
    name = str(input("Enter your name according to The Day you were Born: ")).lower()
    results = day(name)
    print(f'You were Born On {results}')
        
main()






