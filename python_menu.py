
import os
os.system("tput setaf 2")
print("""\t\t\t\t\t\t\t                

                                          
                             @@             @@   @@@@@@@@@   @@          @@@@@@@@@    @@@@@@@@@@   @@@          @@@   @@@@@@@@@
                             @@             @@   @@          @@          @@           @@      @@   @@ @@      @@ @@   @@
                             @@             @@   @@          @@          @@           @@      @@   @@   @@  @@   @@   @@
                             @@             @@   @@          @@          @@           @@      @@   @@     @@     @@   @@
                             @@             @@   @@@@@@@@@   @@          @@           @@      @@   @@            @@   @@@@@@@@@
                             @@      @@     @@   @@          @@          @@           @@      @@   @@            @@   @@
                             @@   @@   @@   @@   @@          @@          @@           @@      @@   @@            @@   @@
                             @@ @@       @@ @@   @@          @@          @@           @@      @@   @@            @@   @@
                             @@@           @@@   @@@@@@@@@   @@@@@@@@@   @@@@@@@@@    @@@@@@@@@@   @@            @@   @@@@@@@@@ 

                        


    """)










print("\n\n")
os.system("tput setaf 2")
system=input("Where you want to run the Commands (Local/Remote): ").lower()
if system=="local":
    print("This is Local Execution Environment!!")
elif system=="remote":
    ip=input("Enter the Remote System IP:")
    print("This is Remote Execution Environment!!")
else:
    print("Invalid Choice!!")
    exit()
while True:
    os.system("tput setaf 5")
    if system=="local":
        print(""" \t\t
                =================================================
                |   1  |   For YUM CONFIGURATION....            |
                =================================================
                |   2  |   For WEBSERVER CONFIGURATION....      |
                =================================================
                |   3  |   For LVM PARTITION....                |
                =================================================
                |   4  |   For DOCKER CONFIGURATION....         |  
                ================================================= 
                |   5  |   For HADOOP CONFIGURATION....         |
                =================================================
                |   6  |   For AWS CONFIGURATION....            | 
                =================================================
                |   7  |   For LINUX BASICS....                 |
                =================================================
                |   8  |   For Closing the Program....          |
                =================================================
""")

        Ch=input("Enter Your Choice: ")
        os.system("tput setaf 2")
        if int(Ch)==1:
             os.system("tput setaf 6")
             print(""" \t\t
                                          =============================================================
                                          |                  YUM CONFIGURATION:-                      |
                                          |                                                           |
                                          =============================================================
                                          |   1   |     For configuring the YUM inside the OS....     |
                                          =============================================================
                                          |   2   |     For viewing the YUM is configured or not....  |
                                          =============================================================
                   """) 
             
             Ch=input("Enter Your Choice: ")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 Dir=input("Enter the Directory Name where you want to mount the DVD or ISO file: ")
                 os.system("mkdir {} ; mount /dev/cdrom {} ; cd {}; ls ; yum install wget -y".format(Dir,Dir,Dir))
                 os.system("rm -rf dvd.repo")
                 os.system("wget https://raw.githubusercontent.com/Megha-Varshney/yum_configuartion/main/dvd.repo ; cp dvd.repo /etc/yum.repos.d/dvd.repo")
             elif int(Ch)==2:
                 os.system("yum repolist")

        elif int(Ch)==2:
             os.system("tput setaf 6")
             print(""" \t\t
                                           ==================================================================
                                           |                 WEBSERVER CONFIGURATION:-                      |
                                           |                                                                |
                                           ==================================================================
                                           |   1   |    For installing the Httpd Software....               |
                                           ==================================================================
                                           |   2   |    For removing the Httpd Software....                 |
                                           ==================================================================
                                           |   3   |    For viewing Httpd Software is installed or not....  |
                                           ==================================================================
                                           |   4   |    For creating a Page....                             |
                                           ==================================================================
                                           |   5   |    For passing an existing webpage....                 | 
                                           ==================================================================
                                           |   6   |    For starting the Httpd Service....                  |
                                           ==================================================================
                                           |   7   |    For viewing the status of the Httpd Service....     |
                                           ==================================================================
                                           |   8   |    For stopping the Httpd Service....                  |
                                           ==================================================================
                                           |   9   |    For restarting the Httpd Service....                |
                                           ==================================================================
                       """)

             Ch=input("Enter Your Choice: ")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 os.system("yum install httpd -y")
             elif int(Ch)==2:
                 os.system("yum remove httpd -y")
             elif int(Ch)==3:
                 os.system("rpm -q httpd")
             elif int(Ch)==4:
                 page=input("Enter the Page Name: ")
                 os.system("vim /var/www/html/{}.html".format(page))
             elif int(Ch)==5:
                 page=input("Enter the Page Path: ")
                 pname=input("Just enter the page name from the above path you provided: ")
                 os.system("cp {}  /var/www/html/{}.html".format(page,pname))
             elif int(Ch)==6:
                 os.system("systemctl start httpd")
             elif int(Ch)==7:
                 os.system("systemctl status httpd")
             elif int(Ch)==8:
                 os.system("systemctl stop httpd")
             elif int(Ch)==9:
                 os.system("systemctl restart httpd")

        elif int(Ch)==3:
             os.system("tput setaf 6")
             print(""" \t\t
                                        ====================================================================================
                                        |                             LVM PARTITION:-                                      |
                                        |                                                                                  |
                                        ====================================================================================                                           
                                        |   1   |    For viewing the Existing Hard Disk....                                |                                           
                                        ====================================================================================                                         
                                        |   2   |    For viewing the Existing Physical Volumes....                         |
                                        ====================================================================================
                                        |   3   |    For viewing the Existing Virtual Groups....                           |  
                                        ====================================================================================
                                        |   4   |    For viewing the Existing Logical Volumes....                          |
                                        ====================================================================================
                                        |   5   |    For viewing all the Mounted Partitions with their Mount Points....    |
                                        ====================================================================================
                                        |   6   |    For creating the Physical Volume....                                  |
                                        ====================================================================================
                                        |   7   |    For creating the Volume Group....                                     |
                                        ====================================================================================
                                        |   8   |    For creating the Logical Volume....                                   |
                                        ====================================================================================
                                        |   9   |    For creating a Directory....                                          |
                                        ====================================================================================
                                        |   10  |    For formatting the Logical Volume....                                 |
                                        ====================================================================================
                                        |   11  |    For mounting the Logical Volume....                                   |
                                        ====================================================================================
                                        |   12  |    For extending the Logical Volume Size....                             |  
                                        ====================================================================================
                                        |   13  |    For reducing the Logical Volume Size....                              |
                                        ====================================================================================
                                        |   14  |    For starting the NameNode after increasing the Storage on the fly.... |
                                        ====================================================================================
                                        |   15  |    For starting the DataNode after increasing the Storage on the fly.... |
                                        ====================================================================================
                                        |   16  |    For viewing the report of connected DataNodes to the NameNode....     |
                                        ====================================================================================
                                                                                                                                                                                              """)    
             Ch=input("Enter Your Choice: ")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 os.system("fdisk -l")
             elif int(Ch)==2:
                 os.system("pvdisplay")
             elif int(Ch)==3:
                 vg=input("Enter the Volume Group Name: ")
                 os.system("vgdisplay {}".format(vg))
             elif int(Ch)==4:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 os.system("lvdisplay {}/{}".format(vg,lv))
             elif int(Ch)==5:
                 os.system("df -h")
             elif int(Ch)==6:
                 pv=input("Enter the Physical Volume Name: ")
                 os.system("pvcreate {}".format(pv))
             elif int(Ch)==7:
                 vg=input("Enter the Volume Group Name: ")
                 b=int(input("Enter the Number of Physical Volumes you want to add to Virtual Group: "))
                 d1=input("Enter the Physical Volume0 Name: ")
                 d=input("Enter the Physical Volume1 Name: ")
                 os.system("vgcreate {} {} {} ".format(vg,d1,d))
             elif int(Ch)==8:
                 vg=input("Enter the Volume Group Name from which you want to create a Logical Volume: ")
                 lv=input("Enter the Logical Volume Name: ")
                 size=input("Enter the size of Logical Volume: ")
                 os.system("lvcreate --size {} --name {} {}".format(size,lv,vg))
             elif int(Ch)==9:
                 dir=input("Enter the Directory Name: ")
                 os.system("mkdir {}".format(dir))
             elif int(Ch)==10:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 os.system("mkfs.ext4 /dev/{}/{}".format(vg,lv))
             elif int(Ch)==11:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 l=input("Enter the Mount Point Name: ")
                 os.system("mount /dev/{}/{} {}".format(vg,lv,l))
             elif int(Ch)==12:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 o=input("Enter the size for extending the Logical Volume: ")
                 os.system("lvextend --size +{} /dev/{}/{}".format(o,vg,lv))
                 os.system("resize2fs /dev/{}/{}".format(vg,lv))
             elif int(Ch)==13:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 r=input("Enter the size you want for your Logical Volume: ")
                 s=input("Enter the Mount Point Name to which you mount the Logical Volume: ")
                 os.system("umount {}".format(s))
                 os.system("e2fsck -f /dev/{}/{}".format(vg,lv))
                 os.system("resize2fs /dev/{}/{} {}".format(vg,lv,r))
                 os.system("lvreduce --size {} /dev/{}/{} -y ".format(r,vg,lv))
                 os.system("mount /dev/{}/{} {}".format(vg,lv,s))
             elif int(Ch)==14:
                 ip=input("Enter the NameNode IP: ")
                 os.system("hadoop-daemon.sh start namenode")
                 os.system("jps")
             elif int(Ch)==15:
                 os.system("hadoop-daemon.sh start datanode")
                 os.system("jps")
             elif int(Ch)==16:
                 os.system("hadoop dfsadmin -report")
        
        elif int(Ch)==4:
             os.system("tput setaf 6")
             print("""\t\t            
                                        =========================================================================================                    
                                        |                             DOCKER CONFIGURATION:-                                    |
                                        |                                                                                       |
                                        =========================================================================================
                                        |   1  |     For installing Docker....                                                  |
                                        =========================================================================================
                                        |   2  |     For viewing the Running Docker Containers....                              |
                                        =========================================================================================
                                        |   3  |     For viewing the Existing Docker Images....                                 |
                                        =========================================================================================
                                        |   4  |     For downloading Docker Image from DockerHub....                            |
                                        =========================================================================================
                                        |   5  |     For launching the Docker Container from the Docker Image....               |
                                        =========================================================================================
                                        |   6  |     For going inside the Launched Docker Container....                         |
                                        =========================================================================================
                                        |   7  |     For stopping the Running Docker Container....                              |
                                        =========================================================================================
                                        |   8  |     For starting the Docker Container....                                      |
                                        =========================================================================================
                                        |   9  |     For removing the Docker Image....                                          |
                                        =========================================================================================
                                        |   10 |     For removing the Docker Container....                                      |
                                        =========================================================================================
                                        |   11 |     For viewing all the Existing Docker Containers either Running or Stopped...|
                                        =========================================================================================
                                        |   12 |     For viewing the Docker logs....                                            |
                                        =========================================================================================
                                        |   13 |     For starting the Docker Services....                                       |
                                        =========================================================================================
                                        |   14 |     For stopping the Docker Services....                                       |
                                        =========================================================================================
                                        |   15 |     For viewing the Docker Service Status....                                  |
                                        =========================================================================================
      
             """)
             Ch=input("Enter Your Choice: ")
             os.system("tput setaf 2")                        
             if int(Ch)==1:
                 os.system("echo -e '\n[dock]\nbaseurl=https://download.docker.com/linux/centos7/x86_64/stable/\ngpgcheck=0' >> /etc/yum.repos.d/docker.repo")
                 os.system("yum repolist")
                 os.system("yum install docker  --nobest -y")
                 print("Docker installed successfully")
             elif int(Ch)==2:
                 os.system("docker ps")
             elif int(Ch)==3:
                 os.system("docker images")
             elif int (Ch)==4:
                 c_name=input("Please enter the image id:")
                 os.system("docker pull {}".format(c_name))
             elif int(Ch)==5:
                 c_name=input("Please specify the Container Name:")
                 i_name=input("Please specify the Image Name: ")
                 os.system(" docker run -it --name {} {}".format(c_name))
             elif int(Ch)==6:
                 c_name=input("Please specify the Container Name or Container ID: ")
                 os.system("docker attach {}".format(c_name))
             elif int (Ch)==7:
                 c_name=input("Please specify the Container Name or Container ID")
                 os.system("docker stop {}".format(c_name))
             elif int (Ch)==8:
                 c_name=input("Please specify the Container Name or Container ID")
                 os.system("docker start {}".format(c_name))
             elif int (Ch)==9:
                 c_image=input("please specify the image id")
                 os.system("docker rmi {}".format(c_image))
             elif int (Ch)==10:
                 c_name=input("Please specify the name of the Container")
                 os.system("docker rm {}".format(c_name))
             elif int (Ch)==11:
                 os.system("docker ps -a")
             elif int(Ch)==12:
                 c_name=input("Please specify the name of the Container")
                 os.system("docker logs {}".format(c_name))
             elif int(Ch)==13:
                 os.system("systemctl start docker")
             elif int(Ch)==14:
                 os.system("systemctl stop docker")
             elif int(Ch)==15:
                 os.system("systemctl status docker")
      
        elif int(Ch)==5:
             os.system("tput setaf 6")
             print("""\t\t
                                                   
                                        ========================================================================================        
                                        |                              HADOOP CONFIGURATION:-                                  |
                                        |                                                                                      |
                                        ========================================================================================
                                        |   1  |     For configuring the Hadoop Name Node....                                  |
                                        ========================================================================================
                                        |   2  |     For configuring the Hadoop Data Node....                                  |
                                        ========================================================================================
                                        |   3  |     For configuring the Hadoop Client....                                     |
                                        ========================================================================================
                                        |   4  |     For viewing the report of connected DataNodes to the NameNode....         |
                                        ========================================================================================
                                        |   5  |     For stopping the Name Node or Data Node....                               |
                                        ========================================================================================
                                        |   6  |     For starting the Name Node or Data Node....                               |
                                        ========================================================================================
                                        |   7  |     For viewing the Name Node or Data Node Services are running or not....    |
                                        ========================================================================================
                                        |   8  |     For creating a File and then uploading the File from the Hadoop Client....|
                                        ========================================================================================
                                        |   9  |     For uploading the Existing File from the Hadoop Client....                |
                                        ========================================================================================
                                        |   10 |     For viewing all the Files uploaded by the Hadoop Client....               |
                                        ========================================================================================
                                        |   11 |     For reading the File uploaded by the Hadoop Client....                    |
                                        ========================================================================================
                                        |   12  |     For removing the File uploaded by the Hadoop Client....                  |
                                        ========================================================================================
                                                                
             """)
             Ch=input("Enter Your Choice: ")
             os.system("tput setaf 2")  
             if int(Ch)==1:
                 os.system("echo -e '\n[java]\nbaseurl=https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html#license-lightbox\ngpgcheck=0' >> /etc/yum.repos.d/java.repo")
                 os.system("echo -e '\n[hadoop]\nhttps://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm\ngpgcheck=0' >> /etc/yum.repos.d/hadoop.repo")
                 os.system("yum repolist")
                 os.system("yum install java -y")
                 os.system("yum install hadoop -y")
                 folder_name=input("Enter the folder Name you want to use in the cluster: ")
                 #hdfs-site.xml file configuration
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                 os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<property>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<name>dfs.name.dir</name>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<value>/%s</value>" >> /etc/hadoop/hdfs-site.xml' %foldername)
                 os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "</property>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/hdfs-site.xml')
                 #core-site.xml file configuration
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
                 os.system('echo "  " >> /etc/hadoop/core-site.xml')
                 os.system('echo "<!Put site-specific property overrides in this file.>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<name>fs.default.name</name>" >> /etc/hadoop/core-site.xml')
                 ipadd=input("enter the public ip address of the namenode and port no. in like IPaddress:portNumber :_____")
                 os.system('echo "<value>hdfs://%s</value>" >> /etc/hadoop/core-site.xml' %ipadd)
                 os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')
                 os.mkdir(foldername)
                 os.system('hadoop namenode -format')
                 os.system('hadoop-daemon.sh start namenode')
                 os.system('jps')
             elif int(Ch)==2:
                 foldername=input("Enter the folder Name you want to use in the cluster: ")
                 #hdfs-site.xml file configuration
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                 os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo " " >> /etc/hadoop/hdfs-site.xml')      
                 os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<property>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<name>dfs.data.dir</name>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<value>/%s</value>" >> /etc/hadoop/hdfs-site.xml' %foldername)
                 os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "</property>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/hdfs-site.xml')
                 #core-site.xml file configuration
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
                 os.system('echo "  " >> /etc/hadoop/core-site.xml')
                 os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<name>fs.default.name</name>" >> /etc/hadoop/core-site.xml')
                 ipadd=input("enter the public ip address of the namenode and port no. in like IPaddress:portNumber :_____")
                 os.system('echo "<value>hdfs://%s</value>" >> /etc/hadoop/core-site.xml' %ipadd)
                 os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')
                 os.mkdir(foldername)
                 os.system('hadoop-daemon.sh start datanode')
                 os.system('jps')
             elif int(Ch)==3:
                 os.system("echo -e '\n[java]\nbaseurl=https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html#license-lightbox\ngpgcheck=0' >> /etc/yum.repos.d/java.repo")
                 os.system("echo -e '\n[hadoop]\nhttps://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm\ngpgcheck=0' >> /etc/yum.repos.d/hadoop.repo")
                 os.system("yum repolist")
                 os.system("yum install java -y")
                 os.system("yum install hadoop -y")
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?> >> /etc/hadoop/core-site.xml")
                 os.system('echo "  " >> /etc/hadoop/core-site.xml')
                 os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<name>fs.default.name</name>" >> /etc/hadoop/core-site.xml')
                 ipadd=input("enter the public ip address of the Namenode and port no. in like IPaddress:portNumber :_____")
                 os.system('echo "<value>hdfs://%s</value>" >> /etc/hadoop/core-site.xml' %ipadd)
                 os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')
             elif int(Ch)==4:
                 os.system("hadoop dfsadmin -report")
             elif int(Ch)==5:
                 Node=input("Enter the Name of the Node which you want to Stop(namenode/datanode): ")
                 os.system("hadoop-daemon.sh stop {}".format(Node))
             elif int(Ch)==6:
                 Node=input("Enter the Name of the Node which you want to Start(namenode/datanode): ")
                 os.system("hadoop-daemon.sh start {}".format(Node))   
             elif int(Ch)==7:
                 os.system("jps")   
             elif int(Ch)==8:
                 page=input("Enter the Name for the File you want to Create:")
                 os.system("vi {}".format(page))
                 os.system("hadoop fs -put {} /".format(page))
             elif int(Ch)==9:
                 page=input("Enter the Existing File Name:")
                 os.system("hadoop fs -put {} /".format(page))
             elif int(Ch)==10:
                 os.system("hadoop fs -ls / ")    
             elif int(Ch)==11:
                 page=input("Enter the File Name you want to Read:")
                 os.system("hadoop fs -cat /{}".format(page))
             elif int(Ch)==12:
                 page=input("Enter the File Name you want to Delete:")
                 os.system("hadoop fs -rm /{}".format(page)) 
       

        elif int(Ch)==6:
             os.system("tput setaf 6")
             print("""\t\t 
                                     ============================================================================================
                                     |                                     AWS CONFIGURATION:-                                  |
                                     |                                                                                          | 
                                     ============================================================================================
                                     |   1  |      For setting up the AWS CLI....                                               |
                                     ============================================================================================
                                     |   2  |      For logging to the AWS Account by giving Credentials....                     |
                                     ============================================================================================
                                     |   3  |      For creating a Key-Pair on the AWS....                                       |
                                     ============================================================================================
                                     |   4  |      For creating a Security-Group on the AWS....                                 |
                                     ============================================================================================
                                     |   5  |      For adding Inbound Rules to the Security-Group....                           |
                                     ============================================================================================
                                     |   6  |      For removing the Inbound Rules from the Security-Group.....                  |
                                     ============================================================================================
                                     |   7  |      For launching an EC2 Instance on the top of AWS....                          |
                                     ============================================================================================
                                     |   8  |      For creating an EBS Volume on the AWS....                                    |
                                     ============================================================================================
                                     |   9  |      For attaching an EBS Volume to the EC2 Instance....                          |
                                     ============================================================================================
                                     |   10 |      For creating a S3 Bucket on AWS....                                          |
                                     ============================================================================================
                                     |   11 |      For uploading the Content to the S3 Bucket....                               |
                                     ============================================================================================
                                     |   12 |      For giving Public Access to the S3 Bucket and the Uploaded Content....       |
                                     ============================================================================================
                                     |   13 |      For creating a Cloud Front Distribution on the AWS....                       |
                                     ============================================================================================
                                     |   14 |      For viewing all the Existing Key-Pairs on the AWS....                        |
                                     ============================================================================================  
                                     |   15 |      For viewing all the Existing Security-Groups....                             |
                                     ============================================================================================
                                     |   16 |      For viewing all the Existing EC2 Instances....                               |
                                     ============================================================================================
                                     |   17 |      For viewing all the Existing EBS Volumes....                                 |
                                     ============================================================================================
                                     |   18 |      For viewing all the Existing S3 Buckets....                                  |
                                     ============================================================================================
                                     |   19 |      For viewing all the Existing CLoud Front Distribution....                    |
                                     ============================================================================================
                                     |   20 |      For deleting the Key-Pair from the AWS....                                   |
                                     ============================================================================================
                                     |   21 |      For deleting the Security-Group from the AWS....                             |
                                     ============================================================================================
                                     |   22 |      For deleting the EC2 Instances from the AWS....                              |
                                     ============================================================================================
                                     |   23 |      For deleting the EBS Volumes from the AWS....                                |
                                     ============================================================================================
                                     |   24 |      For deleting the S3 Bucket from the AWS....                                  |
                                     ============================================================================================
                                     |   25 |      For deleting the Cloud Front Distribution....                                |
                                     ============================================================================================
                                     |   26 |      For detaching the EBS Volume from the EC2 Instance....                       |
                                     ============================================================================================
                                     |   27 |      For stopping the EC2 Instance....                                            |
                                     ============================================================================================
                                     |   28 |      For starting the EC2 Instance....                                            |
                                     ============================================================================================
        """)
             Ch=input("Enter Your Choice:")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 os.system("yum install python2 -y") 
                 os.system("pip2 install awscli")
                 os.system("pip2 install awscli --upgrade") 
                 os.system("aws --version")
             elif int(Ch)==2:
                 os.system("aws configure")
             elif int(Ch)==3:
                 key=input("Enter the Name for the Key-Pair you want to Create: ")
                 os.system("aws ec2 create-key-pair --key-name {}".format(key))
             elif int(Ch)==4:
                 sg=input("Enter the Name for the Security Group you want to Create: ")
                 os.system("aws ec2 create-security-group --group-name {} --description {}".format(sg,sg))
             elif int(Ch)==5:
                 sgi=input("Enter the Security Group ID to which you want to Add the Rules: ")
                 protocol=input("Enter the Protocol Name:")
                 port=input("Enter the Port No:")
                 cidr=input("Enter the CIDR:")
                 os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(sgi,protocol,port,cidr))
             elif int(Ch)==6:
                 sgname=input("Enter the Security Group Name from which you want to Delete the Rules:")
                 protocol=input("Enter the Protocol Name:")
                 port=input("Enter the Port No:")
                 cidr=input("Enter the CIDR:")
                 os.system("aws ec2 revoke-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}".format(sgname,protocol,port,cidr))
             elif int(Ch)==7:
                 ami=input("Enter the AMI ID for launching EC2 Instance:")
                 count=int(input("How many Instances you want to Launch:"))
                 itype=input("Enter the Instance Type for launching the Instance:")
                 key=input("Enter the Key-Pair you want to use for launching the Instance:")
                 sg=input("Enter the Security-Group ID you want to use for launching the Instance:")
                 subnet=input("Enter the Subnet ID to which you want to launch the Instance:")
                 os.system("aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {}".format(ami,count,itype,key,sg,subnet))
             elif int(Ch)==8:
                 vtype=input("Enter the Volume Type")
                 size=int(input("Enter the Size for the EBS Volume:"))
                 az=input("Enter the Availability Zone:")
                 os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(vtype,size,az))
             elif int(Ch)==9:
                 vid=input("Enter that EBS Volume ID which you want to attach to the EC2 Instance:")
                 iid=input("Enter the Instance ID to which you want to attach the EBS Volume:")
                 device=input("Enter the Device Name:")
                 os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(vid,iid,device))
             elif int(Ch)==10:
                 bname=input("Enter a Name for creating the S3 Bucket:")
                 az=input("Enter the Region in which you want to create the S3 Bucket:")
                 os.system("aws s3 mb s3://{} --region {}".format(bname,az))
             elif int(Ch)==11:
                 folder=input("Enter the Folder or Directory Name from which you want to upload the Content:")
                 content=input("Enter the Content Name you want to upload to the S3 Bucket:")
                 bname=input("Enter the Bucket Name to which you want to upload the Content:")
                 os.system("aws s3 cp {}:/{} s3://{}".format(folder,content,bname))
             elif int(Ch)==12:
                 content=input("Enter the Content Name you want to upload to the S3 Bucket:")
                 bname=input("Enter the Bucket Name to which you want to upload the Content:") 
                 os.system("aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(bname,content))
             elif int(Ch)==13:
                 content=input("Enter the Content Name you want to upload to the S3 Bucket:")
                 bname=input("Enter the Bucket Name to which you want to upload the Content:")
                 az=input("Enter the Region in which you want to create the S3 Bucket:")
                 os.system("aws cloudfront create-distribution --origin-domain-name  {}.s3.{}.amazonaws.com --default-root-object {}".format(bname,az,content))
             elif int(Ch)==14:
                 os.system("aws ec2 describe-key-pairs")
             elif int(Ch)==15:
                 os.system("aws ec2 describe-security-groups")
             elif int(Ch)==16:
                 os.system("aws ec2 describe-instances")
             elif int(Ch)==17:
                 os.system("aws ec2 describe-volumes")
             elif int(Ch)==18:
                 os.system("aws s3api list-buckets")
             elif int(Ch)==19:
                 os.system("aws cloudfront list-distributions")
             elif int(Ch)==20:
                 key=input("Enter the Key-Pair Name which you want to Delete:")
                 os.system("aws ec2 delete-key-pair --key-name {}".format(key))
             elif int(Ch)==21:
                 sg=input("Enter the Security-Group Name which you want to Delete:")
                 os.system("aws ec2 delete-security-group --group-name {}".format(sg))
             elif int(Ch)==22:
                 iid=input("Enter the Instance ID which you want to Terminate:")
                 os.system("aws ec2 terminate-instances --instance-ids {}".format(iid))
             elif int(Ch)==23:
                 vid=input("Enter the Volume ID which you want to Delete:")
                 os.system("aws ec2 delete-volume --volume-id {}".format(vid))
             elif int(Ch)==24:
                 bname=input("Enter the S3 Bucket Name which you want to Delete:")
                 az=input("Enter the Region from which you want to Delete the S3 Bucket:")
                 os.system("aws s3api delete-bucket --bucket {} --region {}".format(bname,az))
             elif int(Ch)==25:
                 cid=input("Enter the Cloud Front ID which you want to Delete:")
                 os.system("aws cloudfront delete-distribution --id {}".format(cid))
             elif int(Ch)==26:
                 vid=input("Enter the Volume ID which you want to Detach from the Instance:")
                 os.system("aws ec2 detach-volume --volume-id {}".format(iid))
             elif int(Ch)==27:
                 iid=input("Enter the Instance ID which you want to Stop:")
                 os.system("aws ec2 stop-instances --instance-ids {}".format(iid))
             elif int(Ch)==28:
                 iid=input("Enter the Instance ID which you want to Start:")
                 os.system("aws ec2 start-instances --instance-ids {}".format(iid))

        elif int(Ch)==7:
             os.system("tput setaf 6")
             print("""\t\t
                                      ===================================================================================
                                      |                             LINUX BASICS:-                                      |
                                      |                                                                                 | 
                                      ===================================================================================
                                      |   1  |      For pinging to a OS for particular No of Times....                  |
                                      ===================================================================================
                                      |   2  |      For creating more Users....                                         |
                                      ===================================================================================
                                      |   3  |      For checking the Software is present inside the OS or not....       |
                                      ===================================================================================
                                      |   4  |      For knowing more about the Command and its Syntax....               |
                                      ===================================================================================
                                      |   5  |      For viewing the IP Address of the OS....                            |
                                      ===================================================================================
                                      |   6  |      For viewing all the Usable Ports....                                |
                                      ===================================================================================
                                      |   7  |      For disabling the Firewall....                                      |
                                      ===================================================================================
                                      |   8  |      For enabling the Firewall....                                       |
                                      ===================================================================================
                                      |   9  |      For starting the Firewall....                                       |
                                      ===================================================================================
                                      |   10 |      For stopping the Firewall....                                       |
                                      ===================================================================================
                                      |   11 |      For viewing the Status of the Firewall....                          |
                                      ===================================================================================
                                      |   12 |      For running any of the Linux Commands....                           |
                                      ===================================================================================

                                              """)        
             Ch=input("Enter Your Choice:")                                      
             os.system("tput setaf 2")
             if int(Ch)==1:
                 ip1=input("Enter the OS IP for Pinging:")
                 n=input("Enter the No. of Times:")
                 os.system("ping -c {} {}".format(n,ip1))
             elif int(Ch)==2:
                 user=input("Enter the User Name:")
                 os.system("useradd {} ".format(user))
                 os.system("passwd {} ".format(user))
             elif int(Ch)==3:
                 software=input("Enter the Software Name:")
                 os.system("rpm -q {}".format(software))
             elif int(Ch)==4:
                 command=input("Enter the Command Name for knowing its Syntax:")
                 os.system("man {}".format(command))
             elif int(Ch)==5:
                 os.system("ifconfig")
             elif int(Ch)==6:
                 os.system("netstat -tnlp")
             elif int(Ch)==7:
                 os.system("systemctl disable firewalld")
             elif int(Ch)==8:
                 os.system("systemctl enable firewalld")
             elif int(Ch)==9:
                 os.system("systemctl start firewalld")
             elif int(Ch)==10:
                 os.system("systemctl stop firewalld")
             elif int(Ch)==11:
                 os.system("systemctl status firewalld")
             elif int(Ch)==12:
                 command=input("Enter the Command:")
                 os.system("{}".format(command))
       
        elif int(Ch)==8:
            os.system("tput setaf 2")
            print("\t\t\t\t\t\t\t\t\t THANK YOU!!")
            exit()




    elif system=="remote":
        print(""" \t\t
                =================================================
                |   1  |   For YUM CONFIGURATION....            |
                =================================================
                |   2  |   For WEBSERVER CONFIGURATION....      |
                =================================================
                |   3  |   For LVM PARTITION....                |
                =================================================
                |   4  |   For DOCKER CONFIGURATION....         |
                =================================================
                |   5  |   For HADOOP CONFIGURATION....         |
                =================================================
                |   6  |   For AWS CONFIGURATION....            |
                =================================================
                |   7  |   For LINUX BASICS....                 |
                =================================================
                |   8  |   For Closing the Program....          |
                =================================================
""")

        Ch=input("Enter Your Choice: ")
        os.system("tput setaf 2")
        if int(Ch)==1:
             os.system("tput setaf 6")
             print(""" \t\t
                                          =============================================================
                                          |                  YUM CONFIGURATION:-                      |
                                          |                                                           |
                                          =============================================================
                                          |   1   |     For configuring the YUM inside the OS....     |
                                          =============================================================
                                          |   2   |     For viewing the YUM is configured or not....  |
                                          =============================================================
                   """)
            
             Ch=input("Enter Your Choice: ")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 Dir=input("Enter the Directory Name where you want to mount the DVD or ISO file: ")
                 os.system("ssh {} mkdir {} ; mount /dev/cdrom {} ; cd {}; ls ; yum install wget -y".format(ip,Dir,Dir,Dir))
                 os.system("ssh {} rm -rf dvd.repo".format(ip))
                 os.system("ssh {} wget https://raw.githubusercontent.com/Megha-Varshney/yum_configuartion/main/dvd.repo ; cp dvd.repo /etc/yum.repos.d/dvd.repo".format(ip))
             elif int(Ch)==2:
                 os.system("ssh {} yum repolist".format(ip))

        elif int(Ch)==2:
             os.system("tput setaf 6")
             print(""" \t\t
                                           ==================================================================
                                           |                 WEBSERVER CONFIGURATION:-                      |
                                           |                                                                |
                                           ==================================================================
                                           |   1   |    For installing the Httpd Software....               |
                                           ==================================================================
                                           |   2   |    For removing the Httpd Software....                 |
                                           ==================================================================
                                           |   3   |    For viewing Httpd Software is installed or not....  |
                                           ==================================================================
                                           |   4   |    For creating a Page....                             |
                                           ==================================================================
                                           |   5   |    For passing an existing webpage....                 |
                                           ==================================================================
                                           |   6   |    For starting the Httpd Service....                  |
                                           ==================================================================
                                           |   7   |    For viewing the status of the Httpd Service....     |
                                           ==================================================================
                                           |   8   |    For stopping the Httpd Service....                  |
                                           ==================================================================
                                           |   9   |    For restarting the Httpd Service....                |
                                           ==================================================================
                       """)
             Ch=input("Enter Your Choice: ")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 os.system("ssh {} yum install httpd -y".format(ip))
             elif int(Ch)==2:
                 os.system("ssh {} yum remove httpd -y".format(ip))
             elif int(Ch)==3:
                 os.system("ssh {} rpm -q httpd".format(ip))
             elif int(Ch)==4:
                 page=input("Enter the Page Name: ")
                 os.system("ssh {} vim /var/www/html/{}.html".format(ip,page))
             elif int(Ch)==5:
                 page=input("Enter the Page Path: ")
                 pname=input("Just enter the page name from the above path you provided: ")
                 os.system("ssh {} cp {}  /var/www/html/{}.html".format(ip,page,pname))
             elif int(Ch)==6:
                 os.system("ssh {} systemctl start httpd".format(ip))
             elif int(Ch)==7:
                 os.system("ssh {} systemctl status httpd".format(ip))
             elif int(Ch)==8:
                 os.system("ssh {} systemctl stop httpd",format(ip))
             elif int(Ch)==9:
                 os.system("ssh {} systemctl restart httpd".format(ip))

        elif int(Ch)==3:
             os.system("tput setaf 6")
             print(""" \t\t
                                            
                                         ====================================================================================
                                         |                             LVM PARTITION:-                                      |
                                         |                                                                                  |
                                         ====================================================================================
                                         |   1   |    For viewing the Existing Hard Disk....                                |
                                         ====================================================================================
                                         |   2   |    For viewing the Existing Physical Volumes....                         |
                                         ====================================================================================
                                         |   3   |    For viewing the Existing Virtual Groups....                           |
                                         ====================================================================================                                                                                    |   4   |    For viewing the Existing Logical Volumes....                          |
                                         ====================================================================================                                                                                    |   5   |    For viewing all the Mounted Partitions with their Mount Points....    |
                                         ====================================================================================                                                                                    |   6   |    For creating the Physical Volume....                                  |
                                         ====================================================================================
                                         |   7   |    For creating the Volume Group....                                     |
                                         ====================================================================================
                                         |   8   |    For creating the Logical Volume....                                   |
                                         ====================================================================================
                                         |   9   |    For creating a Directory....                                          |
                                         ====================================================================================
                                         |   10  |    For formatting the Logical Volume....                                 |
                                         ====================================================================================
                                         |   11  |    For mounting the Logical Volume....                                   |
                                         ====================================================================================                                                                                    |   12  |    For extending the Logical Volume Size....                             |
                                         ====================================================================================
                                         |   13  |    For reducing the Logical Volume Size....                              |
                                         ====================================================================================
                                         |   14  |    For starting the NameNode after increasing the Storage on the fly.... |
                                         ====================================================================================
                                         |   15  |    For starting the DataNode after increasing the Storage on the fly.... |
                                         ====================================================================================
                                         |   16  |    For viewing the report of connected DataNodes to the NameNode....     |
                                         ====================================================================================
        
                   """)
             h=input("Enter Your Choice: ")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 os.system("ssh {} fdisk -l".format(ip))
             elif int(Ch)==2:
                 os.system("ssh {} pvdisplay".format(ip))
             elif int(Ch)==3:
                 vg=input("Enter the Volume Group Name: ")
                 os.system("ssh {} vgdisplay {}".format(ip,vg))
             elif int(Ch)==4:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 os.system("ssh {} lvdisplay {}/{}".format(ip,vg,lv))
             elif int(Ch)==5:
                 os.system("ssh {} df -h".format(ip))
             elif int(Ch)==6:
                 pv=input("Enter the Physical Volume Name: ")
                 os.system("ssh {} pvcreate {}".format(ip,pv))
             elif int(Ch)==7:
                 vg=input("Enter the Volume Group Name: ")
                 b=int(input("Enter the Number of Physical Volumes you want to add to Virtual Group: "))
                 d1=input("Enter the Physical Volume0 Name: ")
                 d=input("Enter the Physical Volume1 Name: ")
                 os.system("ssh {} vgcreate {} {} {} ".format(ip,vg,d1,d))
             elif int(Ch)==8:
                 vg=input("Enter the Volume Group Name from which you want to create a Logical Volume: ")
                 lv=input("Enter the Logical Volume Name: ")
                 size=input("Enter the size of Logical Volume: ")
                 os.system("ssh {} lvcreate --size {} --name {} {}".format(ip,size,lv,vg))
             elif int(Ch)==9:
                 dir=input("Enter the Directory Name: ")
                 os.system("ssh {} mkdir {}".format(ip,dir))
             elif int(Ch)==10:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 os.system("ssh {} mkfs.ext4 /dev/{}/{}".format(ip,vg,lv))
             elif int(Ch)==11:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 l=input("Enter the Mount Point Name: ")
                 os.system("ssh {} mount /dev/{}/{} {}".format(ip,vg,lv,l))
             elif int(Ch)==12:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 o=input("Enter the size for extending the Logical Volume: ")
                 os.system("ssh {} lvextend --size +{} /dev/{}/{}".format(ip,o,vg,lv))
                 os.system("ssh {} resize2fs /dev/{}/{}".format(ip,vg,lv))
             elif int(Ch)==13:
                 vg=input("Enter the Volume Group Name: ")
                 lv=input("Enter the Logical Volume Name: ")
                 r=input("Enter the size you want for your Logical Volume: ")
                 s=input("Enter the Mount Point Name to which you mount the Logical Volume: ")
                 os.system("ssh {} umount {}".format(ip,s))
                 os.system("ssh {} e2fsck -f /dev/{}/{}".format(ip,vg,lv))
                 os.system("ssh {} resize2fs /dev/{}/{} {}".format(ip,vg,lv,r))
                 os.system("ssh {} lvreduce --size {} /dev/{}/{} -y ".format(ip,r,vg,lv))
                 os.system("ssh {} mount /dev/{}/{} {}".format(ip,vg,lv,s))
             elif int(Ch)==14:
                 ip=input("Enter the NameNode IP: ")
                 os.system("hadoop-daemon.sh start namenode ; jps".format(ip))
             elif int(Ch)==15:
                 os.system("ssh {} hadoop-daemon.sh start datanode ; jps".format(ip))
             elif int(Ch)==16:
                 os.system("ssh {} hadoop dfsadmin -report".format(ip))

        elif int(Ch)==4:
             os.system("tput setaf 6")
             print("""\t\t
                                        =========================================================================================
                                        |                             DOCKER CONFIGURATION:-                                    |
                                        |                                                                                       |
                                        =========================================================================================
                                        |   1  |     For installing Docker....                                                  |
                                        =========================================================================================
                                        |   2  |     For viewing the Running Docker Containers....                              |
                                        =========================================================================================
                                        |   3  |     For viewing the Existing Docker Images....                                 |
                                        =========================================================================================
                                        |   4  |     For downloading Docker Image from DockerHub....                            |
                                        =========================================================================================
                                        |   5  |     For launching the Docker Container from the Docker Image....               |
                                        =========================================================================================
                                        |   6  |     For going inside the Launched Docker Container....                         |
                                        =========================================================================================
                                        |   7  |     For stopping the Running Docker Container....                              |
                                        =========================================================================================
                                        |   8  |     For starting the Docker Container....                                      |
                                        =========================================================================================
                                        |   9  |     For removing the Docker Image....                                          |
                                        =========================================================================================
                                        |   10 |     For removing the Docker Container....                                      |
                                        =========================================================================================
                                        |   11 |     For viewing all the Existing Docker Containers either Running or Stopped...|
                                        =========================================================================================
                                        |   12 |     For viewing the Docker logs....                                            |
                                        =========================================================================================
                                        |   13 |     For starting the Docker Services....                                       |
                                        =========================================================================================
                                        |   14 |     For stopping the Docker Services....                                       |
                                        =========================================================================================
                                        |   15 |     For viewing the Docker Service Status....                                  |
                                        =========================================================================================

             """)
             Ch=input("Enter Your Choice: ")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 os.system("ssh {} echo -e '\n[dock]\nbaseurl=https://download.docker.com/linux/centos7/x86_64/stable/\ngpgcheck=0' >> /etc/yum.repos.d/docker.repo ; yum repolist ; yum install docker  --nobest -y".format(ip))
                 print("Docker installed successfully")
             elif int(Ch)==2:
                 os.system("ssh {} docker ps".format(ip))
             elif int(Ch)==3:
                 os.system("ssh {} docker images".format(ip))
             elif int (Ch)==4:
                 c_name=input("Please enter the image id:")
                 os.system("ssh {} docker pull {}".format(ip,c_name))
             elif int(Ch)==5:
                 c_name=input("Please specify the Container Name:")
                 i_name=input("Please specify the Image Name: ")
                 os.system("ssh {} docker run -it --name {} {}".format(ip,c_name))
             elif int(Ch)==6:
                 c_name=input("Please specify the Container Name or Container ID: ")
                 os.system("ssh {} docker attach {}".format(ip,c_name))
             elif int (Ch)==7:
                 c_name=input("Please specify the Container Name or Container ID")
                 os.system("ssh {} docker stop {}".format(ip,c_name))
             elif int (Ch)==8:
                 c_name=input("Please specify the Container Name or Container ID")
                 os.system("ssh {} docker start {}".format(ip,c_name))
             elif int (Ch)==9:
                 c_image=input("please specify the image id")
                 os.system("ssh {} docker rmi {}".format(ip,c_image))
             elif int (Ch)==10:
                 c_name=input("Please specify the name of the Container")
                 os.system("ssh {} docker rm {}".format(ip,c_name))
             elif int (Ch)==11:
                 os.system("ssh {} docker ps -a".format(ip))
             elif int(Ch)==12:
                 c_name=input("Please specify the name of the Container")
                 os.system("ssh {} docker logs {}".format(ip,c_name))
             elif int(Ch)==13:
                 os.system("ssh {} systemctl start docker".format(ip))
             elif int(Ch)==14:
                 os.system("ssh {} systemctl stop docker".format(ip))
             elif int(Ch)==15:
                 os.system("ssh {} systemctl status docker".format(ip))
        elif int(Ch)==5:
             os.system("tput setaf 6")
             print("""\t\t

                                        ========================================================================================
                                        |                              HADOOP CONFIGURATION:-                                  |
                                        |                                                                                      |
                                        ========================================================================================
                                        |   1  |     For configuring the Hadoop Name Node....                                  |
                                        ========================================================================================
                                        |   2  |     For configuring the Hadoop Data Node....                                  |
                                        ========================================================================================
                                        |   3  |     For configuring the Hadoop Client....                                     |
                                        ========================================================================================
                                        |   4  |     For viewing the report of connected DataNodes to the NameNode....         |
                                        ========================================================================================
                                        |   5  |     For stopping the Name Node or Data Node....                               |
                                        ========================================================================================
                                        |   6  |     For starting the Name Node or Data Node....                               |
                                        ========================================================================================
                                        |   7  |     For viewing the Name Node or Data Node Services are running or not....    |
                                        ========================================================================================
                                        |   8  |     For creating a File and then uploading the File from the Hadoop Client....|
                                        ========================================================================================
                                        |   9  |     For uploading the Existing File from the Hadoop Client....                |
                                        ========================================================================================
                                        |   10 |     For viewing all the Files uploaded by the Hadoop Client....               |
                                        ========================================================================================
                                        |   11 |     For reading the File uploaded by the Hadoop Client....                    |
                                        ========================================================================================
                                        |   12  |     For removing the File uploaded by the Hadoop Client....                  |
                                        ========================================================================================

             """)
             Ch=input("Enter Your Choice: ")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 os.system("echo -e '\n[java]\nbaseurl=https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html#license-lightbox\ngpgcheck=0' >> /etc/yum.repos.d/java.repo")
                 os.system("echo -e '\n[hadoop]\nhttps://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm\ngpgcheck=0' >> /etc/yum.repos.d/hadoop.repo")
                 os.system("yum repolist")
                 os.system("yum install java -y")
                 os.system("yum install hadoop -y")
                 folder_name=input("Enter the folder Name you want to use in the cluster: ")
                 #hdfs-site.xml file configuration
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                 os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<property>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<name>dfs.name.dir</name>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<value>/%s</value>" >> /etc/hadoop/hdfs-site.xml' %foldername)
                 os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "</property>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/hdfs-site.xml')
                 #core-site.xml file configuration
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
                 os.system('echo "  " >> /etc/hadoop/core-site.xml')
                 os.system('echo "<!Put site-specific property overrides in this file.>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<name>fs.default.name</name>" >> /etc/hadoop/core-site.xml')
                 ipadd=input("enter the public ip address of the namenode and port no. in like IPaddress:portNumber :_____")
                 os.system('echo "<value>hdfs://%s</value>" >> /etc/hadoop/core-site.xml' %ipadd)
                 os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')
                 os.mkdir(foldername)
                 os.system('hadoop namenode -format')
                 os.system('hadoop-daemon.sh start namenode')
                 os.system('jps')
             elif int(Ch)==2:
                 foldername=input("Enter the folder Name you want to use in the cluster: ")
                 #hdfs-site.xml file configuration
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                 os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo " " >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml') 
                 os.system('echo "<property>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<name>dfs.data.dir</name>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "<value>/%s</value>" >> /etc/hadoop/hdfs-site.xml' %foldername)
                 os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "</property>" >> /etc/hadoop/hdfs-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/hdfs-site.xml')
                 #core-site.xml file configuration
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
                 os.system('echo "  " >> /etc/hadoop/core-site.xml')
                 os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<name>fs.default.name</name>" >> /etc/hadoop/core-site.xml')
                 ipadd=input("enter the public ip address of the namenode and port no. in like IPaddress:portNumber :_____")
                 os.system('echo "<value>hdfs://%s</value>" >> /etc/hadoop/core-site.xml' %ipadd)
                 os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')
                 os.mkdir(foldername)
                 os.system('hadoop-daemon.sh start datanode')
                 os.system('jps')
             elif int(Ch)==3:
                 os.system("echo -e '\n[java]\nbaseurl=https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html#license-lightbox\ngpgcheck=0' >> /etc/yum.repos.d/java.repo")
                 os.system("echo -e '\n[hadoop]\nhttps://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm\ngpgcheck=0' >> /etc/yum.repos.d/hadoop.repo")
                 os.system("yum repolist")
                 os.system("yum install java -y")
                 os.system("yum install hadoop -y")
                 os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                 os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?> >> /etc/hadoop/core-site.xml")
                 os.system('echo "  " >> /etc/hadoop/core-site.xml')
                 os.system('echo "<!-- Put site-specific property overrides in this file. -->" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "<name>fs.default.name</name>" >> /etc/hadoop/core-site.xml')
                 ipadd=input("enter the public ip address of the Namenode and port no. in like IPaddress:portNumber :_____")
                 os.system('echo "<value>hdfs://%s</value>" >> /etc/hadoop/core-site.xml' %ipadd)
                 os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
                 os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')                                                                                                      
             elif int(Ch)==4:
                 os.system("ssh {} hadoop dfsadmin -report".format(ip))
             elif int(Ch)==5:
                 Node=input("Enter the Name of the Node which you want to Stop(namenode/datanode): ")
                 os.system("ssh {} hadoop-daemon.sh stop {}".format(ip,Node))
             elif int(Ch)==6:
                 Node=input("Enter the Name of the Node which you want to Start(namenode/datanode): ")
                 os.system("ssh {} hadoop-daemon.sh start {}".format(ip,Node))
             elif int(Ch)==7:
                 os.system("ssh {} jps".format(ip))
             elif int(Ch)==8:
                 page=input("Enter the Name for the File you want to Create:")
                 os.system("vi {}".format(page))
                 os.system("ssh {} hadoop fs -put {} /".format(ip,page))
             elif int(Ch)==9:
                 page=input("Enter the Existing File Name:")
                 os.system("ssh {} hadoop fs -put {} /".format(ip,page))
             elif int(Ch)==10:
                 os.system("ssh {} hadoop fs -ls / ".format(ip))
             elif int(Ch)==11:
                 page=input("Enter the File Name you want to Read:")
                 os.system("ssh {} hadoop fs -cat /{}".format(ip,page))
             elif int(Ch)==12:
                 page=input("Enter the File Name you want to Delete:")
                 os.system("ssh {} hadoop fs -rm /{}".format(ip,page))


        elif int(Ch)==6:
             os.system("tput setaf 6")
             print("""\t\t                                                                             
                                                                                                                                                                                                             ============================================================================================                                                                            |                                 AWS CONFIGURATION:-                                      |
                                     |                                                                                          |
                                     ============================================================================================
                                     |   1  |      For setting up the AWS CLI....                                               |
                                     ============================================================================================
                                     |   2  |      For logging to the AWS Account by giving Credentials....                     |
                                     ============================================================================================
                                     |   3  |      For creating a Key-Pair on the AWS....                                       |
                                     ============================================================================================
                                     |   4  |      For creating a Security-Group on the AWS....                                 |
                                     ============================================================================================
                                     |   5  |      For adding Inbound Rules to the Security-Group....                           |
                                     ============================================================================================
                                     |   6  |      For removing the Inbound Rules from the Security-Group.....                  |
                                     ============================================================================================
                                     |   7  |      For launching an EC2 Instance on the top of AWS....                          |
                                     ============================================================================================
                                     |   8  |      For creating an EBS Volume on the AWS....                                    |
                                     ============================================================================================
                                     |   9  |      For attaching an EBS Volume to the EC2 Instance....                          |
                                     ============================================================================================
                                     |   10 |      For creating a S3 Bucket on AWS....                                          |
                                     ============================================================================================
                                     |   11 |      For uploading the Content to the S3 Bucket....                               |
                                     ============================================================================================
                                     |   12 |      For giving Public Access to the S3 Bucket and the Uploaded Content....       |
                                     ============================================================================================
                                     |   13 |      For creating a Cloud Front Distribution on the AWS....                       |
                                     ============================================================================================
                                     |   14 |      For viewing all the Existing Key-Pairs on the AWS....                        |
                                     ============================================================================================
                                     |   15 |      For viewing all the Existing Security-Groups....                             |
                                     ============================================================================================
                                     |   16 |      For viewing all the Existing EC2 Instances....                               |
                                     ============================================================================================
                                     |   17 |      For viewing all the Existing EBS Volumes....                                 |
                                     ============================================================================================
                                     |   18 |      For viewing all the Existing S3 Buckets....                                  |
                                     ============================================================================================
                                     |   19 |      For viewing all the Existing CLoud Front Distribution....                    |
                                     ============================================================================================
                                     |   20 |      For deleting the Key-Pair from the AWS....                                   |
                                     ============================================================================================                                                                            |   21 |      For deleting the Security-Group from the AWS....                             |                                                                            ============================================================================================                                                                            |   22 |      For deleting the EC2 Instances from the AWS....                              |                                                                            ============================================================================================                                                                            |   23 |      For deleting the EBS Volumes from the AWS....                                |                                                                            ============================================================================================                                                                            |   24 |      For deleting the S3 Bucket from the AWS....                                  |                                                                            ============================================================================================                                                                            |   25 |      For deleting the Cloud Front Distribution....                                |                                                                            ============================================================================================                                                                            |   26 |      For detaching the EBS Volume from the EC2 Instance....                       |                                                                            ============================================================================================                                                                            |   27 |      For stopping the EC2 Instance....                                            |                                                                            ============================================================================================                                                                            |   28 |      For starting the EC2 Instance....                                            |                                                                            ============================================================================================                                            
                   """) 
             Ch=input("Enter Your Choice:")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 os.system("ssh {} yum install python2 -y".format(ip)) 
                 os.system("ssh {} pip2 install awscli".format(ip)) 
                 os.system("ssh {} pip2 install awscli --upgrade".format(ip)) 
                 os.system("ssh {} aws --version".format(ip))
             elif int(Ch)==2:
                 os.system("ssh {} aws configure".format(ip))
             elif int(Ch)==3:
                 key=input("Enter the Name for the Key-Pair you want to Create")
                 os.system("ssh {} aws ec2 create-key-pair --key-name {}".format(ip,key))
             elif int(Ch)==4:
                 sg=input("Enter the Name for the Security Group you want to Create:")
                 os.system("ssh {} aws ec2 security-group-name --group-name {} --description {}".format(ip,sg,sg))
             elif int(Ch)==5:
                 sgi=input("Enter the Security Group ID to which you want to Add the Rules:")
                 protocol=input("Enter the Protocol Name:")
                 port=input("Enter the Port No:")
                 cidr=input("Enter the CIDR:")
                 os.system("ssh {} aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(ip,sgi,protocol,port,cidr))
             elif int(Ch)==6:
                 sgname=input("Enter the Security Group Name from which you want to Delete the Rules:")
                 protocol=input("Enter the Protocol Name:")
                 port=input("Enter the Port No:")
                 cidr=input("Enter the CIDR:")
                 os.system("ssh {} aws ec2 revoke-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}".format(ip,sgname,protocol,port,cidr))
             elif int(Ch)==7:
                 ami=input("Enter the AMI ID for launching EC2 Instance:")
                 count=int(input("How many Instances you want to Launch:"))
                 itype=input("Enter the Instance Type for launching the Instance:")
                 key=input("Enter the Key-Pair you want to use for launching the Instance:")
                 sg=input("Enter the Security-Group ID you want to use for launching the Instance:")
                 subnet=input("Enter the Subnet ID to which you want to launch the Instance:")
                 os.system("ssh {} aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {}".format(ip,ami,count,itype,key,sg,subnet))
             elif int(Ch)==8:
                 vtype=input("Enter the Volume Type")
                 size=int(input("Enter the Size for the EBS Volume:"))
                 az=input("Enter the Availability Zone:")
                 os.system("ssh {} aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(ip,vtype,size,az))
             elif int(Ch)==9:
                 vid=input("Enter that EBS Volume ID which you want to attach to the EC2 Instance:")
                 iid=input("Enter the Instance ID to which you want to attach the EBS Volume:")
                 device=input("Enter the Device Name:")
                 os.system("ssh {} aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(ip,vid,iid,device))
             elif int(Ch)==10:
                 bname=input("Enter a Name for creating the S3 Bucket:")
                 az=input("Enter the Region in which you want to create the S3 Bucket:")
                 os.system("ssh {} aws s3 mb s3://{} --region {}".format(ip,bname,az))
             elif int(Ch)==11:
                 folder=input("Enter the Folder or Directory Name from which you want to upload the Content:")
                 content=input("Enter the Content Name you want to upload to the S3 Bucket:")
                 bname=input("Enter the Bucket Name to which you want to upload the Content:")
                 os.system("ssh {} aws s3 cp {}:/{} s3://{}".format(ip,folder,content,bname))
             elif int(Ch)==12:
                 content=input("Enter the Content Name you want to upload to the S3 Bucket:")
                 bname=input("Enter the Bucket Name to which you want to upload the Content:")
                 os.system("ssh {} aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(ip,bname,content))
             elif int(Ch)==13:
                 content=input("Enter the Content Name you want to upload to the S3 Bucket:")
                 bname=input("Enter the Bucket Name to which you want to upload the Content:")
                 az=input("Enter the Region in which you want to create the S3 Bucket:")
                 os.system("ssh {} aws cloudfront create-distribution --origin-domain-name  {}.s3.{}.amazonaws.com --default-root-object {}".format(ip,bname,az,content))
             elif int(Ch)==14:
                 os.system("ssh {} aws ec2 describe-key-pairs".format(ip))
             elif int(Ch)==15:
                 os.system("ssh {} aws ec2 describe-security-groups".format(ip))
             elif int(Ch)==16:
                 os.system("ssh {} aws ec2 describe-instances".format(ip))
             elif int(Ch)==17:
                 os.system("ssh {} aws ec2 describe-volumes".format(ip))
             elif int(Ch)==18:
                 os.system("ssh {} aws s3api list-buckets".format(ip))
             elif int(Ch)==19:
                 os.system("ssh {} aws cloudfront list-distributions".format(ip))
             elif int(Ch)==20:
                 os.system("ssh {} aws ec2 delete-key-pair --key-name {}".format(ip))
             elif int(Ch)==21:
                 sg=input("Enter the Security-Group Name which you want to Delete:")
                 os.system("ssh {} aws ec2 delete-security-group --group-name {}".format(ip,sg))
             elif int(Ch)==22:
                 iid=input("Enter the Instance ID which you want to Terminate:")
                 os.system("ssh {} aws ec2 terminate-instances --instance-ids {}".format(ip,iid))
             elif int(Ch)==23:
                 vid=input("Enter the Volume ID which you want to Delete:")
                 os.system("ssh {} aws ec2 delete-volume --volume-id {}".format(ip,vid))
             elif int(Ch)==24:
                 bname=input("Enter the S3 Bucket Name which you want to Delete:")
                 az=input("Enter the Region from which you want to Delete the S3 Bucket:")
                 os.system("ssh {} aws s3api delete-bucket --bucket {} --region {}".format(ip,bname,az))
             elif int(Ch)==25:
                 cid=input("Enter the Cloud Front ID which you want to Delete:")
                 os.system("ssh {} aws cloudfront delete-distribution --id {}".format(ip,cid))
             elif int(Ch)==26:
                 vid=input("Enter the Volume ID which you want to Detach from the Instance:")
                 os.system("ssh {} aws ec2 detach-volume --volume-id {}".format(ip,iid))
             elif int(Ch)==27:
                 iid=input("Enter the Instance ID which you want to Stop:")
                 os.system("ssh {} aws ec2 stop-instances --instance-ids {}".format(ip,iid))
             elif int(Ch)==28:
                 iid=input("Enter the Instance ID which you want to Start:")
                 os.system("ssh {} aws ec2 start-instances --instance-ids {}".format(ip,iid))

        elif int(Ch)==7:
             os.system("tput setaf 6")
             print("""\t\t
                                                          
                                      =================================================================================== 
                                      |                              LINUX BASICS:-                                     |
                                      |                                                                                 |
                                      ===================================================================================
                                      |   1  |      For pinging to a OS for particular No of Times....                  |
                                      ===================================================================================
                                      |   2  |      For creating more Users....                                         |
                                      ===================================================================================
                                      |   3  |      For checking the Software is present inside the OS or not....       |
                                      ===================================================================================
                                      |   4  |      For knowing more about the Command and its Syntax....               |
                                      ===================================================================================
                                      |   5  |      For viewing the IP Address of the OS....                            |
                                      ===================================================================================
                                      |   6  |      For viewing all the Usable Ports....                                |
                                      ===================================================================================
                                      |   7  |      For disabling the Firewall....                                      |
                                      ===================================================================================
                                      |   8  |      For enabling the Firewall....                                       |
                                      ===================================================================================
                                      |   9  |      For starting the Firewall....                                       |
                                      ===================================================================================
                                      |   10 |      For stopping the Firewall....                                       |
                                      ===================================================================================
                                      |   11 |      For viewing the Status of the Firewall....                          |
                                      ===================================================================================
                                      |   12 |      For running any of the Linux Commands....                           |
                                      ===================================================================================
                             """)
             Ch=input("Enter Your Choice:")
             os.system("tput setaf 2")
             if int(Ch)==1:
                 ip1=input("Enter the OS IP for Pinging:")
                 n=input("Enter the No. of Times:")
                 os.system("ssh {} ping -c {} {}".format(ip,n,ip1))
             elif int(Ch)==2:
                 user=input("Enter the User Name:")
                 os.system("ssh {} useradd {} ".format(ip,user))
                 os.system("ssh {} passwd {} ".format(ip,user))
             elif int(Ch)==3:
                 software=input("Enter the Software Name:")
                 os.system("ssh {} rpm -q {}".format(ip,software))
             elif int(Ch)==4:
                 command=input("Enter the Command Name for knowing its Syntax:")
                 os.system("ssh {} man {}".format(ip,command))
             elif int(Ch)==5:
                 os.system("ssh {} ifconfig".format(ip))
             elif int(Ch)==6:
                 os.system("ssh {} netstat -tnlp".format(ip))
             elif int(Ch)==7:
                 os.system("ssh {} systemctl disable firewalld".format(ip))
             elif int(Ch)==8:
                 os.system("ssh {} systemctl enable firewalld".format(ip))
             elif int(Ch)==9:
                 os.system("ssh {} systemctl start firewalld".format(ip))
             elif int(Ch)==10:
                 os.system("ssh {} systemctl stop firewalld".format(ip))
             elif int(Ch)==11:
                 os.system("ssh {} systemctl status firewalld".format(ip))
             elif int(Ch)==12:
                 command=input("Enter the Command:")
                 os.system("ssh {} {}".format(ip,command))

        elif int(Ch)==8:
            os.system("tput setaf 2")
            print("\t\t\t\t\t\t\t\t\t THANK YOU!!")
            exit()    