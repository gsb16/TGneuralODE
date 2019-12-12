import json
import os
from PIL import Image

for dir in os.listdir('UFPR-AMR Dataset'):  
  for filename in os.listdir("UFPR-AMR Dataset/"+dir):
    extension = os.path.splitext(filename)[-1].lower()
    if (extension == ".jpg"):  
      chaves = {}
      print(dir+"/"+filename)
      label = filename.replace('jpg','txt')
      with open(os.path.join("UFPR-AMR Dataset/"+dir, label), "r") as fh:
          for line in fh:
              chave, valor = line.strip().split(': ', 1)
              chaves[chave] = valor.strip()

      first_l = chaves.get("reading")[0]
      second_l = chaves.get("reading")[1]
      third_l = chaves.get("reading")[2]
      fourth_l = chaves.get("reading")[3]
      fifth_l = chaves.get("reading")[4]


      text = chaves.get("digit 1")
      first_pos = [int(n) for n in text.split(' ')]
      text = chaves.get("digit 2")
      second_pos = [int(n) for n in text.split(' ')]
      text = chaves.get("digit 3")
      third_pos = [int(n) for n in text.split(' ')]
      text = chaves.get("digit 4")
      fourth_pos = [int(n) for n in text.split(' ')]
      text = chaves.get("digit 5")
      fifth_pos = [int(n) for n in text.split(' ')]

      # Número de pixels de padding
      buffer = 4

      temp = label.replace('txt','')
      img = Image.open("UFPR-AMR Dataset/"+dir+"/"+filename)
      img1 = img.crop((first_pos[0]-buffer, first_pos[1]-buffer, first_pos[0]+first_pos[2]+buffer, first_pos[1]+first_pos[3]+buffer))
      img1.save(os.path.join("cropped/"+dir+"/"+first_l, temp+"img1.jpg"))

      img2 = img.crop((second_pos[0]-buffer, second_pos[1]-buffer, second_pos[0]+second_pos[2]+buffer, second_pos[1]+second_pos[3]+buffer))
      img2.save(os.path.join("cropped/"+dir+"/"+second_l, temp+"img2.jpg"))

      img3 = img.crop((third_pos[0]-buffer, third_pos[1]-buffer, third_pos[0]+third_pos[2]+buffer, third_pos[1]+third_pos[3]+buffer))
      img3.save(os.path.join("cropped/"+dir+"/"+third_l, temp+"img3.jpg"))

      img4 = img.crop((fourth_pos[0]-buffer, fourth_pos[1]-buffer, fourth_pos[0]+fourth_pos[2]+buffer, fourth_pos[1]+fourth_pos[3]+buffer))
      img4.save(os.path.join("cropped/"+dir+"/"+fourth_l, temp+"img4.jpg"))

      img5 = img.crop((fifth_pos[0]-buffer, fifth_pos[1]-buffer, fifth_pos[0]+fifth_pos[2]+buffer, fifth_pos[1]+fifth_pos[3]+buffer))
      img5.save(os.path.join("cropped/"+dir+"/"+fifth_l, temp+"img5.jpg"))
