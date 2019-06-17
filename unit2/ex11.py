def Tab2Space(file):
    fi = open(file, "r")
    fo = open(file+'out', 'w')
    lines = fi.readlines()

    for line in lines:
        # print(line.replace('\t', " "))
        fo.write(line.replace('\t', " ") + '\n')
    fi.close
    fo.close



Tab2Space("hightemp.txt")

# command line:
# expand -t1 hightemp.txt
# sed 's/\t/ /g' hightemp.txt
# echo hightemp.txt | tr -s [:space:] ' '