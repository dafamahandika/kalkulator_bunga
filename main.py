lanjut = True
while lanjut:
     
     print("\n KALKULATOR BUNGA: \n")
     print("1. BUNGA TUNGGAL\n")
     print("2. BUNGA MAJEMUK\n")
     print("3. KELUAR \n")
     menu = int(input("PILIH MENU: "))
     
     if menu == 1:
          print("\n BUNGA TUNGGAL \n")
          mo = int(input("MODAL: Rp. "))
          bo = int(input("BUNGA: "))
          p = int(input("PERIODE: "))
          ma = mo + ((mo * bo / 100) * p)
          print(f"\nMODAL: Rp. {mo:,}")
          print(f"BUNGA: {bo}%")
          print(f"PERIODE: {p}")
          print("\n")
          print("Ma = Mo + i")
          print(f"Ma = {mo} + (({mo} * {bo} / 100) * {p})")
          print(f"MODAL AKHIR: Rp. {ma:,}")
          print("\n PROGRAM SUCCES ! \n")

     elif menu == 2:
          print("\n BUNGA MAJEMUK \n")
          mo = int(input("MODAL: Rp. "))
          bo = int(input("BUNGA : "))
          p = int(input("PERIODE: "))
          print(f"\nMODAL: Rp. {mo}")
          print(f"BUNGA: {bo}%")
          print(f"PERIODE: {p} \n")
          
          bf = (1 + (bo / 100)) ** p 
          bp = (1 + (bo / 100)) ** -p 
          bfr = round(bf, 4) 
          bpr = round(bp, 4) 
          ma = mo * bfr
               
          print("\n FUTURE VALUE \n")
          print(f"Ma = Mo * (1 + i)^t")
          print(f"Ma = {mo} * (1 + {bo})^{p}")
          print(f"Ma = {mo} * {bfr}")
          print(f"Ma = Rp. {ma:,}")

          print("\n PRESENT VALUE \n")
          print(f"Mo = Ma * (1 + i)^-t")
          print(f"Mo = {mo} * (1 + {bo})^-{p}")
          print(f"Mo = {mo} * {bpr}")
          mo = mo * bpr
          print(f"Mo = Rp. {mo:,}")
          print("\nPROGRAM SUCCES !\n")

     else : 
          print("CREATED BY DM")
          lanjut = False
     