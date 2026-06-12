import requests

def verifiko_isbn_lokal(isbn):
    """Verifikon matematikisht strukturën e një kodi ISBN-10 ose ISBN-13."""
    # Pastrojmë kodin nga vijat ndarëse ose hapësirat
    isbn = isbn.replace("-", "").replace(" ", "").strip()
    
    # --- Kontrolli për ISBN-10 ---
    if len(isbn) == 10:
        shuma = 0
        for i in range(9):
            if not isbn[i].isdigit():
                return False
            shuma += int(isbn[i]) * (10 - i)
        
        # Shifra e fundit mund të jetë edhe 'X' (që vlen 10)
        shifra_fundit = isbn[9].upper()
        if shifra_fundit == 'X':
            shuma += 10
        elif shifra_fundit.isdigit():
            shuma += int(shifra_fundit)
        else:
            return False
            
        return shuma % 11 == 0

    # --- Kontrolli për ISBN-13 ---
    elif len(isbn) == 13:
        if not isbn.isdigit():
            return False
        shuma = 0
        for i in range(13):
            # Shumëzohet me 1 pozicionet tek, dhe me 3 pozicionet çift
            pesha = 1 if i % 2 == 0 else 3
            shuma += int(isbn[i]) * pesha
            
        return shuma % 10 == 0

    else:
        return False

def kerko_librin_online(isbn):
    """Kërkon në Google Books API nëse kodi është i regjistruar."""
    isbn_paster = isbn.replace("-", "").replace(" ", "").strip()
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn_paster}"
    
    try:
        pergjigjja = requests.get(url, timeout=5)
        te_dhenat = pergjigjja.json()
        
        # Nëse 'totalItems' është më i madh se 0, libri ekziston
        if "totalItems" in te_dhenat and te_dhenat["totalItems"] > 0:
            infot_e_librit = te_dhenat["items"][0]["volumeInfo"]
            titulli = infot_e_librit.get("title", "Titulli i panjohur")
            autoret = ", ".join(infot_e_librit.get("authors", ["Autor i panjohur"]))
            viti = infot_e_librit.get("publishedDate", "Viti i panjohur")
            
            return True, f"'{titulli}' nga {autoret} ({viti})"
        else:
            return False, "Libri nuk u gjet në databazën globale."
    except requests.exceptions.RequestException:
        return False, "Gabim në lidhjen me internetin për verifikimin online."

# --- PROGRAMI KRYESOR ---
print("=== VERIFIKUESI I LIBRIT (ISBN) ===")
isbn_hyrje = input("Vendosni kodin ISBN (p.sh. 9780132350884 ose 0132350882): ")

# Hapi 1: Kontrolli i strukturës matematike
if verifiko_isbn_lokal(isbn_hyrje):
    print("Formati i kodit ISBN është matematikisht i saktë.")
    print("Duke kërkuar në databazën globale të librave...")
    
    # Hapi 2: Kontrolli live në internet
    ekziston, mesazhi = kerko_librin_online(isbn_hyrje)
    if ekziston:
        print("LIBRI ËSHTË I REGJISTRUAR!")
        print(mesazhi)
    else:
        print(f"{mesazhi}")
else:
    print("Kodi ISBN nuk është i saktë! Kontrolloni shifrat ose formatin.")
