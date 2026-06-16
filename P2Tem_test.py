import sys
import os
import pathlib

class MockLabel:
    """Klasa symulująca widget tekstowy z interfejsu"""
    def __init__(self):
        self.text = ""
        
    def config(self, text):
        self.text = text
        
    def setText(self, text):
        self.text = text

print("=" * 50)
print("  AUTOMATYCZNY TEST INTEGRACYJNY - TEMAT 10")
print("=" * 50)

try:
    # 1. Sprawdzenie obecności wymaganych plików
    current_dir = pathlib.Path(__file__).parent
    script_path = current_dir / "P2Tem10.py"
    data_path = current_dir / "P2Tem10_dane.xlsx"
    
    if not script_path.exists():
        raise FileNotFoundError("Brak pliku kodu źródłowego: P2Tem10.py")
    if not data_path.exists():
        raise FileNotFoundError("Brak pliku z danymi: P2Tem10_dane.xlsx")
        
    # 2. Dynamiczny import modułu
    print("[1/3] Importowanie modułu P2Tem10...")
    import P2Tem10
    
    # 3. Przygotowanie makiety labela i uruchomienie funkcji eXecute
    print("[2/3] Uruchamianie funkcji eXecute()...")
    mock_label = MockLabel()
    P2Tem10.eXecute(None, mock_label)
    
    # 4. Wyświetlenie wyprodukowanego wyniku
    print("[3/3] Pobieranie wyników z makiety interfejsu...\n")
    print(mock_label.text)
    print("=" * 50)
    print("STATUS: TEST ZAKOŃCZONY SUKCESEM!")
    print("=" * 50)

except Exception as e:
    print(f"\n[BŁĄD TESTU]: {str(e)}")
    print("=" * 50)

input("\nWciśnij ENTER, aby zamknąć to okno...")