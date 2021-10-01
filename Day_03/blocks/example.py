#file = open("myfile.txt")
#print(file.read())
#file1.close()

try:
    file = open("myfile.txt")
    print(file.read())

except Exception as e:
    pass
finally:
    print("This block alway run")
