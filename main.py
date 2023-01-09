import re
import convert_cyk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

not_accepted = ['K','S','P','O','Pel','Ket','NP','VP','AdjP','PP']
all_alphabet = convert_cyk.get_set_of_production()
all_kata = []
for key,value in all_alphabet.items():
    if(key not in not_accepted):
        for val in value:
            all_kata.append(val)

window = tk.Tk()
 
window.configure(bg="white")
window.geometry("520x520")
window.resizable(False, False)
window.title("Tugas Final Project")

frame = ttk.Frame(window)
frame.pack(padx=20, pady=20, fill="x", expand=True)

label_entry = ttk.Label(frame, text="Masukkan Kalimat Yang Ingin Diuji")
label_entry.pack(padx=10, fill="x", expand=True)

kalimat = tk.StringVar()
entry = ttk.Entry(frame, textvariable=kalimat)
entry.pack(padx=10, fill="x", expand=True)

def event():
    cek_kalimat = kalimat.get().lower()
    cek_kata = cek_kalimat.split()
    tidak_ketemu = 0
    kata_tidak_ketemu = []
    for kata in cek_kata:
        if(kata not in all_kata):
            tidak_ketemu=1
            kata_tidak_ketemu.append(kata)
    if(tidak_ketemu==1):
        kata = ','.join(kata_tidak_ketemu)
        showinfo(title=f"Error!", message=f"{kata} tidak ditemukan!")
        return
    if(convert_cyk.is_accepted(cek_kalimat)):
        showinfo(title="Diterima!", message="Kalimat Baku")
    else:
        showinfo(title="Ditolak.", message="Kalimat Tidak Baku")
    # if general.check_alphabet(kalimat.get().lower().split()) == False:
    #     showinfo(title="Notifikasi", message="Kalimat Tidak Valid Karena Terdapat Kata Yang Belum Ada Di Data File")
    # elif process.table_filling_process(kalimat.get().lower().split()) == True:
    #     showinfo(title="Notifikasi", message="Kalimat Diterima Karena Sesuai Dengan Pola Dan Persyaratan")
    # else:
    #     showinfo(title="Notifikasi", message="Kalimat Ditolak Karena Tidak Sesuai Dengan Pola Dan Persyaratan")

button = ttk.Button(frame, text="Cek", command=event)
button.pack(padx=10, pady=10, fill="x", expand=True)

window.mainloop()


#CEK ALL
# with open('C:\\NGODING\\Python\\Final-Project-TBO-bakcup-main\\input_test.txt','r') as f:
#     listinput = f.readlines()
#     ditrima=0
#     for x,value in enumerate(listinput):
#         if(value[0]==' '):
#             value= value[1:len(value)]
#         clean = re.sub('\n','',value.lower())
#         if(clean[len(clean)-1]=='.'):
#             clean=clean[0:len(clean)-1]
#         if(convert_cyk.is_accepted(clean.lower())):
#             ditrima+=1
#             print(f'{x} Valid')
#         else:
#             print(f'{x} Tidak Valid')
#             # if(process.table_filling_process(clean.lower().split()) == True):
#             #     print(f'{x+1:>2}. Diterima',clean)
#             #     hasil = process.print_table(clean.lower().split())
#             #     print(f'{hasil}')
#             #     ditrima+=1
#             # else:
#             #     print(f'{x+1:>2}. Ditolak \n',clean)
#             #     hasil = process.print_table(clean.lower().split())
#             #     print(f'{hasil}')
# print(f'{ditrima}/{len(listinput)}')
# kata = 'Baju baru itu sangat elok'
# print('Diterima' if convert_cyk.is_accepted(kata) else 'Ditolak')