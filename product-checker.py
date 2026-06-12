# 1. Databaza e produkteve të disponueshme (Kodi: Çmimi)
# Mund të shtoni ose ndryshoni kodet dhe çmimet këtu
produktet_ne_magazine = {
    "101": 1.50,  # P.sh. Ujë
    "102": 2.30,  # P.sh. Kafe
    "103": 0.80,  # P.sh. Çokollatë
    "104": 4.50,  # P.sh. Vaj
    "105": 1.20   # P.sh. Qumësht
}

def skano_produktet():
    shuma_totale = 0.0
    produktet_e_skanuara = []

    print("=== SKANERI I PRODUKTEVE ===")
    print("Shtypni kodin e produktit për ta shtuar në faturë.")
    print("Shkruani 'STOP' për të përfunduar faturën dhe për të parë totalin.\n")
    
    # Shfaq produktet e disponueshme për lehtësi testimi
    print("Kodet e vlefshme në sistem:")
    for kodi, cmimi in produktet_ne_magazine.items():
        print(f" -> Kodi: {kodi} (Çmimi: {cmimi:.2f} €)")
    print("-" * 40)

    while True:
        kodi_hyrje = input("Skano kodin (ose 'STOP'): ").strip()
        
        # Kushti për të ndaluar skanimin
        if kodi_hyrje.upper() == "STOP":
            break
            
        # 2. Verifikimi nëse kodi është i saktë (ekziston në magazinë)
        if kodi_hyrje in produktet_ne_magazine:
            cmimi_produktit = produktet_ne_magazine[kodi_hyrje]
            shuma_totale += cmimi_produktit
            produktet_e_skanuara.append((kodi_hyrje, cmimi_produktit))
            print(f"Produkti u shtua! Çmimi: {cmimi_produktit:.2f} € | Totali aktual: {shuma_totale:.2f} €")
        else:
            print("Gabim: Ky kod nuk ekziston në sistem! Ju lutem provoni përsëri.")
        print("-" * 30)

    # 3. Afishimi i faturës përfundimtare
    print("\n================ FATURA PËRFUNDIMTARE ================")
    if not produktet_e_skanuara:
        print("Nuk u skanua asnjë produkt.")
    else:
        print(f"Totali i produkteve të blera: {len(produktet_e_skanuara)}")
        print("-" * 46)
        for i, (kodi, cmimi) in enumerate(produktet_e_skanuara, 1):
            print(f"{i}. Produkti [{kodi}] -> {cmimi:.2f} €")
        print("-" * 46)
        print(f"SHUMA TOTALE PËR TË PAGUAR: {shuma_totale:.2f} €")
    print("======================================================")

# Ekzekutimi i programit
skano_produktet()
