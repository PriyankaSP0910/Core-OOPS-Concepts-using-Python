hile(True):
        print("="*61)
        print("MENU")
        print("\n1.Value Error\n2.Name Error\n3.Type Error\n4.IO Error\n5.Filenotfound error\n0.Exit\n")
        print("="*61)
        ch=int(input("Enter your choice: "))
        if(ch == 1):
                try:
                        f=open('f1.txt','z')
                        print('Successful')
                except ValueError as e:
                        print("Value Error",e)
        elif(ch == 2):
                try:
                        f=opens('blue.txt','w')
                        print('Successful')
                except NameError as e:
                        print("Name Error",e)
        elif(ch == 3):
                try:
                        f=open('red.txt','w','r')
                        f.write()
                        print('Successful')
                except TypeError as e:
                        print("Type Error",e)
        elif(ch == 4):
                try:
                        f=open('yellow.txt','w')
                        f.write('Hello color yellow')
                        f.read()
                        print('Successful')
                except IOError as e:
                        print("Input Output error ",e)
        elif(ch == 5):
                try:
                        f=open('f1.txt','r')
                        print('Successful')
                except FileNotFoundError as e:
                        print("File not found Error",e)
        elif(ch == 0):
                break
        else:
                print("Invalid input")
