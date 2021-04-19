import pyfiglet
from colorama import init
from termcolor import colored
import os
import getpass
import speech_recognition as sr
import os
import pyttsx3 as py


init()
#os.system("tput setaf 3")
a1_banner = pyfiglet.figlet_format("\n\tARTH2020.2.20 Group 4")
print(colored(a1_banner, 'green'))
print("""
\n\tTEAM MEMBERS
\t1.Pritee Dharme
\t2.Suyog Shinde 
\t3.Shrikant Luharia
\t4.Suraj Kumar
""")


#os.system("tput setaf 5")
a2_banner = pyfiglet.figlet_format("\n\tAutomation menu")
print(colored(a2_banner, 'red'))
py.speak("Welcome to my Automation menu!!")
print("\n\t\t\tWelcome to my Automation menu!!")
#os.system("tput setaf 7")
print("\n\t\t\t---------------------------")

#passwd = getpass.getpass("Enter your password : ")

#if passwd != "root":
 #  print("\n\tInvalid Password...")
 #r  exit()

key = input("Enter the Key name of aws: ")

def task():
   
    print("""
\n
        To launch the Hadoop menu
        To launch the AWS menu
        To launch the Partition menu
        To launch the docker menu
        Exit..
""")
    r = sr.Recognizer()
    with sr.Microphone() as s:
        py.speak("Start saying what do you want to do.....")
        print("start saying ....")
        audio = r.listen(s)
        py.speak("i got it...")
        print("i got it ...")

    kite = r.recognize_google(audio)
    print(kite)

    if ("docker" in kite ) or ("Docker" in kite ) and  ("menu" in kite ):
        dock()
    elif ("amazon" in kite ) or ("Amazon" in kite ) and ("menu" in kite ):
        aws()
    elif ("partition" in kite ) or ("Partition" in kite ) and  ("menu" in kite ):
        par()
    elif ("hadoop" in kite ) or  ("Hadoop" in kite ) and ("menu" in kite ):
        hadoop_all()
    else:
        os.system("exit")





def dock():
            
            import os
            import speech_recognition as sr 
            import subprocess as sp

            a3_banner = pyfiglet.figlet_format("\n\t Docker Menu")
            print(colored(a3_banner, 'blue'))
            print("""
            \tPress  1 : To install docker  00
            \tPress  2 : To start docker  
            \tPress  3 : To check status of docker  
            \tPress  4 : To install images of Docker  
            \tPress  5 : To check images of docker  
            \tPress  6 : To launch docker container  
            \tPress  7 : To run python on top of container  
            \tPress  8 : Exit.. 
            """)

            py.speak("Enter your remote IP Address....")
            ip = input("Enter the remote IP Address (eg. 1.2.3.4 ) : ")
            #py.speak("Tell your choice : ")
            #i = (input("Enter your choice.. : "))

            while True:
                r = sr.Recognizer()
                with sr.Microphone() as s:
                    py.speak("Start saying what do you want to do.....")
                    print("start saying ....")
                    audio = r.listen(s)
                    py.speak("i got it...")
                    print("i got it ...")

                data = r.recognize_google(audio)
                print(data)

                if (("install" in data) and ("docker" in data)):
                    os.system("ssh -i {} ec2-user@{} sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo".format(key, ip))
                    os.system("ssh  -i {} ec2-user@{} sudo dnf install docker-ce --nobest -y".format(key, ip))
                    dock()

                elif (("start" in data) and ("docker" in data)) or ("service" in data):
                    os.system("ssh -i {} ec2-user@{} sudo systemctl start docker".format(key, ip))
                    dock()
                
                elif (("stop" in data) and ("docker" in data)) or ("service" in data):
                    os.system("ssh -i {} ec2-user@{} sudo systemctl stop docker".format(key, ip))
                    dock()

                elif ("docker" in data) and (("check" in data) or ("status" in data)):
                    os.system("ssh  -i {} ec2-user@{} sudo systemctl status docker".format(key, ip))
                    dock()

                elif (("install" in data) and ("images" in data)):
                    x = input("Enter image name..>>  ")
                    os.system("ssh  -i {} ec2-user@{} sudo docker pull {}".format(key, ip, x))
                    dock()

                elif ("check" in data) or (("docker" in data) and ("images" in data)):
                    os.system("ssh -i {} ec2-user@{} sudo docker images".format(key, ip))
                    dock()

                elif (("launch" in data) and ("container" in data)) or ("docker" in data):
                    os_name = input("enter container name..>>  ")
                    image = input("Give image name that  you want..>>   ")
                    os.system("ssh -i {} ec2-user@{} sudo docker run -dit --name {} {}".format(key, ip, os_name, image))
                    dock()

                elif (("Run" in data) and ("python" in data)) or ("docker" in data):
                    python_docker = sp.getoutput("ssh -i {} ec2-user@{} sudo docker run hello-world".format(key, ip))
                    print(python_docker)
                    #y = input("enter image name..>>  ")
                    #z = input("Give OS name that  you want..>>   ")
                    #os.system("ssh {} docker run -it --name {}  {}".format(ip, z, y))
                    #os.system("yum install python3")
                    #os.system("python 3")
                    dock()

                elif ("quit" in data) or ("exit" in data):
                    exit()

                else:
                    print("Invalid option...")
                    break
                dock()
#Partition menu
def par():

        import speech_recognition as sr
        import os
        import pyttsx3 as py
    
        py.speak("Enter your remote IP Address")
        ip = input("Enter Your IP Address (eg. 1.2.3.4) : ")
        a4_banner = pyfiglet.figlet_format("\n\t Partition menu ")
        print(colored(a4_banner, 'red'))
        print("""\n
        \tPress 1.To Enter the static partition menu
        \tPress 2.To Enter the LVM partition menu
        \tPress 3.Exit
        """)

        r = sr.Recognizer()
        with sr.Microphone() as s:
            py.speak("Start saying what do you want to do.....")
            print("start saying ....")
            audio = r.listen(s)
            py.speak("i got it...")
            print("i got it ...")

        data = r.recognize_google(audio)
        print(data) 

        #part = int(input("\n\tEnter the option.. "))
        if (("static" in data) and ("partition" in data)):
            def option():
                    print('''
                      \n
                        \tPress 1 : To Create a Static Partition..
                        \tPress 2 : Format and mount partition..
                        \tPress 3 : To increase size of Partition..
                        \tPress 4 : To decrease size of partition..
                        \tPress 5 : To delete the static partiton..
                        \tpress 6 : exit..
                      \n
                    what can I help you..: ''')

                    py.speak("What do you want to do : ")
                    #op = input("Enter what you want to do : ")

                    r = sr.Recognizer()
                    with sr.Microphone() as s:
                            py.speak("Start saying.....")
                            print("start saying ....")
                            audio1 = r.listen(s)
                            py.speak("i got it...")
                            print("i got it ...")

                    data1 = r.recognize_google(audio1)
                    print(data1)

                    if ("create" in data1) or (("static" in data1) and ("partition" in data1)):
                        os.system("\n ssh -i {}  ec2-user@{} sudo yum install parted".format(key, ip))
                        py.speak("Enter your harddisk that you want")
                        name1 = input("\n\tEnter your harddisk that you want..>> ")
                        py.speak("Enter start point of partition")
                        part1 = input("\n\tEnter start point of partition..>> ")
                        py.speak("Enter end point of partition")
                        part2 = input("\n\tEnter end point of partition..>> ")
                        os.system("ssh -i {} ec2-user@{} sudo parted {} mkpart primary ext4 {}G {}G;".format(key, ip, name1, part1, part2))
                        os.system("ssh -i {} ec2-user@{} sudo lsblk".format(key, ip))
                        option()

                    elif (("format" in data1) and ("mount" in data1)) or ("partition" in data1):
                        py.speak("Enter the name of partition")
                        name3 = input("\n\t Enter the name of partition..>> ")
                        os.system("ssh -i {} ec2-user@{} sudo mkfs.ext4 {}".format(key, ip, name3))
                        py.speak("Enter the folder name that you want")
                        name4 = input("\n\t Enter the folder name that you want..>>")
                        os.system("ssh -i {} ec2-user@{} sudo mkdir /{}".format(key, ip, name4))
                        os.system("ssh -i {} ec2-user@{} sudo mount {} {}".format(key, ip, name3,name4))
                        os.system("ssh -i {} ec2-user@{} sudo lsblk".format(key, ip))

                    elif (("increase" in data1) and ("size" in data1)) or ("partition" in data1):
                        py.speak("Enter the name of harddisk")
                        name1 = input("\n\t Enter the name of harddisk..>> ")
                        py.speak("Enter the number of partition")
                        num1 = input("\n\t Enter the number of partition..>> ")
                        py.speak("Enter the increasing end point size")
                        size1 = input("\n\t Enter the increasing end point size..>> ")
                        os.system("ssh -i {} ec2-user@{} sudo parted {} resizepart {} {}G".format(key, ip, name1, num1, size1))
                        os.system("ssh -i {} ec2-user@{} sudo lsblk".format(key, ip))
                        option()

                    elif (("decrease" in data1) and ("size" in data1)) or ("partition" in data1):
                        py.speak("Enter the name of harddisk")
                        name1 = input("\n\t Enter the name of harddisk..>> ")
                        py.speak("Enter the number of partition")
                        num1 = input("\n\t Enter the number of partition..>> ")
                        py.speak("Enter the decreasing end point size")
                        size2 = input("\n\t Enter the decreasing end point size..>> ")
                        os.system("ssh -i {} ec2-user@{} sudo parted {} resizepart {} {}G".format(key, ip, name1, num1, size2))
                        os.system("ssh -i {} ec2-user@{} sudo lsblk".format(key, ip))
                        option()

                    elif (("delete" in data1) and ("partition" in data1)):
                        py.speak("Enter the name of harddisk")
                        name1 = input("\n\t Enter the name of harddisk..>> ")
                        py.speak("Enter the number of partition")
                        num1 = input("\n\t Enter the number of partition..>> ")
                        os.system("ssh -i {} ec2-user@{} sudo parted {} rm {}".format(key, ip, name1, num1))
                        os.system("ssh -i {} ec2-user@{} sudo lsblk".format(key, ip))
                        option()

                    elif (("exit" in data1) or ("quit" in data1)):
                        os.system("exit")
                        #os.system("tput setaf 3")
                        py.speak("Thank you See you soon....")
                        print("\n\n\t#########..THANK YOU..See you soon..#########")
                        #os.system("ssh -i {} ec2-user@{} sudo tput setaf 7".format(ip))
                        print("\n")

                    else:
                        py.speak("Incorrect choice please select correct option")
                        print("Incorrect Choice,select correct option..")
                        py.speak("Press Enter to go to main menu")
                        input("\n\t Press Enter to go main menu")
            option()
            par()
        elif (("logical" in data) and ("volume" in data) and ("partition" in data)):
            def printme():
                    print(''' 
                        \n
                    
                    \tPress 1 : To see Hard disk information..
                    \tPress 2 : To create a Physical Volume (PV)..
                    \tPress 3 : To create a Volume Group (VG)..
                    \tPress 4 : To create a Logical Volume (LV)..
                    \tPress 5 : To format the Logical Volume (LV)..
                    \tPress 6 : To create a Folder and Mount Logical Volume..
                    \tPress 7 : To increase the LVM partition..
                    \tPress 8 : To decrease the LVM partition..
                    \tPress 9 : Exit..
                        \n
                        What can I help you : ''')
                    print("\t\n.........................###...........................\n")

                    r = sr.Recognizer()
                    with sr.Microphone() as s:
                            py.speak("Start saying.....")
                            print("start saying ....")
                            audio2 = r.listen(s)
                            py.speak("i got it...")
                            print("i got it ...")

                    data2 = r.recognize_google(audio2)
                    print(data2)

                    if (("see" in data2) and ("info" in data2)) and (("harddisk" in data2) and ("information" in data2)):
                        os.system("\n ssh -i {} ec2-user@{} sudo fdisk -l".format(key, ip))
                        os.system("ssh -i {} ec2-user@{} sudo tput setaf 3".format(key, ip))
                        py.speak("Press Enter to go main menu")
                        input("\n\t Press Enter to go main menu...>>")
                        os.system("ssh -i {} ec2-user@{} sudo tput setaf 7".format(key, ip))
                        printme()

                    elif ("create" in data2) and ("physical" in data2) and ("volume" in data2) or ("PV" in data2):
                        os.system("\n ssh -i {} ec2-user@{} sudo fdisk -l".format(key, ip))
                        py.speak("Enter name of first harddisk that you want")
                        Disk1 = input("\n\n\tEnter name of 1 st harddisk that you want >> ")
                        os.system("ssh -i {} ec2-user@{} sudo pvcreate {}".format(key, ip, Disk1))
                        os.system("ssh -i {} ec2-user@{} sudo pvdisplay {}".format(key, ip, Disk1))
                        py.speak("Enter name of second harddisk that you want")
                        Disk2 = input("\n\t Enter name of 2 nd harddisk that you want >> ")
                        os.system("ssh -i {} ec2-user@{} sudo pvcreate {}".format(key, ip, Disk2))
                        os.system("ssh -i {} ec2-user@{} sudo pvdisplay {}".format(key, ip, Disk2))
                        os.system("ssh -i {} ec2-user@{} sudo tput setaf 3".format(key, ip))
                        py.speak("Your two physical volume created successfully")
                        print("\n\n\t>>>>>>>>>Your two physical volume(PV) created successfully<<<<<<<<<<")
                        py.speak("Press Enter to go main menu")
                        input("\n\t Press Enter to go main menu...>>")
                        os.system("ssh -i {} ec2-user@{} sudo tput setaf 7".format(key, ip))
                        printme()

                    elif ("create" in data2) and ("volume" in data2) and ("group" in data2) or ("VG" in data2):
                        os.system("\n ssh -i {} ec2-user@{} sudo fdisk -l".format(key, ip))
                        py.speak("Enter name of first harddisk that you want")
                        Disk1 = input("\n\n\tEnter name of 1 st harddisk that you want >> ")
                        py.speak("Enter name of second harddisk that you want")
                        Disk2 = input("\n\tEnter name of 2 nd harddisk that you want >> ")
                        py.speak("Give name to your Volume Group")
                        name1 = input("\n\tGive name to your Volume Group(VG) >> ")
                        os.system("ssh -i {} ec2-user@{} sudo pvdisplay {}".format(key, ip, Disk1))
                        os.system("ssh -i {} ec2-user@{} sudo pvdisplay {}".format(key, ip, Disk2))
                        os.system("ssh -i {} ec2-user@{} sudo vgcreate {} {} {}".format(key, ip, name1, Disk1, Disk2))
                        os.system("ssh -i {} ec2-user@{} sudo vgdisplay {}".format(key, ip, name1))
                        os.system("ssh -i {} ec2-user@{} sudo tput setaf 3".format(key, ip))
                        py.speak("Your Volume Group created successfully")
                        print("\n\n\t>>>>>>>>>>Your Volume Group(VG) {} created successfully<<<<<<<<< ".format(key, ip, name1))
                        py.speak("Press Enter to go main menu")
                        input("\n\t Press Enter to go main menu...>>")
                       # os.system("ssh -i {} ec2-user@{} sudo tput setaf 7".format(ip))
                        printme()

                    elif ("create" in data2) and ("logical" in data2) and ("volume" in data2) or ("LV" in data2):
                        os.system("\n ssh -i {} ec2-user@{} sudo fdisk -l".format(key, ip))
                        # Disk1= input("\n\n\t Enter name of 1 st harddisk that you want >> ")
                        # Disk2= input("\n\t Enter name of 2 nd harddisk that you want >> ")
                        py.speak("Enter size for your Logical Volume")
                        size1 = input("\n\t Enter size for your Logical Volume >> ")
                        py.speak("Enter your Volume Group name")
                        name1 = input("\n\t Enter your Volume Group(VG) name >> ")
                        py.speak("Give name to your Logical Volume")
                        name2 = input("\n\t Give name to your Logical Volume(LV) >> ")
                        # os.system("pvcreate {}".format(Disk1))
                        # os.system("pvcreate {}".format(Disk2))
                        # os.system("vgcreate {} {} {}".format (name1,Disk1,Disk2))
                        os.system("ssh -i {} ec2-user@{} sudo vgdisplay {}".format(key, ip, name1))
                        os.system("ssh -i {} ec2-user@{} sudo lvcreate --size {}G --name {} {} ".format(key, ip, size1, name2, name1))
                        os.system("ssh -i {} ec2-user@{} sudo lvdisplay {}/{}".format(key, ip, name1, name2))
                        os.system("ssh -i {} ec2-user@{} sudo tput setaf 3")
                        py.speak("Your Logical Volume created successfully")
                        print("\n\n\t>>>>>>>>>Your Logical Volume(LV) {} created successfully<<<<<<<<<".format(key, ip, name2))
                        py.speak("Press Enter to go main menu")
                        input("\n\t Press Enter to go main menu...>>")
                        os.system("ssh -i {} ec2-user@{} sudo tput setaf 7".format(key, ip))
                        printme()

                    elif ("format" in data2) and ("logical" in data2) and ("volume" in data2):
                        py.speak("Enter the name of Volume Group")
                        name2 = input("\n\n\tEnter the name of Volume Group >> ")
                        py.speak("Enter the name of Logical Volume")
                        name3 = input("\n\n\tEnter the name of Logical Volume >> ")
                        os.system("ssh -i {} ec2-user@{} sudo mkfs.ext4 /dev/{}/{}".format(key, ip, name2, name3))
                        os.system("ssh -i {} ec2-user@{} sudo tput setaf 3".format(key, ip))
                        py.speak("Your Logical Volume Formated")
                        print("\n\n\t>>>>>>>>>Your Logical Volume Formated<<<<<<<<")
                        py.speak("Press Enter to go main menu")
                        input("\n\t Press Enter to go main menu...>>")
                        os.system("ssh -i {} ec2-user@{} sudo tput setaf 7".format(key, ip))
                        printme()

                    elif ("create" in data2) and ("folder" in data2) and ("mount" in data2) and ("LV" in data2):
                        py.speak("Enter folder name that you want")
                        folder1 = input("\n\n\t Enter folder name that you want >> ")
                        os.system("ssh -i {} ec2-user@{} sudo mkdir {}".format(key, ip, folder1))
                        py.speak("Enter the name of Volume Group")
                        name2 = input("\n\tEnter the name of Volume Group >> ")
                        py.speak("Enter the name of Logical Volume")
                        name3 = input("\n\tEnter the name of Logical Volume >> ")
                        os.system("ssh -i {} ec2-user@{} sudo mount /dev/{}/{} {}".format(key, ip, name2, name3, folder1))
                        os.system("ssh -i {} ec2-user@{} sudo df -hT".format(ip))
                       # os.system("ssh -i {} ec2-user@{} sudo tput setaf 3".format(ip))
                        py.speak("Your Logical Volume mounted")
                        print("\n\n\t>>>>>>>>Your Logical Volume mounted<<<<<<<<")
                        py.speak("Press Enter to go main menu")
                        input("\n\t Press Enter to go main menu...>> ")
                        #os.system("ssh -i {} ec2-user@{} sudo tput setaf 7".format(ip))
                        printme()

                    elif ("increase" in data2) and ("logical" in data2) and ("volume" in data2) and  ("size" in data2):
                        py.speak("Enter the name of VG Partition")
                        pr1 =  input("\n\n\tEnter the name of VG Partition..: ")
                        py.speak("Enter the name of LV Partition")
                        pr2 = input("\n\n\tEnter the name of LV Partition..:")
                        py.speak("Enter the increase size")
                        pr3 = input("\n\n\tEnter the increase size..: ")
                        os.system("ssh -i {} ec2-user@{} sudo lvextend --size +{}G /dev/{}/{}".format(key, ip, pr3,pr1,pr2))
                        os.system("ssh -i {} ec2-user@{} sudo resize2fs /dev/{}/{}".format(key, ip, pr1,pr2))
                        py.speak("Press Enter to go main menu")
                        input("\n\t Press Enter to go main menu...>> ")
                        printme()

                    elif (("decrease" in data2) and ("LVM" in data2)) or ("size" in data2):
                        py.speak("Enter the name of VG Partition")
                        pr1 = input("\n\n\tEnter the name of VG Partition..: ")
                        py.speak("Enter the name of LV Partition")
                        pr2 = input("\n\n\tEnter the name of LV Partition..:")
                        py.speak("Enter the decrease size")
                        pr3 = input("\n\n\tEnter the decrease size..: ")
                        os.system("ssh -i {} ec2-user@{} sudo lvreduce -r -L {}G /dev/{}/{}".format(key, ip, pr3, pr1, pr2))
                        py.speak("Press Enter to go main menu")
                        input("\n\t Press Enter to go main menu...>> ")
                        printme()

                    elif (("exit" in data2) or ("quit" in data2)):
                        os.system("exit")
                        #os.system("ssh -i {} ec2-user@{} sudo tput setaf 3".format(ip))
                        py.speak("Thank you see you soon")
                        print("\n\n\t#########..THANK YOU..See you soon..#########")
                        #os.system("ssh -i {} ec2-user@{} sudo tput setaf 7".format(ip))
                        print("\n")

                    else:
                        py.speak("Incorrect choice please select correct option")
                        print("Incorrect Choice,select correct option..")
                        py.speak("Press Enter to go to main menu")
                        input("\n\t Press Enter to go main menu")
                        printme()
            printme()
            par()

        elif ("exit" in data) or ("quit" in data):
                os.system("exit")

        par()
        #task()

#Hadoop menu
def hadoop_all():
    import os
    import subprocess as sp
    import speech_recognition as sr
    import pyttsx3 as pt
    
    def startd():
            a = sp.getstatusoutput("ssh -i {} ec2-user@{} sudo hadoop-daemon.sh start datanode".format(key, St_ip))
            print(a)
            #if a[0]!=0:
             #   pt.speak("We have got an error")
              #  print("We have got an error")
            #else:
             #   sp.getoutput("ssh -i {} ec2-user@{} sudo jps".format(St_ip))
    def stopd():
            a = sp.getstatusoutput("ssh -i {} ec2-user@{} sudo hadoop-daemon.sh stop datanode".format(key, St_ip))
            print(a)
            #if a[0]!=0:
             #   pt.speak("We have got an error")
             #   print("We have got an error")
            #else:
             #   print("datnode stoped")
    
    def startn():
            a = sp.getstatusoutput("ssh -i {} ec2-user@{} sudo  hadoop-daemon.sh start namenode".format(key, St_ip))
            if a[0]!=0:
                pt.speak("We have got an error")
                print("We have got an error")
            else:
                sp.getoutput("ssh -i {} ec2-user@{} sudo jps".format(key, St_ip))
    def stopn():
            a = sp.getstatusoutput("ssh -i {} ec2-user@{} sudo hadoop-daemon.sh stop namenode".format(key, St_ip))
            if a[0]!=0:
                pt.speak("We have got an error")
                print("We have got an error")
            else:
                sp.getoutput("ssh -i {} ec2-user@{} sudo jps ".format(key, St_ip))
    
    pt.speak("Can you enter your remote IP")
    St_ip = input("Enter your remote IP: ")
    
    while True:
        pt.speak("Welcome to hadoop menu")
        a5_banner = pyfiglet.figlet_format("\n\t Let's  hadoop menu ")
        print(colored(a5_banner, 'yellow'))
        print("""
        \n
                        Welcome to hadoop menu
                        ----------------------

                Press 1 to get into master menu
                Press 2 to get into slave menu
                Press 3 to get into client menu
                Press 4 Exit..
        """)
        opt = int(input("Enter the option :"))
        if opt == 1 :
            a6_banner = pyfiglet.figlet_format("\n\t hadoop Master menu ")
            print(colored(a6_banner, 'green'))
            pt.speak("Welcome to hadoop Master menu")
            print("""
                            \tTo configure the master
                            \tTo start the master
                            \tTo stop master
                            \tTo check the cluster report 
                            \tExit    
                            """)
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Can you tell your choice")
                pt.speak("Can you tell your choice")
                audio = r.listen(source)
                print("Got it...")
                pt.speak("Got it.")
            spi = r.recognize_google(audio)
            spi = spi.lower()    

            #if ("Configure" in spi) or ("configure") and ("data node " in spi):
                #def cmaster():
                    #pt.speak("Enter the details")
                    #pt.speak("Enter the directory name for master storage")
                    #direc = input("\n\tEnter the directory name for master:")
                    #sp.getoutput("ssh -i {} ec2-user@{} sudo rm -rf /{}".format(key, St_ip,direc))
                    #sp.getoutput("ssh -i {} ec2-user@{} sudo mkdir /{}".format(key, St_ip, direc))
                    #pt.speak("Provide the master IP")
                    #ipp = input("\n\tEnter the Master ip:")
                    #cc = '''<?xml version="1.0"?>    
            #<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
                    
            #<!-- Put site-specific property overrides in this file. -->
                    
            #<configuration>
            #<property>
            #<name>fs.default.name</name>
            #<value>hdfs://{}:9001</value>
            #</property>
            #</configuration>'''.format(ipp)
                    #text_file = open("/etc/hadoop/core-site.xml", 'w')
                    #n = text_file.write(cc)
                    #text_file.close()
                    #dd ="""<?xml version="1.0"?>
            #<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
                    
            #<!-- Put site-specific property overrides in this file. -->
                    
            #<configuration>s
            #<property>
            #<name>dfs.name.dir</name>
            #<value>/{}</value>
            #</property>
            #</configuration>
                        #""".format(direc)
                    #hdf_file = open("/etc/hadoop/hdfs-site.xml", 'w')
                    #m = hdf_file.write(dd)
                    #hdf_file.close()
                    #sp.getoutput("ssh -i {} ec2-user@{} sudo hadoop namenode -format -Y".format(key, St_ip))
                    #pt.speak("Successfully configured the name node")
                    #print("Successfully configured the name node")
                #cmaster()
            elif("start" in spi)and("master" in spi):
                startn()
            elif("stop" in spi)and("master" in spi):
                stopn()
            elif("Cluster" in spi)and("report" in spi):
                sp.getoutput("ssh -i {} ec2-user@{} sudo hadoop dfsadmin --report".format(key, St_ip))
            elif("exit" in spi):
                print("Do you want to exit? yes or no")
                exitt = input("Enter you want to exit or not ")
                if exitt == "yes":
                    break
                else:
                    hadoop_all()
        elif opt == 2:
            a7_banner = pyfiglet.figlet_format("\n\t Let's hadoop slave menu ")
            print(colored(a7_banner, 'red'))
            pt.speak("Welcome to hadoop slave menu")
            print("""
            \tTo configure the data node
            \tTo start the slave
            \tTo stop slave
            \tTo check report 
            \tExit 
        """)
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Can you tell your choice")
                pt.speak("Can you tell your choice")
                audio = r.listen(source)
                print("Got it...")
                pt.speak("Got it.")
            spi = r.recognize_google(audio)
            spi = spi.lower() 
            print(spi)
            #if ("cofigure" in spi)or ("configure") and("data" in spi) and ("node" in spi):
                #def cslave():
                    #pt.speak("Enter the details")
                    #pt.speak("Enter the directory name for slave storage")
                    #direc = input("\n\tEnter the directory name for slave:")
                    #sp.getoutput("ssh -i {} ec2-user@{} sudo rm -rf /{}".format(key, St_ip,direc))
                    #sp.getoutput("ssh -i {} ec2-user@{} sudo mkdir /{}".format(key, St_ip, direc))
                    #pt.speak("Provide the master IP")
                    #ipp = input("\n\tEnter the Master ip:")

                    #cc = '''<?xml version="1.0"?>
            #<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
        
            #<!-- Put site-specific property overrides in this file. -->
        
            #<configuration>
            #<property>
            #<name>fs.default.name</name>
            #<value>hdfs://{}:9001</value>
            #</property>
            #</configuration>'''.format(ipp)
                    text_file = open("/etc/hadoop/core-site.xml", 'w')
                    n = text_file.write(cc)
                    text_file.close()
                    dd = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
        
<!-- Put site-specific property overrides in this file. -->
        
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{}</value>
</property>
</configuration>
            """.format(direc)
                    #hdf_file = open("/etc/hadoop/hdfs-site.xml", 'w')
                    #m = hdf_file.write(dd)
                    #hdf_file.close()
                    #pt.speak("Successfully configured the data node")
                    #print("Successfully configured the data node")
                #cslave()
                
            elif ("start" in spi) or ("Start" in spi)and("slave" in spi) or ("Slave" in spi ):
                startd()
            elif ("stop" in spi) and ("slave" in spi):
                stopd()
            elif ("Cluster" in spi)or ("cluster" in spi )and("report" in spi):
                a = sp.getstatusoutput("ssh -i {} ec2-user@{} sudo hadoop dfsadmin --report".format(key, St_ip))
                print(a)
            elif ("exit" in spi):
                print("Do you want to exit? yes or no")
                exitt = input("Enter you want to exit or not ")
                if exitt == "yes":
                        break
                else:
                    hadoop_all()
        elif opt == 3:
            def client():
                pt.speak("Welcome to hadoop client menu")
                print("""
                 \tTo configure the client
                 \tTo upload a file
                 \tTo remove a file
                 \tTo read a file
                 \tTo list the files
                 \tTo upload a file with  block size
                 \tExit..")
                """)
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Can you tell your choice")
                    pt.speak("Can you tell your choice")
                    audio = r.listen(source)
                    print("Got it...")
                    pt.speak("Got it.")
                spi = r.recognize_google(audio)
                spi = spi.lower()
                if ("Configure" in spi)and("client" in spi):
                    def cclient():
                        pt.speak("Input the master IP")
                        mip = input("\n\tEnter the master ip")
                        cc = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
        
<!-- Put site-specific property overrides in this file. -->
        
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>'''.format(mip)
                        text_file = open("/etc/hadoop/core-site.xml", 'w')
                        n = text_file.write(cc)
                        text_file.close()
                        pt.speak("Successfully configured the Client")
                        print("Successfully configured the Client")
                elif ("upload" in spi)and("a" in spi)and("file" in spi):
                    pt.speak("Enter the file path")
                    filep = input("\n\tEnter the full file path")
                    sp.getoutput("ssh -i {} ec2-user@{} sudo hadoop fs -put {} /".format(key, St_ip,filep))
                    print("File Uploded successfully")
                elif ("remove" in spi)and("a" in spi)and("file" in spi):
                    pt.speak("Enter the file path")
                    filep = input("\n\tEnter the full file path")
                    sp.getoutput("ssh -i {} ec2-user@{} sudo hadoop fs -rm {} /".format(key, St_ip, filep))
                    print("File Uploded successfully")
                elif ("read" in spi)and("a" in spi)and("file" in spi):
                    pt.speak("Enter the file path")
                    filep = input("\n\tEnter the full file path")
                    sp.getoutput("ssh -i {} ec2-user@{} sudo hadoop fs -cat {} /".format(key, St_ip, filep))
                    print("File Uploded successfully")
                elif ("list" in spi)and("the" in spi)and("files" in spi):
                    you = sp.getstatusoutput("ssh -i {} ec2-user@{} sudo hadoop fs ls /".format(key, St_ip))
                    print(you)
                elif ("upload" in spi)and("a" in spi)and("file" in spi)and("default" in spi):
                    pt.speak("Enter the block size")
                    bs = int(input("Enter the Block size"))
                    pt.speak("Enter the file path")
                    filep = input("Enter the full file path")
                    sp.getoutput("ssh -i {} ec2-user@{} sudo hadoop fs -Ddfs.block.size={}M -put {} /".format(key, st_ip,bs,filep))
                    pt.speak("File upload successfull with default size")
                elif("exit" in spi):
                    print("Do you want to exit? yes or no")
                    exitt = input("Enter you want to exit or not ")
                    if exitt == "yes":
                        print("hello")
                    else:
                        hadoop_all()        
        hadoop_all()            



def aws():
    import os
    import getpass
    import subprocess as sp
    import speech_recognition as sr
    import pyttsx3 as pt

    #1pt.speak("Enter your remote IP Address ?")
    #ip = input("Enter Your IP Address (eg. 1.2.3.4) : ")
    
    def final():
        a8_banner = pyfiglet.figlet_format("\n\t AWS Menu ")
        print(colored(a8_banner, 'blue'))
        pt.speak("Welcome in AWS Menu")
        print("""
        \n
            >>>>>>>>>>>>> Welcome In A AWS Menu >>>>>>>>>>>>>

                Press 1 To launch the EC-2 menu
                Press 2 To launch the S3 menu
                Press 3 To launch the IAM menu
                Press 4 To launch the CLOUDFRONT 
                Press 5 To configure the AWS CLI
                Press 6 Exit
                """)
    
        # pt.speak("""Press 1 To launch the EC-2 menu
             #   Press 2 To launch the S3 menu
            #    Press 3 To launch the IAM menu
           #     Press 4 To launch the CLOUDFRONT 
          #      Press 5 To configure the AWS CLI
         #       Press 6 Exit
        #        """)
        
        pt.speak("enter the option")
        menu = int(input("Enter the option : "))
        if menu == 1:
            def ec2():
                a9_banner = pyfiglet.figlet_format("\n\t Let's EC-2 Menu ")
                print(colored(a9_banner, 'green'))
                print(""">>>>>>>> Welcome in a EC-2 Menu <<<<<<<<
                    \n
                    Launch the instances menu 
                    Launch the volume menu 
                    Launch the Security group menu 
                    Launch the Key pair menu 
                    Launch the snapshot menu
                    Exit
                    """)
                #pt.speak("""Welcome in a Ec-2 menu
                 #   Launch the instances menu 
                  #  Launch the volume menu 
                  #  Launch the Security group menu 
                 #   Launch the Key pair menu 
                 #   Launch the snapshot menu
                  #  Exit
                   # """)

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Can you tell your choice")
                    pt.speak("Can you tell your choice")
                    audio = r.listen(source)
                    print("Got it...")
                    pt.speak("Got it.")
                ola = r.recognize_google(audio)
                ola = ola.lower()
                print(ola)

                if ("instance" in ola) and ("menu" in ola) or ("instant" in ola):
                    def ins():
                        a10_banner = pyfiglet.figlet_format("\n\t Let's start Instances menu ")
                        print(colored(a10_banner, 'red'))
                        print(">>>>>>> Welcome in a Instances menu <<<<<< \n 1.To describe instances \n 2.To Describe the instances type \n 3.To Run a new instance \n 4.To start a instance \n 5.To stop the instance \n 6.To reboot a instance \n 7.To terminate a instance \n 8.To Exit ")
                        pt.speak("""Welcome in a instance menu
                            Describe instances 
                            Describe the instances type
                            Run a new instance                     
                            start a instance 
                            stop the instance  
                            reboot a instance 
                            terminate a instance 
                            Exit 
                            """)

                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Can you tell your choice")
                            pt.speak("Can you tell your choice")
                            audio = r.listen(source)
                            print("Got it...")
                            pt.speak("Got it.")
                        im = r.recognize_google(audio)
                        im = im.lower()

                        if ("describe" in im) and ("instance" in im):
                            os.system("aws ec2 describe-instances")
                            ins()
                        elif ("describe" in im) and ("instance" in im) and ("type" in im):
                            os.system("aws ec2 describe-instances-types")
                            ins()
                        elif ("new" in im) and ("instance" in im):
                            pt.speak("enter the image id")
                            imageid = input("Enter the image id : ")
                            pt.speak("enter the instance type")
                            inty = input("Enter the instance type :")
                            #pt.speak("enter the subnet id")
                            #subnetid = input("enter the subnet id :")
                            pt.speak("enter the security group id")
                            security = input("enter the security group id :")
                            pt.speak("enter the key name")
                            keyname = input("enter the key name :")
                            pt.speak("Got it please wait")
                            print("Got it please wait..")
                            os.system("aws ec2 run-instance --image-id {} --instance-type {} --count 1  --key-name {}".format(imageid,inty,security,keyname,)) 
                            ins()                   
                        elif ("start" in im) and ("instance" in im):
                            pt.speak("enter the instance id")
                            instanceid = input("Enter the instance id : ")
                            print("got it..")
                            pt.speak("got it")
                            os.system("aws ec2 start-instances --instance-ids {}".format(instanceid))
                            ins()
                        elif ("stop" in im) and ("instance" in im):
                            pt.speak("enter the instance id")
                            instanceid = input("Enter the instance id : ")
                            print("got it..")
                            pt.speak("got it")
                            os.system("aws ec2 stop-instances --instance-ids {}".format(instanceid))
                            ins()
                        elif ("reboot" in im) and ("instance" in im):
                            pt.speak("enter the instance id")
                            instanceid = input("Enter the instance id : ")
                            print("got it..")
                            os.system("aws ec2 reboot-instances --instance-ids {}".format(instanceid))
                            ins()
                        elif ("terminate" in im) and ("instance" in im):
                            pt.speak("enter the instance id")
                            instanceid = input("Enter the instance id")
                            print("got it")
                            os.system("aws ec2 terminate-instances --instance-ids {}".format(instanceid))
                            ins()
                        elif ("exit" in im):
                            pt.speak("thank you")
                            print("Thank you")
                            os.system("exit")
                        else:
                            pt.speak("choose the correct option")
                            print("Choose the correct option")
                    ins()
                    ec2()
                elif ("volume" in ola) and ("menu" in ola):
                    def volume():
                        a11_banner = pyfiglet.figlet_format("\n\t Let's start Volume menu ")
                        print(colored(a11_banner, 'blue'))
                        print(">>>>>>>> Welcome in a Volume Menu <<<<<<<< \n 1.Create Volume\n 2.Delete Volume\n 3.Modify Volume\n 4.Attach Volume\n 5.Detach Volume\n 6.Exit ")
                        pt.speak("""Welcome in a Volume menu
                            Create Volume  
                            Delete Volume 
                            Modify Volume 
                            Attach Volume  
                            Detach Volume 
                            Exit
                            """)
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Can you tell your choice")
                            pt.speak("Can you tell your choice")
                            audio = r.listen(source)
                            print("Got it...")
                            pt.speak("Got it.")
                        pr = r.recognize_google(audio)
                        pr = pr.lower()
                        
                        if ("create" in pr) and ("volume" in pr):
                            pt.speak("enter the volume type")                        
                            vtype = input("Enter the Volume type")
                            pt.speak("enter the size of volume")
                            size = input("Enter the size of volume ")
                            pt.speak("enter the availability zone")
                            az = input("Enter the availability zone")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(vtype,size,az))
                            volume()
                        elif ("delete" in pr) and ("volume" in pr):
                            pt.speak("enter the volume id")
                            vid = input("Enter the Volume ID")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 delete-volume {}".format(vid))
                            volume()
                        elif ("Modify" in pr) and ("volume" in pr):
                            pt.speak("enter the volume id")
                            vid =input("Enter the volume ID : ")
                            pt.speak("enter the size you want to change")
                            size =int(input("Enter the size you want to change : "))
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 modify-volume {} --size {}".format(vid,size))
                            volume()
                        elif ("Attach" in pr) and ("volume" in pr):
                            pt.speak("enter the device")
                            device = input("Enter the device e.g /dev/shd : ")
                            pt.speak("enter the instance id : ")
                            iid = input("Enter the instance id")
                            pt.speak("enter the volume id")
                            vid = input("Enter the Volume id : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {}".format(device,iid,vid))
                            volume()
                        elif ("Detach" in pr) and ("volume" in pr):
                            pt.speak("enter the device")
                            device = input("Enter the device e.g /dev/shd : ")
                            pt.speak("enter the instance id")
                            iid = input("Enter the instance id : ")
                            pt.speak("enter the volume id")
                            vid = input("Enter the Volume id : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 detach-volume --device {} --instance-id {} --volume-id {}".format(device,iid,vid))
                            volume()
                        elif ("Exit" in pr):
                            pt.speak("thank you")
                            print("Thank you")
                            os.system("exit")
                        else:
                            pt.speak("give the correct option")
                            print("Give the correct option")
                    volume()
                    ec2()
                elif ("launch" in ola) and ("security" in ola) and ("group" in ola):
                    def sec():
                        a12_banner = pyfiglet.figlet_format("\n\t Let's start Security Group Menu  ")
                        print(colored(a12_banner, 'green'))
                        print(">>>>>>> Welcome in Security Group Menu <<<<<<<<\n 1.Describe security group\n 2.Create a security group\n 3.Delete a security group\n 4.Exit ")
                        pt.speak("""Welcome in security group menu
                            Describe security group
                            Create a security group
                            Delete a security group
                            Exit
                            """)

                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Can you tell your choice")
                            pt.speak("Can you tell your choice")
                            audio = r.listen(source)
                            print("Got it...")
                            pt.speak("Got it.")
                        se = r.recognize_google(audio)
                        se = se.lower()    
                            
                        if ("Describe" in se) and ("security" in se) and ("group" in se):
                            pt.speak("enter the group names")
                            gn = input("Enter the groups names")
                            pt.speak("got it")
                            print("got it") 
                            os.system("aws ec2 describe-security-groups --group-names {}".format(   gn))
                            sec()
                        elif ("create" in se) and ("security" in se) and ("group" in se):
                            pt.speak("enter the group name")
                            pt.speak("enter the description")
                            gn = input("Enter the group name : ")
                            des = input("Enter the description : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 create-security-group --group-name {} --description' {}' ".format(gn,des))
                            sec()
                        elif ("delete" in se) and ("security" in se) and ("group" in se):
                            pt.speak("enter the group name")
                            gn = input("Enter the group name")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 delete-security-group --group-name {}".format(gn))
                            sec()
                        elif ("exit" in se):
                            pt.speak("thank you")
                            print("Thank you")
                            os.system("exit")
                        else:
                            pt.speak("give the correct option")
                            print("give the correct option")
                    sec()
                    ec2()    
                elif ("launch" in ola) and ("key" in ola) and ("pair" in ola):
                    def key():
                        a13_banner = pyfiglet.figlet_format("\n\t Let's Key Pair Menu   ")
                        print(colored(a13_banner, 'red'))
                        print(">>>>>>>> Welcome in Key Pair Menu <<<<<<<<\n 1.Describe key pairs\n 2.Create a new key pair\n 3.Delete a key pair\n 4.Exit")
                        pt.speak("""Welcome in a key pair menu
                            Describe key pairs
                            Create a new key pair 
                            Delete a key pair 
                            Exit"
                            """)
                        
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Can you tell your choice")
                            pt.speak("Can you tell your choice")
                            audio = r.listen(source)
                            print("Got it...")
                            pt.speak("Got it.")
                        key = r.recognize_google(audio)
                        key = key.lower()    
                            
                        if ("Describe" in key) and ("key" in key) and ("pair" in key):
                            pt.speak("enter the key pair name")
                            kn = input("Enter the key pair name : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 descibe-key-pairs --key-name {}".format(kn))
                            key()
                        elif ("create" in key) and ("key" in key) and ("pair" in key):
                            pt.speak("enter the key name")
                            kn = input("Enter the key name : ")
                            pt.speak("enter the query")
                            qe =input("Enter the query : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 create-key-pairs --key-name {} --query '{}' --output text > {}.pem".format(kn,qe,kn))  
                            key()                          
                        elif ("Delete" in key) and ("key" in key) and ("pair" in key):
                            pt.speak("enter the key pair name")
                            kn = input("Enter the key pair name : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 delete-key-pairs --key-name {}".format(kn))
                            key()
                        elif ("exit" in key):
                            pt.speak("thank you")
                            print("thank you")
                            os.system("exit")
                        else:
                            pt.speak("give correct choice")
                            print("give correct choice")
                    key()
                    ec2()
                elif ("launch" in ola) and ("snapshot" in ola):
                    def snap():
                        a14_banner = pyfiglet.figlet_format("\n\t Let's start Snapshot menu   ")
                        print(colored(a14_banner, 'yellow'))
                        print(">>>>>>> Welcome in Snapshot menu >>>>>>>\n 1.Describe snapshots\n 2.Create snapshots\n 3.Delete snapshots\n 4.Exit")
                        pt.speak("""Welcome in Snapshot menu
                            1.Describe snapshots
                            2.Create snapshots 
                            3.Delete snapshots 
                            4.Exit
                            """)
                        
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Can you tell your choice")
                            pt.speak("Can you tell your choice")
                            audio = r.listen(source)
                            print("Got it...")
                            pt.speak("Got it.")
                        sn = r.recognize_google(audio)
                        sn = sn.lower() 

                        if ("Describe" in sn) and ("snapshot" in sn):
                            pt.speak("enter your snapshot id")
                            sid = input("Enter yours snapshot id : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 describe-snapshots --snapshot-ids {}".format(sid))
                            snap()
                        elif ("create" in sn) and ("snapshot" in sn):
                            pt.speak("enter the volume id")
                            vid =input("Enter the volume id : ")
                            pt.speak("enter the description for snapshot")
                            des = input("Enter the description for snapshot : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 create-snapshot --volume-id {} --description '{}'".format(vid,des))
                            snap()
                        elif ("Delete" in sn) and ("snapshot" in sn):
                            pt.speak("enter your snapshot id")
                            sid = input("Enter yours snapshot ID : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws ec2 delete-snapshot --snapshot-id {}".format(sid))
                            snap()
                        elif ("exit" in sn):
                            pt.speak("thank you")
                            print("thank you")
                            os.system("exit")
                        else:
                            pt.speak("give the correct option")
                            print("give the correct option")
                    snap()
                    ec2()
                elif ("exit" in ola):
                    pt.speak("thank you")
                    print("thank you")
                    os.system("exit")

                else:
                    pt.speak("give correct option")
                    print("give the correct option")
            ec2()
            final()
        #S3 menu starts
        elif menu ==2:
            def option():
                a15_banner = pyfiglet.figlet_format("\n\t Let's start S3 menu   ")
                print(colored(a15_banner, 'green'))
                print(""" >>>>>>>> Welcome in a S3 Menu <<<<<<<<
                    \n
                    Create a S3 Bucket..
                    List S3 Bucket..
                    Create Bucket policies..
                    Delete the Bucket..
                    Delete Bucket Policies..
                    Exit..
                    \n
                    """)
                pt.speak("""Welcome in a S3 menu
                    Create a S3 Bucket
                    List S3 Bucket
                    Create Bucket policies
                    Delete the Bucket
                    Delete Bucket Policies
                    exit
                    """)
                
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Can you tell your choice")
                    pt.speak("Can you tell your choice")
                    audio = r.listen(source)
                    print("Got it...")
                    pt.speak("Got it.")
                op = r.recognize_google(audio)
                op = op.lower()

                if ("create" in op) or ( "Create" in op) and ("Bucket" in op) or ("bucket" in op):
                    pt.speak("enter your bucket name")
                    name1 = input("\n\tEnter your Bucket name : ")
                    pt.speak("enter your aws region")
                    name2 = input("\n\tEnter your AWS Region : ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(name1, name2, name2))
                    option()
                elif ("List" in op) and ("S3" in op) and ("Bucket" in op):
                    pt.speak("got it")
                    print("got it")
                    os.system('aws s3api list-buckets --query "Bucket[].Name"')
                    option()
                elif ("Create" in op) and ("Bucket" in op) and ("Policies" in op):
                    def pub():
                        print("\n 1.Create Bucket Public\n 2.Make Image Public 3.Exit")
                        pt.speak("""Create bucket public
                            Make image public
                            Exit
                            """)

                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Can you tell your choice")
                            pt.speak("Can you tell your choice")
                            audio = r.listen(source)
                            print("Got it...")
                            pt.speak("Got it.")
                        pr = r.recognize_google(audio)
                        pr = pr.lower()

                        if ("create" in pr) and ("Bucket" in pr) and ("Public" in pr):
                            pt.speak("Enter the name of bucket")
                            name1 = input("\n Enter the name of Bucket : ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws s3api put-bucket-ac1 --public-read --bucket {}".format(name1))
                            pub()
                        elif ("make" in pr) and ("Image" in pr) and ("public" in pr):
                            pt.speak("enter your image name")
                            name2 = input("\n Enter your image name :  ")
                            pt.speak("got it")
                            print("got it")
                            os.system("aws s3api put-object-ac1 --bucket {} --key {}.jpg --grant-read uri=http://acs.amazonaws.com/groups/global/AllUsers".format(name1, name2))
                            pub()
                        elif ("Exit" in pr):
                            pt.speak("thank you")
                            print("Thank you")
                            os.system("exit")
                        else:
                            pt.speak("give correct input")
                            print("Give correct option")
                    pub()    
                    option()
                elif ("Delete" in op) and ("Bucket" in op):
                    pt.speak("enter the name of bucket")
                    name1 = input("\n Enter the name of bucket : ")
                    pt.speak("enter the region name")
                    name2 = input("\n Enter the Region name : ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws s3api delete-bucket --bucket {} --region {}".format(name1, name2))
                    option()
                elif ("Delete" in op) and ("Bucket" in op) and ("Policies" in op):
                    pt.speak("enter the name of bucket")
                    name1 = input("\n Enter the name of Bucket : ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws s3api delete-bucket-policy --bucket {}".format(name1))
                    option()
                elif ("exit" in op):
                    pt.speak("thank you")
                    print("Thank you")
                    os.system("exit")
                else:
                    pt.speak("select correct option")
                    print("select correct option..")
            option()
            final()
            
        elif menu ==3:
            def select():
                a16_banner = pyfiglet.figlet_format("\n\t Let's start IAM menu   ")
                print(colored(a16_banner, 'red'))
                print(""">>>>>>>> Welcome in IAM Menu
                    \n
                    Create a IAM Group..
                    Create a IAM User..
                    Add IAM User in IAM Group..
                    Attach IAM managed policy to IAM User..
                    Set Password to IAM User..
                    Create Access and Public Key..
                    Exit..
                    """)
                pt.speak("""Welcome in IAM Menu
                    Create a IAM Group
                    Create a IAM User
                    Add IAM User in IAM Group
                    Attach IAM managed policy to IAM User
                    Set Password to IAM User
                    Create Access and Public Key
                    Exit..
                    """)

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Can you tell your choice")
                    pt.speak("Can you tell your choice")
                    audio = r.listen(source)
                    print("Got it...")
                    pt.speak("Got it.")
                ia = r.recognize_google(audio)
                ia = ia.lower()
                print(ia)

                if ("Create" in ia) or ("create" in ia) and ("Group" in ia) or ("group" in ia):
                    pt.speak("Enter Group name")
                    name1 = input("\n Enter Group name that you want : ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws iam create-group --group-name {}".format(name1))
                    select()
                elif ("create" in ia) or ("Create" in ia)  and ("user" in ia)or ("User " in ia):
                    pt.speak("Enter user name")
                    name2 = input("\n Enter User name that you want : ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws iam create-user --user-name {}".format(name2))
                    select()                    
                elif ("add" in ia) or ("Add" in ia) and ("user" in ia) or ("User" in ia) and ("in" in ia) or ("In" in ia) and ("group" in ia) or ("Group" in ia):
                    pt.speak("enter the IAM user name")
                    name2 = input("\n Enter the name of IAM User : ")
                    pt.speak("enter the IAM group name")
                    name1 = input("\n Enter the name of IAM Group : ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws iam add-user-to-group --user-name {} --group-name {}".format(name2, name1))
                    os.system("aws iam get-group --group-name {}".format(name1))
                    select()
                elif ("Attach" in ia) and ("IAM" in ia) and ("Policy" in ia) and ("User" in ia):
                    pt.speak("enter the IAM user name")
                    name2 = input("\n Enter the name of IAM User : ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws iam attach-user-policy --user-name {} --policy=arn:aws:iam::aws:policy/PowerUserAccess")
                    os.system("aws iam list-attached-user-policies --user-name {}".format(name2))
                    select()
                elif ("Password" in ia) and ("IAM" in ia) and ("User" in ia):
                    pt.speak("enter IAM user name")
                    name2 = input("\n Enter the name of IAM User : ")
                    pt.speak("enter your password")
                    name3 = input("\n Enter the Password that you want to give : ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws iam create-login-profile --user-name {} --password {} --password-reset-required".format(name2, name3))
                    select()
                elif ("Access" in ia) and ("Public" in ia) and ("Key" in ia):
                    pt.speak("enter the IAM user name")
                    name2 = input("\n Enter the name of IAM User : ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws iam create-access-key --user-name {}".format(name2))
                    select()
                elif ("Exit" in ia):
                    pt.speak("thank you")
                    print("Thank you")
                    os.system("exit")
                else:
                    pt.speak("give correct option")
                    print("Give correct option..")
            select()
            final()
        elif menu == 4:
            def cloud():
                import subprocess as sp
                
                a17_banner = pyfiglet.figlet_format("\n\t Let's start Cloud Front Menu   ")
                print(colored(a17_banner, 'green'))
                print(""">>>>>>>> Welcome in Cloud Front Menu <<<<<<<<<
                    Create distribution  
                    Delete distribution
                    List the distribution
                    Exit 
                    """)
                pt.speak("""Welcome in Cloud Front Menu 
                    create distribution  
                    delete distribution
                    list the distribution
                    exit
                    """)
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Can you tell your choice")
                    pt.speak("Can you tell your choice")
                    audio = r.listen(source)
                    print("Got it...")
                    pt.speak("Got it.")
                opt = r.recognize_google(audio)
                opt = opt.lower()
            
                if ("Create" in opt) and ("distribution" in opt):
                    pt.speak("enter the origin domain name")
                    odn = input("\n Enter the origin domain name : ")
                    pt.speak("\n enter the default root object")
                    dro = input("\n Enter the default root object : ")
                    pt.speak("got it")
                    pt.speck("got it")
                    os.system("aws cloudfront create-distribution --origin-domain-name {} --default-root-object {}".format(odn,dro))
                    cloud()
                elif ("Delete" in opt) and ("distribution" in opt):
                    pt.speak("enter the distribution id")
                    cid = input("Enter the distribution id : ")
                    pt.speak("enter the distribution etag : ")
                    etag = input("Enter the distribution etag ")
                    pt.speak("got it")
                    print("got it")
                    os.system("aws cloudfront delete-distribution --id {cid} --if-match {}".format(cid,etag))
                    cloud()
                elif ("list" in opt) or ("List" in opt) and ("distribution" in opt):
                    pt.speak("got it")
                    print("got it")
                    a = sp.getoutput("aws cloudfront list-distributions")
                    print(a)
                    cloud()
                elif ("Exit" in opt):
                    print("Thank you")
                    pt.speak("thank you")
                    os.system("exit")
                else:
                    pt.speak("give correct option")
                    print("Give correct option")
            cloud()
            final()
        elif menu == 5:
            print("got it")
            pt.speak("got it")
            os.system('\ncurl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip"')
            os.system(" unzip awscliv2.zip ")
            os.system(" sudo ./aws/install ")
            os.system("\n sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin")
            os.system("\n aws --version")
            os.system("\n aws configure")
            final()
        elif menu == 6:
            print("Thank you")
            pt.speak("thank you")
            os.system("exit")

        else:
            pt.speak("Select the Correct Option")
            print("Select the correct option")
    final()
task()
