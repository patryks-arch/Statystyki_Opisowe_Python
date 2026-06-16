# Statystyki_Opisowe_Python

Aplikacja kliencka (moduł) napisana w języku Python, przeznaczona do automatycznego wyznaczania podstawowych statystyk opisowych z plików arkusza kalkulacyjnego (`.xlsx`). Projekt został przygotowany jako zadanie zaliczeniowe (Projekt P2) z przedmiotu *Narzędzia Programistyczne 2*.

## 📋 Spis treści
- [Funkcje aplikacji](#-funkcje-aplikacji)
- [Struktura danych wejściowych](#-struktura-danych-wejściowych)
- [Wymagania systemowe](#-wymagania-systemowe)
- [Instalacja i uruchomienie](#-instalacja-i-uruchomienie)
- [Struktura plików projektu](#-struktura-plików-projektu)
- [Autorzy](#-autorzy)

## 🚀 Funkcje aplikacji
Moduł automatycznie przetwarza dane liczbowe i generuje sformatowany raport zawierający:
- **Średnią arytmetyczną**
- **Medianę** (wartość środkową)
- **Odchylenie standardowe** (wyznaczane ze wzoru próbkowego)
- **Rozstęp danych** (różnica między wartością maksymalną a minimalną)

Program posiada wbudowane mechanizmy odporności na błędy: automatycznie ignoruje puste rekordy oraz konwertuje błędne wpisy tekstowe na wartości liczbowe przy użyciu bezpiecznej koercji typów.

## 📊 Struktura danych wejściowych
Program domyślnie poszukuje pliku z danymi testowymi o nazwie `P2Tem10_dodatki.xlsx`. 
- Plik musi znajdować się w tym samym katalogu co skrypt.
- Pierwsza kolumna arkusza (`A1`) **musi** posiadać nagłówek o nazwie **`Wartosci`**.
- Dane liczbowe powinny być umieszczone w kolumnie bezpośrednio pod nagłówkiem (`A2`, `A3`, `A4`...).

## 💻 Wymagania systemowe
Do poprawnego działania aplikacji wymagany jest interpreter języka **Python w wersji 3.8 lub nowszej** oraz następujące biblioteki zewnętrzne:
- `pandas`
- `openpyxl` (niezbędna do obsługi plików `.xlsx` przez pandas)

## 🛠️ Instalacja i uruchomienie

1. **Sklonuj repozytorium:**
   ```bash
   git clone [https://github.com/TWÓJ-LOGIN-GITHUB/NAZWA-REPOZYTORIUM.git](https://github.com/TWÓJ-LOGIN-GITHUB/NAZWA-REPOZYTORIUM.git)
   cd NAZWA-REPOZYTORIUM
