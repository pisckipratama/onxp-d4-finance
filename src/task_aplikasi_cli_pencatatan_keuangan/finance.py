class MoneyTracker:
    def __init__(self):
        self.list_uang_masuk = []
        self.list_uang_keluar = []

    def uang_masuk(self, jumlah):
        self.list_uang_masuk.append(jumlah)
        return f"List uang masuk: {self.list_uang_masuk}"

    def uang_keluar(self, jumlah):
        if jumlah > self.cetak_uang_masuk():
            return "tidak bisa mengeluarkan uang, karena saldo kurang"
        else:
            self.list_uang_keluar.append(jumlah)
        
        return f"List uang keluar: {self.list_uang_keluar}"

    def cetak_uang_masuk(self):
        result = 0

        for count in self.list_uang_masuk:
            result += count

        return result

    def cetak_uang_keluar(self):
        result = 0

        for count in self.list_uang_keluar:
            result += count

        return result
    
    def cetak_saldo(self):
        return self.cetak_uang_masuk() - self.cetak_uang_keluar()

pencatat_keuangan = MoneyTracker()

print("*** SELAMAT DATANG DI APLIKASI PENCATATAN KEUANGAN CLI ***")

def main():
    choice = input("SILAHKAN PILIH MENU YANG ANDA INGINKAN [masuk/keluar/sum masuk/sum keluar/sum all]: ")

    if choice == 'masuk':
        jumlah = int(input("Masukkan jumlah uang yang ingin anda masukkan: "))
        print(pencatat_keuangan.uang_masuk(jumlah))
    elif choice == 'keluar':
        jumlah = int(input("Masukkan jumlah uang yang ingin anda keluarkan: "))
        print(pencatat_keuangan.uang_keluar(jumlah))
    elif choice == 'sum masuk':
        print(f"Jumlah uang masuk Anda: {pencatat_keuangan.cetak_uang_masuk()}")
    elif choice == 'sum keluar':
        print(f"Jumlah uang keluar Anda: {pencatat_keuangan.cetak_uang_keluar()}")
    elif choice == 'sum all':
        print(f"Jumlah saldo Anda: {pencatat_keuangan.cetak_saldo()}")
    else:
        print("That is not a valid input.")


if __name__=='__main__':
    choice2=""
    while choice2 != 'quit':
        main()
        choice2=str(input('Apakah anda ingin keluar?: [y/n] '))
        if choice2=='y' or choice2=='ya' or choice2=='yes':
            choice2='quit'
        