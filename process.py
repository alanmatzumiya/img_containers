import os, subprocess

branches = ['img_' + str(j) for j in range(1, 7)]
repo = "https://github.com/alanmatzumiya/img_containers.git"


def gitpush():
    sentence_1 = "git init"
    sentence_2 = " && git add ."
    sentence_3 = " && git commit -m 'auto'"
    sentence_4 = " && git push origin " 
    sentence = sentence_1 + sentence_2 + sentence_3 + sentence_4
    for branch in branches:
        #f = open("./" + branch + "/gitpush.py", "w")
        #f.write('import os\nos.system("' + sentence + branch + '")')
        #f.close()
        os.system("cd ./" + branch + " && python3 gitpush.py")
        
def gitclone():
    sentence = "git clone -b "
    for branch in branches:
        print(sentence + branch + " " + repo + " " + branch)
        #os.system(sentence + branch + " " + repo + " " + branch)

gitclone()        
