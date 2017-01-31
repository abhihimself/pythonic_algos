import requests
import time


while(1):
    time.sleep(4)
    f = open("output.txt", 'a')
    output=requests.get("http://ec2-54-255-192-162.ap-southeast-1.compute.amazonaws.com/sliq/get_turnserver.php")
    current_time=time.time()
    print (current_time,"ip is", output.content)
    f.write('{0}: ip is {1}'.format(current_time,output.content))
    f.write("\n")
    f.close()
