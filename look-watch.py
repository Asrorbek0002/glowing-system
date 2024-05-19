# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:12:33 2024

@author: Asilbek
"""

# if va else kamciligi faqat shu bir shratni tekshirish mumkun
#son=-2
#f son>0:
#    print("Musbat son")
#else:
 #   print("Manfiy son")
#yosh=int(input("Yoshingiz nechida:"))
#if yosh<=4:
 #  narh=0  
#elif yosh<=12:    
 #  narh=5000
#elif yosh<=18:
 #  narh=8000  
#else:    
 # narh=10000
#print(f"Sizga kirish {narh}")          
 #ko'rgan bo'lsangiz siz elif qo'shimchasi kiritilgan bu yerda sizga bu qulaylik beradi shuni ko'plab qilishmiz mumkin
   # else ni manosi biz bilamiz shu yerda agar , aks holda deb tarjima qilnadi
# ko' dasturchilar qiladi ular hech qachon kodni qayta qayta yozmaysi chunki shu yersa ular
 # or va and operatorida biz shug'ulanamz shu kabi ikki yoki undan ortiq so'zlarni kiritganimizda foyalanamiz
#kun=input("Bugun kun nima:")
#if kun.lower()=="shanba" or kun.lower()=="yakshanba":
 #   print("Bugun dam olish kuni")
#else:
 #   print("Bugun ish kuni")
 # Bizga malumki har doim foydalanuvchidan ikki narsa so'raladi shunda and operatori bajariladi
#kun=input("Bugun nima kun:")
#harorat=float(input("Havo harorati qanday?"))
#if kun.lower()=="yakshanba" or kun.lower()=="shanba" and harorat>=36:
 #   print("Biz cho'milgani chiqamiz")
#elif kun.lower()=="yakshanba" or kun.lower()=="shanba" and harorat<36:
 #   print("Biz cho'milgani chiqmaymiz or Uyda dam olamiz") 
#boolean bizga malumki shu kabi so'zlar mantiqiy malumot turi deb bilishi mumkin 
#narh=15000
#chay=True
#salar=False

#if  'choy and salat':
 #    narh=narh+10000
#elif 'choy or salat':   
#     narh=narh+5000 
#      print(f"Jami" {"narh"} som" )
#narh=15000
#choy = True
#salat= True
#if choy and salat:
 #   narh=narh+40000
#elif choy or salat:
 #   narh=narh+5000
  #  print(f"Jami {narh} so'm")
#narh=0
#choy=False
#salat=True
#if choy and salat:
 #   narh=narh+10000
#elif choy or salat:
 #   narh=narh+5000
    
 
    

#print(f"Jami {narh} so'm")
#narh=15000
#choy=1
#salat=1
#non=1
#kompot=1
#assorti=0
#if choy:
 #   print("Mijoz choy oldi")
  #  narh=narh+3000
#if salat:
 #   print("Mijoz salat oldi")
  #  narh=narh+5000
#if non:
 #   print("Mijoz non oldi")
  #  narh=narh+2000
#if kompot:
 #   print("Mijoz kompot oldi")
  #  narh=narh+5000
#if assorti:
 #  print("Mijoz assorti oldi")
  # narh=narh+6000
   
# these are books because Whenever Ihave some free time I read these books
#print(f"Jami {narh} so'm")  
 # in operatori biz menun ichida bor yoki yoq ekanligini tekshirishimiz mumkun
#menu=["osh","qazonkabob","shashlik","nrin","somsa"]
#"manti" in menu #meuni ichida bor narsa ekan shu kabi sonlarni teshirish kerak
#ovqat=input("Nima ovqat yeysiz?>>>")
#if ovqat.lower() not in menu:
#     print("Afsuski bizda bunday ovqat yo'q")
#else:
#    print("Buyurtma qabul qilindi")    
menu=["osh","qazonkabob","shashlik","nrin","somsa"]   
buyurtmalar=["osh","somsa","manti","shashlik"]
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"menu  {taom} bor")
        else:
            print(f"Kechirasiz, menu {taom} yo'q")
      
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
