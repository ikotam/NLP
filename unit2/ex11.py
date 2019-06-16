def Tab2Space(file):
    f = open(file, "r")
    lines = f.readlines()

    for line in lines:
        print(line.replace('\t', " "))
    
    f.close



Tab2Space("hightemp.txt")

# command line:
# expand -t1 hightemp.txt
# sed 's/\t/ /g' hightemp.txt
# echo hightemp.txt | tr -s [:space:] ' '