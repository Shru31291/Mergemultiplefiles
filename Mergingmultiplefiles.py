def d():
        import os
        import re
        path = "C:/Users/DELL/Desktop/testfile/Testfilex"
        file = os.listdir(path)
        for file in os.listdir(path) :
                  with open(os.path.join(path, file)) as infile :
                     with open("C:/Users/DELL/Desktop/testfile/Testfiley/Testfiley.txt", "a+") as outfile :
                      for line in infile :
                       outfile.write(line + '\n')
                       continue
