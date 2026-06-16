import pathlib
import pandas as pd

def calculate_descriptive_stats(file_path: pathlib.Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"Brak pliku '{file_path.name}' w katalogu.")
        
    # wczytanie arkusza
    if file_path.suffix in ['.xlsx', '.xls']:
        df = pd.read_excel(file_path)
    else:
        df = pd.read_csv(file_path)
        
    if df.empty:
        raise ValueError("Plik z danymi jest pusty.")
        
    # szukamy kolumny 'Wartosci', a jak nie ma, to bierzemy pierwsza
    if 'Wartosci' in df.columns:
        col_name = 'Wartosci'
    else:
        col_name = df.columns[0]
        
    # czyszczenie danych z brakujacych wartosci i konwersja na liczby
    data = pd.to_numeric(df[col_name], errors='coerce').dropna()
    
    if data.empty:
        raise ValueError(f"Kolumna '{col_name}' nie zawiera poprawnych liczb.")
        
    # statystyki opisowe
    mean_val = data.mean()
    median_val = data.median()
    std_val = data.std()
    range_val = data.max() - data.min()
    
    # gotowy tekst na etykiete
    wynik = (
        f"ZADANIE 10 - STATYSTYKI OPISOWE\n"
        f"Analizowana kolumna: {col_name}\n"
        f"---------------------------------\n"
        f"Średnia: {mean_val:.4f}\n"
        f"Mediana: {median_val:.4f}\n"
        f"Odchylenie std.: {std_val:.4f}\n"
        f"Rozstęp: {range_val:.4f}"
    )
    return wynik

def eXecute(win, Mlabel):
    try:
        # Szukanie pliku o nowej nazwie obok skryptu
        current_dir = pathlib.Path(__file__).parent
        file_path = current_dir / "P2Tem10_dane.xlsx"
        
        raport = calculate_descriptive_stats(file_path)
        
        if hasattr(Mlabel, "config"):
            Mlabel.config(text=raport)
        elif hasattr(Mlabel, "setText"):
            Mlabel.setText(raport)
        else:
            Mlabel["text"] = raport
            
    except Exception as e:
        error_msg = f"Błąd T10: {str(e)}"
        if hasattr(Mlabel, "config"):
            Mlabel.config(text=error_msg)
        else:
            Mlabel["text"] = error_msg