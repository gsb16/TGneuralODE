import json
import os
from PIL import Image, ImageFilter

for dir in os.listdir('UFPR-ALPR dataset'):  
  for folder in os.listdir("UFPR-ALPR dataset/"+dir):  
    for filename in os.listdir("UFPR-ALPR dataset/"+dir+"/"+folder):
      extension = os.path.splitext(filename)[-1].lower()
      if (extension == ".png"):  
        chaves = {}
        # print(dir+"/"+folder+"/"+filename)
        label = filename.replace('png','txt')
        with open(os.path.join("UFPR-ALPR dataset/"+dir+"/"+folder, label), "r") as fh:
            for line in fh:
                chave, valor = line.strip().split(': ', 1)
                chaves[chave] = valor.strip()

        first_l = chaves.get("plate")[0]
        second_l = chaves.get("plate")[1]
        third_l = chaves.get("plate")[2]
        fourth_l = chaves.get("plate")[4]
        fifth_l = chaves.get("plate")[5]
        sixth_l = chaves.get("plate")[6]
        seventh_l = chaves.get("plate")[7]


        text = chaves.get("char 1")
        first_pos = [int(n) for n in text.split(' ')]
        text = chaves.get("char 2")
        second_pos = [int(n) for n in text.split(' ')]
        text = chaves.get("char 3")
        third_pos = [int(n) for n in text.split(' ')]
        text = chaves.get("char 4")
        fourth_pos = [int(n) for n in text.split(' ')]
        text = chaves.get("char 5")
        fifth_pos = [int(n) for n in text.split(' ')]
        text = chaves.get("char 6")
        sixth_pos = [int(n) for n in text.split(' ')]
        text = chaves.get("char 7")
        seventh_pos = [int(n) for n in text.split(' ')]

        # Número de pixels de padding
        buffer = 1

        temp = label.replace('txt','')
        img = Image.open("UFPR-ALPR dataset/"+dir+"/"+folder+"/"+filename)
        img_gray = Image.open("UFPR-ALPR dataset/"+dir+"/"+folder+"/"+filename).convert('L')
        img_noise = Image.open("UFPR-ALPR dataset/"+dir+"/"+folder+"/"+filename).filter(ImageFilter.UnsharpMask(radius=2, percent=125))

        img1 = img.crop((first_pos[0]-buffer, first_pos[1]-buffer, first_pos[0]+first_pos[2]+buffer, first_pos[1]+first_pos[3]+buffer))
        img1gray = img_gray.crop((first_pos[0]-buffer, first_pos[1]-buffer, first_pos[0]+first_pos[2]+buffer, first_pos[1]+first_pos[3]+buffer))
        img1noise = img_noise.crop((first_pos[0]-buffer, first_pos[1]-buffer, first_pos[0]+first_pos[2]+buffer, first_pos[1]+first_pos[3]+buffer))
        img1.save(os.path.join("cropped/"+dir+"/"+first_l, temp+"img1.png"))
        img1gray.save(os.path.join("cropped/"+dir+"/"+first_l, temp+"img1gray.png"))
        img1noise.save(os.path.join("cropped/"+dir+"/"+first_l, temp+"img1noise.png"))

        img2 = img.crop((second_pos[0]-buffer, second_pos[1]-buffer, second_pos[0]+second_pos[2]+buffer, second_pos[1]+second_pos[3]+buffer))
        img2gray = img_gray.crop((second_pos[0]-buffer, second_pos[1]-buffer, second_pos[0]+second_pos[2]+buffer, second_pos[1]+second_pos[3]+buffer))
        img2noise = img_noise.crop((second_pos[0]-buffer, second_pos[1]-buffer, second_pos[0]+second_pos[2]+buffer, second_pos[1]+second_pos[3]+buffer))
        img2.save(os.path.join("cropped/"+dir+"/"+second_l, temp+"img2.png"))
        img2gray.save(os.path.join("cropped/"+dir+"/"+second_l, temp+"img2gray.png"))
        img2noise.save(os.path.join("cropped/"+dir+"/"+second_l, temp+"img2noise.png"))

        img3 = img.crop((third_pos[0]-buffer, third_pos[1]-buffer, third_pos[0]+third_pos[2]+buffer, third_pos[1]+third_pos[3]+buffer))
        img3gray = img_gray.crop((third_pos[0]-buffer, third_pos[1]-buffer, third_pos[0]+third_pos[2]+buffer, third_pos[1]+third_pos[3]+buffer))
        img3noise = img_noise.crop((third_pos[0]-buffer, third_pos[1]-buffer, third_pos[0]+third_pos[2]+buffer, third_pos[1]+third_pos[3]+buffer))
        img3.save(os.path.join("cropped/"+dir+"/"+third_l, temp+"img3.png"))
        img3gray.save(os.path.join("cropped/"+dir+"/"+third_l, temp+"img3gray.png"))
        img3noise.save(os.path.join("cropped/"+dir+"/"+third_l, temp+"img3noise.png"))

        img4 = img.crop((fourth_pos[0]-buffer, fourth_pos[1]-buffer, fourth_pos[0]+fourth_pos[2]+buffer, fourth_pos[1]+fourth_pos[3]+buffer))
        img4.save(os.path.join("cropped/"+dir+"/"+fourth_l, temp+"img4.png"))

        img5 = img.crop((fifth_pos[0]-buffer, fifth_pos[1]-buffer, fifth_pos[0]+fifth_pos[2]+buffer, fifth_pos[1]+fifth_pos[3]+buffer))
        img5.save(os.path.join("cropped/"+dir+"/"+fifth_l, temp+"img5.png"))

        img6 = img.crop((sixth_pos[0]-buffer, sixth_pos[1]-buffer, sixth_pos[0]+sixth_pos[2]+buffer, sixth_pos[1]+sixth_pos[3]+buffer))
        img6.save(os.path.join("cropped/"+dir+"/"+sixth_l, temp+"img6.png"))

        img7 = img.crop((seventh_pos[0]-buffer, seventh_pos[1]-buffer, seventh_pos[0]+seventh_pos[2]+buffer, seventh_pos[1]+seventh_pos[3]+buffer))
        img7.save(os.path.join("cropped/"+dir+"/"+seventh_l, temp+"img7.png"))
