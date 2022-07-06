EMAILS = []
while True:
        print('1) input email 2) show emails 3) delete email')
        choices = int(input('enter ur choice 4) stop WHILE 5) rename'))
        if choices == 1:
            email = input('enter ur email')
            if email.endswith('@gmail.com'):
                EMAILS.append(email)
            else:
                print('invalid email')
        elif choices == 2:
            print(EMAILS)
        elif choices == 3:
            email = input('enter email that u wanna delete')
            if email in EMAILS:
                # index = EMAILS.index(email)
                # EMAILS.pop(index)
                EMAILS.remove(email)
                print("u sucessfully deleted email")
            else:
                print("email does not exist")
        elif choices == 4:
            break
        elif choices == 5:
            email == input('enter email')
            if email in EMAILS:
                new_email = input("enter ur new email")
                if email.endswith('@gmail.com'):
                    EMAILS.append(email)
                    EMAILS.remove(new_email)



        else:
            print('error !!')