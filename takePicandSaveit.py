import cv2
import dropbox
import time
import random

global startTime

startTime = time.time()

def takePic():
    num = random.randint(1,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
        ret,frame = videoCaptureObject.read()
        imageName = "img"+str(num)+'.png'
        cv2.imwrite(imageName,frame)
        startTime = int(time.time())
        print("start1"+str(startTime))
        result = False
    
    return imageName
    print("pic taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def UploadFile(imageName):
    access_token = 'sl.A89-2YjdgIpYw75BuUHBfEjSHx0vIdgDeArvthoVoHmzj4rSMeI9jJ2tq8LbdTZU5nb-QJbfJMBQ4yjlt1Vb6NEvgoMhX4HQJNoCA-KIK3S1OVGbncd-mlj956qU6RFY_2BI0p6uG1o'
    fileName = imageName
    file_from = fileName
    file_to = '/picfolder2/'+imageName

    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')

         
def main():
    while True:
        if((int(time.time())-startTime)>=60):
            name = takePic()
            UploadFile(name)
        
    print("start2"+str(startTime))
main()

