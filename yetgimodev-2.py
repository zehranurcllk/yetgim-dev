# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 15:28:25 2025

@author: Zehranur
"""

"""
#1. Listedeki En Büyük Sayıyı Bulma 
**Problem Tanımı:** Verilen bir tamsayı listesindeki en büyük sayıyı bulan bir fonksiyon yazın.
giris = input("lütfen aralarına boşluk koyarak sayıları girin:")
sayi_listesi = list(map(int , giris.split()))
en_buyuk = max(sayi_listesi)
print("girdiğiniz listedeki en büyük sayı:",en_buyuk)"""


""""# 2. String'i Ters Çevirme 
#Problem Tanımı:Verilen bir string'i ters çeviren bir fonksiyon yazın.
metin=input("bir metin girin:")
ters_metin=metin[::-1]
print("girdiğiniz öetinin tersi:", ters_metin)"""



"""#3. Faktöriyel Hesaplama **Problem Tanımı:** Negatif olmayan bir tamsayının faktöriyelini hesaplayan bir fonksiyon yazın.
sayi = int(input("faktöriyelini hesaplamak istediğiniz negatif olmayan sayıyı girin:"))
if sayi <0:
    print("negatif sayının faktöriyeli hesaplanmaz")
else:
   faktoriyel = 1
   for i in range (1, sayi+1):
    faktoriyel *= i
   print(f"{sayi}sayısının faktöriyeli: {faktoriyel}")"""
   
   
"""#4. Listedeki Çift Sayıları Filtreleme **Problem Tanımı:** Verilen bir tamsayı listesindeki yalnızca çift sayıları içeren yeni bir liste döndüren bir fonksiyon yazın.
giris = input("lütfen aralarına boşluk koyarak sayıları girin:")
sayi_listesi = list(map(int, giris.split()))
cift_sayilar = [sayi for sayi in sayi_listesi if sayi % 2 == 0]
print("listedeki çift sayılar:", cift_sayilar)"""



"""#5. İki Listenin Birleşimi ve Tekilleştirilmesi **Problem Tanımı:** Verilen iki listeyi birleştiren ve tekrar eden elemanları kaldırarak tekil bir liste oluşturan bir fonksiyon yazın.
liste1 = input("1. listeyi aralarına boşluk koyarak girin: ")
liste2 = input("2. listeyi aralarına boşluk koyarak girin: ")

liste1 = list(map(int, liste1.split()))
liste2 = list(map(int, liste2.split()))

birlesik_liste = liste1 + liste2
tekil_liste = list(set(birlesik_liste))

print("Birleşmiş ve tekilleştirilmiş liste:", tekil_liste)"""


    
"""#6. Palindrom Kontrolü **Problem Tanımı:** Verilen bir string'in palindrom olup olmadığını kontrol eden bir fonksiyon yazın (tersten okunuşu aynı olan kelime/cümle).
metin = input("Bir kelime veya cümle girin: ")
temiz_metin = metin.replace(" ", "").lower()
ters_metin = temiz_metin[::-1]
if temiz_metin == ters_metin:
    print(f"'{metin}' → Palindromdur ")
else:
    print(f"'{metin}' → Palindrom değildir ")"""
    
    
    
"""7. İki Sayının En Büyük Ortak Böleni (EBOB) **Problem Tanımı:** Verilen iki pozitif tamsayının en büyük ortak bölenini (EBOB) bulan bir fonksiyon yazın.
sayi1 = int(input("1. sayıyı girin: "))
sayi2 = int(input("2. sayıyı girin: "))
ebob = 1
kucuk_sayi = min(sayi1, sayi2)

for i in range(1, kucuk_sayi + 1):
    if sayi1 % i == 0 and sayi2 % i == 0:
        ebob = i
print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {ebob}")"""


"""#8. Anagram Kontrolü **Problem Tanımı:** Verilen iki string'in anagram olup olmadığını kontrol eden bir fonksiyon yazın (aynı harfleri farklı sıralamada içeren kelimeler).
kelime1 = input("1. kelimeyi girin: ")
kelime2 = input("2. kelimeyi girin: ")
k1 = kelime1.replace(" ", "").lower()
k2 = kelime2.replace(" ", "").lower()
if sorted(k1) == sorted(k2):
    print(f"'{kelime1}' ve '{kelime2}'  Anagramdır")
else:
    print(f"'{kelime1}' ve '{kelime2}'  Anagram değildir")"""



"""#9. Listedeki Eksik Sayıyı Bulma **Problem Tanımı:** 1'den N'e kadar olan sayılardan birinin eksik olduğu bir liste veriliyor. Eksik olan sayıyı bulan bir fonksiyon yazın.
def find_missing_number(nums):
    n = len(nums)
    beklenen_toplam = n * (n + 1) // 2
    gercek_toplam = sum(nums)
    return beklenen_toplam - gercek_toplam"""


"""#10. Listeyi Belirli Bir Değere Göre Döndürme (Rotate)
#**Problem Tanımı:** Verilen bir listeyi, belirtilen `k` adımı kadar sağa döndüren bir fonksiyon yazın.
def liste_dondur(liste, k):
    n = len(liste)
    if n == 0:
        return liste
    k = k % n
    return liste[-k:] + liste[:-k]
giris = input("Listeyi girin (elemanları boşlukla ayırın): ")
sayi_listesi = list(map(int, giris.split()))
k = int(input("Kaç adım sağa döndürmek istiyorsunuz? "))

dondurulmus_liste = liste_dondur(sayi_listesi, k)
print(f"{k} adım sağa döndürülmüş liste:", dondurulmus_liste)"""



"""#11. İki Sıralı Listenin Medyanını Bulma **Problem Tanımı:** Verilen iki sıralı tamsayı listesinin birleştirilmiş halinin medyanını bulan bir fonksiyon yazın. Algoritmanın zaman karmaşıklığı O(log(m+n)) olmalıdır; burada m ve n listelerin uzunluklarıdır.
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        
        min_right1 = float('inf') if partition1 == m else nums1[partition1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]
        
        if max_left1 <= min_right2 and max_left2 <= min_right1:
        
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
          
            else:
                return max(max_left1, max_left2)
        
        
        elif max_left1 > min_right2:
            right = partition1 - 1
        
        else:
            left = partition1 + 1


giris1 = input("Birinci sıralı listeyi girin (boşlukla ayırın): ")
giris2 = input("İkinci sıralı listeyi girin (boşlukla ayırın): ")

liste1 = list(map(int, giris1.split()))
liste2 = list(map(int, giris2.split()))

medyan = findMedianSortedArrays(liste1, liste2)
print("İki listenin birleşmiş medyanı:", medyan)"""

"""#12. En Uzun Palindromik Alt String **Problem Tanımı:** Verilen bir string içindeki en uzun palindromik alt string'i bulan bir fonksiyon yazın.
def en_uzun_palindrom(s):
    if not s:
        return ""
    
    start = 0
    end = 0
    
    for i in range(len(s)):
        len1 = expand_center(s, i, i)
        len2 = expand_center(s, i, i + 1)
        max_len = max(len1, len2)
        
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end+1]

def expand_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
giris = input("Bir string girin: ")
palindrom = en_uzun_palindrom(giris)
print("En uzun palindromik alt string:", palindrom)"""


"""#13. Kelime Merdiveni (Word Ladder) **Problem Tanımı:** Bir başlangıç kelimesinden bir bitiş kelimesine, her adımda sadece bir harf değiştirerek ve her ara kelimenin verilen kelime listesinde bulunması koşuluyla en kısa dönüşüm dizisinin uzunluğunu bulun.
from collections import deque

def kelime_merdiveni(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    queue.append((next_word, steps + 1))
                    wordSet.remove(next_word)  
    return 0  
baslangic = input("Başlangıç kelimesi: ").strip()
bitis = input("Bitiş kelimesi: ").strip()
kelime_listesi = input("Kelime listesini girin (boşlukla ayırın): ").strip().split()
uzunluk = kelime_merdiveni(baslangic, bitis, kelime_listesi)
if uzunluk == 0:
    print("Dönüşüm mümkün değil.")
else:
    print("En kısa dönüşüm dizisinin uzunluğu:", uzunluk)"""

"""#14. Maksimum Alt Dizi Toplamı **Problem Tanımı:** Verilen bir tamsayı dizisindeki bitişik alt dizilerden en büyük toplama sahip olanını bulun ve bu toplamı döndürün.
def maksimum_alt_dizi_toplami(nums):
    if not nums:
        return 0
    max_suanki = max_genel = nums[0]
    for num in nums[1:]:
        max_suanki = max(num, max_suanki + num)
        max_genel = max(max_genel, max_suanki)
    return max_genel
giris = input("Tamsayı dizisini girin (boşlukla ayırın): ")
liste = list(map(int, giris.split()))

maks_toplam = maksimum_alt_dizi_toplami(liste)
print("En büyük alt dizi toplamı:", maks_toplam)"""



"""#15. Birleştirme Aralıkları (Merge Intervals)
#**Problem Tanımı:** Verilen bir aralık listesinde, çakışan aralıkları birleştirin ve yeni bir aralık listesi döndür
def birlestirme_araliklari(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev = merged[-1]
        if current[0] <= prev[1]:  # Çakışma varsa
            prev[1] = max(prev[1], current[1])  # Aralıkları birleştir
        else:
            merged.append(current)
    return merged
n = int(input("Kaç adet aralık gireceksiniz? "))
intervals = []
for _ in range(n):
    start, end = map(int, input("Aralığı girin (başlangıç bitiş): ").split())
    intervals.append([start, end])

merged_intervals = birlestirme_araliklari(intervals)
print("Birleştirilmiş aralıklar:", merged_intervals)"""







    



















