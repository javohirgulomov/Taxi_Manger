class Mahsulot:
    def __init__(self, nom, narx, miqdor):
        self.nom = nom
        self.narx = narx
        self.miqdor = miqdor

    def __str__(self):
        return f"{self.nom.ljust(15)} | Narx: {self.narx} so'm | Omborda: {self.miqdor} dona"


class User:
    def __init__(self, ism, parol, balans):
        self.ism = ism
        self.parol = parol
        self.balans = balans
        self.savat = {}
        self.tarix = []

    def savatga_qoshish(self, bozor, mahsulot_nomi, miqdor):
        mahsulot = bozor.mahsulotni_olish(mahsulot_nomi)

        if not mahsulot:
            print(f" '{mahsulot_nomi}' topilmadi.")
            return

        if mahsulot.miqdor < miqdor:
            print(f" Omborda yetarli emas! Faqat {mahsulot.miqdor} dona bor.")
            return

        eski_miqdor = self.savat.get(mahsulot_nomi, 0)
        yangi_miqdor = eski_miqdor + miqdor

        if yangi_miqdor <= 0:
            if mahsulot_nomi in self.savat:
                del self.savat[mahsulot_nomi]
                print(f" {mahsulot_nomi} savatdan olib tashlandi.")
        else:
            if yangi_miqdor > mahsulot.miqdor:
                print(f" Siz jami {yangi_miqdor} so'rayapsiz, lekin omborda {mahsulot.miqdor} bor.")
            else:
                self.savat[mahsulot_nomi] = yangi_miqdor
                print(f" Savat yangilandi: {mahsulot_nomi} -> {yangi_miqdor} dona.")

    def savatni_korish(self, bozor):
        print(f"\n {self.ism}ning SAVATCHASI ")
        jami_summa = 0
        if not self.savat:
            print("Savat bo'sh.")
        else:
            tozalanadiganlar = []
            for nom, soni in self.savat.items():
                mahsulot = bozor.mahsulotni_olish(nom)
                if not mahsulot:
                    tozalanadiganlar.append(nom)
                    continue

                summa = mahsulot.narx * soni
                jami_summa += summa
                print(f"- {nom}: {soni} dona x {mahsulot.narx} = {summa} so'm")

            for t in tozalanadiganlar:
                del self.savat[t]

            print(f"Jami to'lov: {jami_summa} so'm | Sizda bor: {self.balans} so'm")
        return jami_summa

    def tolov_qilish(self, bozor):
        jami_summa = self.savatni_korish(bozor)

        if jami_summa == 0:
            print(" Sotib olish uchun hech narsa yo'q.")
            return

        if self.balans < jami_summa:
            print(" Mablag' yetarli emas!")
            return

        tasdiq = input(f"To'lovni tasdiqlaysizmi? (ha/yo'q): ").lower()
        if tasdiq != 'ha':
            print("To'lov bekor qilindi.")
            return

        print("\n To'lov amalga oshirilmoqda...")
        for nom, soni in self.savat.items():
            mahsulot = bozor.mahsulotni_olish(nom)
            mahsulot.miqdor -= soni

            self.tarix.append(f" {nom} ({soni} dona) - {mahsulot.narx * soni} so'm")

        self.balans -= jami_summa
        bozor.budjet += jami_summa
        self.savat.clear()
        print(f" Xarid muvaffaqiyatli yakunlandi! Qoldiq balans: {self.balans} so'm")


class Admin:
    def __init__(self, ism, parol):
        self.ism = ism
        self.parol = parol

    def mahsulot_qoshish(self, bozor):
        nom = input("Mahsulot nomi: ")

        narx = float(input("Narxi: "))
        miqdor = int(input("Miqdori: "))

        mavjud = bozor.mahsulotni_olish(nom)
        if mavjud:
            mavjud.miqdor += miqdor
            mavjud.narx = narx
            print(f" {nom} yangilandi.")
        else:
            yangi_mahsulot = Mahsulot(nom, narx, miqdor)
            bozor.mahsulotlar.append(yangi_mahsulot)
            print(f" Yangi mahsulot qo'shildi: {nom}")

    def userni_korish(self, bozor):
        ism = input("Qaysi user tarixini ko'rmoqchisiz?: ")
        user = bozor.user_topish(ism)
        if user:
            print(f"\n {user.ism} Xarid Tarixi")
            if not user.tarix:
                print("Hali hech narsa sotib olmagan.")
            else:
                for yozuv in user.tarix:
                    print(yozuv)
        else:
            print(" Bunday user topilmadi.")


class BozorTizimi:
    def __init__(self):
        self.mahsulotlar = []
        self.users = {}
        self.admin = Admin("admin", "123")
        self.budjet = 1000000.0

        self.user_qoshish("user1", "111", 50000)
        self.user_qoshish("user2", "222", 100000)

        self.mahsulotlar.append(Mahsulot("Olma", 5000, 50))
        self.mahsulotlar.append(Mahsulot("Non", 3000, 100))
        self.mahsulotlar.append(Mahsulot("Sut", 12000, 20))

    def user_qoshish(self, ism, parol, balans):
        if ism in self.users:
            return False
        self.users[ism] = User(ism, parol, balans)
        return True

    def user_topish(self, ism):
        return self.users.get(ism)

    def mahsulotni_olish(self, nom):
        for m in self.mahsulotlar:
            if m.nom.lower() == nom.lower():
                return m
        return None

    def mahsulotlarni_korsatish(self):
        print("\n MARKET")
        for m in self.mahsulotlar:
            print(m)



def admin_menu(tizim):
    while True:
        print(f"\n ADMIN PANEL (Budjet: {tizim.budjet} so'm) ")
        print("1. Mahsulot qo'shish")
        print("2. Mahsulotlarni ko'rish")
        print("3. User tarixini ko'rish")
        print("4. Chiqish (Log out)")
        tanlov = input("Tanlov: ")

        if tanlov == '1':
            tizim.admin.mahsulot_qoshish(tizim)
        elif tanlov == '2':
            tizim.mahsulotlarni_korsatish()
        elif tanlov == '3':
            tizim.admin.userni_korish(tizim)
        elif tanlov == '4':
            break


def user_menu(tizim, user):
    while True:
        print(f"\n USER PANEL: {user.ism} (Balans: {user.balans}) ")
        print("1. Mahsulotlarni ko'rish")
        print("2. Savatga qo'shish")
        print("3. Savatni ko'rish ")
        print("4. Sotib olish (Checkout)")
        print("5. Chiqish (Log out)")
        tanlov = input("Tanlov: ")

        if tanlov == '1':
            tizim.mahsulotlarni_korsatish()
        elif tanlov == '2':
            tizim.mahsulotlarni_korsatish()
            nom = input("Mahsulot nomi: ")
            try:
                miqdor = int(input("Necha dona (yoki kg) qo'shasiz (Manfiy son ayiradi): "))
                user.savatga_qoshish(tizim, nom, miqdor)
            except ValueError:
                print("Raqam kiriting.")
        elif tanlov == '3':
            user.savatni_korish(tizim)
        elif tanlov == '4':
            user.tolov_qilish(tizim)
        elif tanlov == '5':
            print(f" Xayr  {user.ism} ")
            break



tizim = BozorTizimi()

while True:
    print("      SUPERMARKET      ")
    print("1. Kirish (Login)")
    print("2. Ro'yxatdan o'tish (Register)")
    print("3. Tizimni to'xtatish")

    buyruq = input("Tanlovni kiriting: ")

    if buyruq == '1':
        ism = input("Login (Ism): ")
        parol = input("Parol: ")

        if ism == tizim.admin.ism and parol == tizim.admin.parol:
            admin_menu(tizim)
        elif ism in tizim.users:
            user = tizim.users[ism]
            if user.parol == parol:
                user_menu(tizim, user)
            else:
                print(" Parol noto'g'ri!")
        else:
            print(" Bunday foydalanuvchi topilmadi.")

    elif buyruq == '2':
        print("\n RO'YXATDAN O'TISH ")
        yangi_ism = input("Yangi Login: ")
        if yangi_ism in tizim.users or yangi_ism == 'admin':
            print(" Bu nom band.")
            continue

        yangi_parol = input("Parol o'ylab toping: ")
        try:
            boshlangich_pul = float(input("Balansingizdagi pul (so'm): "))
            tizim.user_qoshish(yangi_ism, yangi_parol, boshlangich_pul)
            print(" Muvaffaqiyatli ro'yxatdan o'tdingiz! Endi kirishingiz mumkin.")
        except ValueError:
            print(" Balans raqam bo'lishi kerak.")

    elif buyruq == '3':
        print("Dastur to'xtatildi.")
        break

    else:
        print("Noto'g'ri buyruq.")