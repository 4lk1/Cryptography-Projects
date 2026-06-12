def valido_iban(iban):
    # 1. Pastro hapsirat dhe ktheji shkronjat në kapitale
    iban = iban.replace(" ", "").upper()
    
    # Një IBAN nuk mund të jetë më i shkurtër se 5 karaktere dhe më i gjatë se 34
    if len(iban) < 5 or len(iban) > 34:
        return False
        
    # 2. Rirregullo IBAN-in: Merr 4 karakteret e para dhe vendosi në fund
    rirregulluar = iban[4:] + iban[:4]
    
    # 3. Kthe shkronjat në numra (A=10, B=11, ..., Z=35)
    numri_konvertuar = ""
    for karakter in rirregulluar:
        if karakter.isdigit():
            numri_konvertuar += karakter
        elif karakter.isalpha():
            # Në ASCII, 'A' është 65. Duke i zbritur 55, 'A' bëhet 10.
            numri_konvertuar += str(ord(karakter) - 55)
        else:
            # Nëse ka karaktere të jashtëligjshme (si pika, viza, etj.)
            return False
            
    # 4. Llogarit mbetjen e pjesëtimit me 97 (MOD 97)
    # Nëse mbetja është 1, IBAN-i është i vlefshëm.
    return int(numri_konvertuar) % 97 == 1

# --- Shembull Përdorimi ---
print("--- KONTROLLUESI I IBAN ---")
iban_perdoruesit = input("Vendosni numrin IBAN: ")

if valido_iban(iban_perdoruesit):
    print("✅ IBAN-i është i vlefshëm!")
else:
    print("❌ IBAN-i NUK është i vlefshëm. Ju lutem kontrolloni shifrat.")
