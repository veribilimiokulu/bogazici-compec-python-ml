#!/usr/bin/env python
# coding: utf-8

# # Soru-1

#     "beni büyük harf yap" cümlesinin tüm harflerini büyük harf yapan ve ekrana yazdıran Python kodlarını yazınız.

# # Cevap-1

# In[12]:


print("beni büyük harf yap".upper())


# # Soru-2

#     1 ile 10 arasındaki tam sayıları (1 ve 10 dahil) azalan şekilde ekrana yazdıran Python kodlarını yazınız.

# # Cevap-2

# In[7]:


for i in range(10,0,-1):
    print(i)


# # Soru-3

#     3 ile 19 arasındaki tek sayıları (3 ve 19 dahil) ekrana yazdıran Python kodlarını yazınız.

# # Cevap-3

# In[8]:


for i in range(3,20,1):
    if(i%2) != 0:
        print(i)


# # Soru-4

#     [1,3,["Elma","Muz"], 25,198, [22,32]] Python listesinde bulunan Muz'u ekrana yazdırınız.

# # Cevap-4

# In[10]:


my_list = [1,3,["Elma","Muz"], 25,198, [22,32]]
print(my_list[2][1])


# # Soru-5

#     {"Ankara":["Etimesgut","Çankaya","Yenimahalle"], "İstanbul":[["Kadıköy-Rıhtım","Kadıköy-Boğa"],"Üsküdar","Beşiktaş"]}
#     Bir şirkete ait şubeler yukarıdaki Python sözlük yapısı içinde belirtilmiştir. Bu şirketin Kadıköy-Boğa şubesini ekrana yazdırınız.

# In[13]:


sirket_sozluk = {"Ankara":["Etimesgut","Çankaya","Yenimahalle"], "İstanbul":[["Kadıköy-Rıhtım","Kadıköy-Boğa"],"Üsküdar","Beşiktaş"]}
print(sirket_sozluk["İstanbul"][0][1])


# # Soru-6

#     Veri bilimi çalışmalarında kullanılan üç adet Python kütüphensini yazınız.

# # Cevap-6

#     1. pandas
#     2. numpy
#     3. matplotlib
#     4. sklearn veya scikit-learn
#     5. seaborn
#     6. scipy

# # Soru-7

#     Sınıflandırma algoritmalarından üç tanesini yazınız.

# # Cevap-7

#     1. K-Enyakın Komşu (K-Nearest eigbor)
#     2. Naive Bayes
#     3. Karar Ağacı (Decision Tree)
#     4. Rastgele Orman (Random Forest)
#     5. Destek Vektör makinesi (Support Vector Machine) ya da SVM
#     6. Lojistik Regresyon

# # Soru-8

#     İki numerik değişken ile ilgili olarak korelasyon neyi ölçer?

# # Cevap-8

# Korelasyon iki değişken arasındaki doğrusal ilişkiyi ölçer.

# # Soru-9

#     Sınıflandırma model değerlendirme esnasında kullanılan kavramlardan üç tanseini yazınız. Örneğin: Accuracy

# # Cevap-9

#     1. Accuracy
#     2. F1 Score
#     3. Precision
#     4. Recall
#     5. ROC AUC Score
#     6. False Positive
#     7. False Negative
#     8. True Positive
#     9. True Negative

# # Soru-10

#     İstatistiksel hipotez testinde Tip-1 hata ne anlama gelir?

# # Cevap-10

# H0 hipotezi doğru iken onu reddetmektir.
