#NIM/Namara: 13519082/Jeanne D'Arc Amara Hanieka
#Tucil 1 Strategi Algoritma

import time

def bacafilejadiarray(namafile):
    global baris
    bukafile = open('../test/'+namafile+'.txt', "r")
    baris = bukafile.read().splitlines() #taro ke array
    bukafile.close()
    return baris

def bersihinplusstrip(arraykata):
    global arraybersih
    
    jumlah = len(arraykata) #panjang baris
    for i in range(jumlah):
        arraykata[i] = arraykata[i].replace('+', '') #n gilangin + 

    arraykata.pop(jumlah-2) #karena si strip strip strip selalu di baris ke dua sblom terakhir maka di pop

    '''for i in range(jumlah-1):
        print(arraykata[i])
    print("jumlah baris array skarang:", len(arraykata))
    print('----------sampe sini ok yah----------\n')'''
    
    arraybersih = [None]*len(arraykata)
    for i in range(0, len(arraykata)):    
        arraybersih[i] = arraykata[i]; #dipindahin ke array baru biar tidak bingung
    return arraybersih

def permutasi(a, b = None): #b tuh panjangnya, jadi kalo permutasi('123',2) jadinya tuh [1,2],[2,3], dst 
    angka = tuple(a) #ini yang mo di ulang ulang critanya
    panjangangka = len(angka) #panjang katanya (ya disini angka dah critanya)
    indeks = list(range(panjangangka)) #index: 0, 1, 2 sebanyak banyaknya angka yg mo di permutasi
    #print(indeks)
    primcycle = list(range(panjangangka, panjangangka - b, -1))
    #print(primcycle)
    yield tuple(angka[i] for i in indeks[:b])
    while panjangangka:
        for i in reversed(range(b)):
            primcycle[i] = primcycle[i] - 1 #mundur
            if primcycle[i] != 0:
                j = primcycle[i]
                indeks[i], indeks[-j] = indeks[-j], indeks[i]
                yield tuple(angka[i] for i in indeks[:b])
                break
            else:
                indeks[i:] = indeks[i+1:] + indeks[i:i+1]
                primcycle[i] = panjangangka - i
        else:
            return

def reformat(a):
    if (len(a)) < 4: #masih bisa kalo len saja
        for i in range(1, len(a), 2):
            a.insert(i," + ")
    else:
        tambahan = (len(a) - 4) #jadi kalo udh lebih dari 3 operand tuh musti nambah gitu terus menerus
        for i in range(1, len(a)+tambahan, 2):
            a.insert(i," + ")
    a.insert(len(a)-1, " == ") #ngapus ==
    #print(a)

    #list to string
    gabungan = ""  #string kosong
    for isi in a: #ya nge traversal di a
        gabungan += isi
    #print(gabungan) 
    return gabungan
    
def hasilakhirnya(katabersih):
    global banyakpercobaan
    banyakpercobaan = 0
    count = 0
    semuahuruf = set(''.join(katabersih)) # semua huruf yang ada di situ, at this point bentuknya masih set gitu
    hurufpertama = set(w[0] for w in katabersih) # nyari huruf pertamanya naon
    semuahuruf = ''.join(hurufpertama) + ''.join(semuahuruf - hurufpertama) #diambil dulu huruf pertamanya baru sisanya ditulis, disini 'semua huruf' udh string gitu ngurut dari huruf pertama muncul baru yang akhir
    n = len(hurufpertama) #banyak huruf bertama
    z = reformat(katabersih) #biar bentuknya kek + ==
    for a in permutasi('0123456789', len(semuahuruf)): #nyobain angka dari 0-9, nyocokinnya sebanyak huruf yang tersedia
        if '0' not in a[:n]: #huruf pertama nda boleh 0
            nani = str.maketrans(semuahuruf, ''.join(a))
            hasilkombinasi = z.translate(nani)
             #untuk menghitung brp kali sampe ketemu
            if eval(hasilkombinasi):
                print(hasilkombinasi)
                banyakpercobaan = count + 0 #dipisah antara perhitungan dan hasil akhir karena kalo pake perhitungan saja, jadinya nambah teruswalaupun udah di stop
            else:
                count += 1
    print("\n")                       

#main programmmmmmmm

bacanamafile = input("Masukkan nama file (cukup tuliskan nama file tanpa extension): ")
print("\n")
#bacanamafile = "txt2"

#baca doang dan ngeprint yang dibaca
bacafilejadiarray(bacanamafile)

for i in range(len(baris)):
    print(baris[i])
print("\n")

start_time = time.time() #setelah input file mulai itung waktu

#proses bersihin file, dari baca file sampe berisihin + sama - nya
bersihinplusstrip(baris)

#ngecek array yang baru
#print(len(arraybersih))
#print(arraybersih)
#print('----------sampe sini ok yah ngecek array baru----------\n')

#ini baru solvingnya
hasilakhirnya(arraybersih)
#reformat(arraybersih)
waktu = time.time() - start_time
print("Membutuhkan waktu: %s detik." % (round(waktu, 3)))
print("Membutuhkan %s percobaan.\n" % banyakpercobaan)
