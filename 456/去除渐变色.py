from PIL import Image,ImageFilter
import subprocess
def cleanFile(filepath,newfilepath):
    image=Image.open(filepath)
    #对图片进行阈值过滤，然后保存
    image=image.point(lambda x:0 if x<143 else 255)
    image.save(newfilepath)

    #调用系统的tesseract命令对图片进行ocr识别
    subprocess.call(['tesseract',newfilepath,'output'])

    #打开文件读取结果
    outputFile=open('output.txt','r')
    print(outputFile.read())
    outputFile.close()


cleanFile('1.tif','text.png')