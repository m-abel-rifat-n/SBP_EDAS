import numpy as np
import pandas as pd

# Instansiasi data kriteria dan bobot
kriteria = ['Luas Tanah', 'Harga', 'Tipe', 'Sumber Air', 'Kamar Tidur', 'Kamar Mandi', 'Pos Satpam', 'Lokasi']
bobot = [0.2904, 0.2133, 0.1708, 0.0441, 0.1399, 0.0293, 0.0624, 0.0498]

# Matriks keputusan
alternatif = {
    'A1': [7, 7, 9, 7, 1, 9, 1, 6],
    'A2': [4, 3, 5, 3, 3, 10, 7, 4],
    'A3': [5, 5, 7, 4, 9, 2, 6, 1],
    'A4': [9, 5, 10, 9, 7, 8, 6, 7],
    'A5': [10, 1, 9, 2, 10, 6, 10, 2],
    'A6': [6, 7, 2, 7, 10, 2, 8, 7],
    'A7': [10, 9, 10, 2, 6, 7, 10, 4],
    'A8': [7, 6, 6, 4, 7, 2, 3, 9],
    'A9': [4, 9, 9, 1, 6, 1, 6, 1],
    'A10': [9, 8, 2, 4, 5, 3, 2, 5],
    'A11': [4, 4, 2, 5, 4, 10, 6, 5],
    'A12': [10, 6, 9, 9, 10, 10, 2, 6],
    'A13': [6, 8, 8, 5, 4, 9, 2, 3],
    'A14': [8, 6, 3, 3, 6, 7, 8, 7],
    'A15': [4, 9, 3, 5, 10, 5, 10, 6],
    'A16': [6, 2, 7, 6, 5, 6, 5, 9],
    'A17': [8, 4, 1, 8, 3, 10, 7, 4],
    'A18': [4, 1, 8, 5, 10, 5, 2, 6],
    'A19': [9, 8, 9, 5, 1, 3, 10, 6],
    'A20': [3, 1, 10, 4, 7, 5, 10, 8]
}

# Menghitung solusi rata-rata (Average Solution, AV)
def calculate_average_solution(df):
    return df.mean()

# Menghitung jarak positif (PDA) dan negatif (NDA) dari rata-rata untuk setiap alternatif.
def calculate_pda_nda(df, mean_df):
    P = df - mean_df
    N = mean_df - df
    return P, N

# Menghitung jumlah terbobot dari PDA (SP) dan NDA (SN) berdasarkan bobot kriteriaaa.
def calculate_sp_sn(P, N, bobot):
    SP = P * bobot
    SN = N * bobot
    return SP.sum(axis=1), SN.sum(axis=1)

# Normalisasi nilai SP / SN (NSP / NSN)
def normalize_sp_sn(SP, SN):
    NSP = SP / (SP.max() - SP.min())
    NSN = SN / (SN.max() - SN.min())
    return NSP, NSN

# Menghitung nilai skor penilaian (AS)
def calculate_as(NSP, NSN):
    return 0.5 * NSP + 0.5 * (1 - NSN)

# Melakukan penentuan peringkat berdasarkan nilai AS.
def rank_alternatives(AS):
    return AS.sort_values(ascending=False)

# Menghitung Combination Factor (CF)
def calculate_cf(df, bobot):
    CF = df.mul(bobot, axis=1).sum(axis=1)
    return CF

# Menampilkan menu
def display_menu():
    print("\nPilihan Menu:")
    print("1. Menghitung solusi rata-rata (AV)")
    print("2. Mengukur jarak positif / negatif dari rata-rata (PDA / NDA)")
    print("3. Menentukan jumlah bobot dari PDA / NDA (SP / SN)")
    print("4. Menormalisasi nilai SP / SN (NSP / NSN)")
    print("5. Mengkalkulasi nilai skor penilaian (AS)")
    print("6. Menentukan peringkat")
    print("7. Menghitung Combination Factor (CF)")
    print("8. Keluar")

# Main function untuk membuat DataFrame dari dictionary alternatif dengan menggunakan pandas, Mengelola alur program sesuai pilihan pengguna.
def main():
    df = pd.DataFrame.from_dict(alternatif, orient='index', columns=kriteria)
    
    while True:
        display_menu()
        choice = input("Input: ")
        
        if choice == '1':
            mean_df = calculate_average_solution(df)
            print("Solusi Rata-rata (AV):")
            print(mean_df)
        
        elif choice == '2':
            mean_df = calculate_average_solution(df)
            P, N = calculate_pda_nda(df, mean_df)
            print("Jarak Positif (PDA):")
            print(P)
            print("Jarak Negatif (NDA):")
            print(N)
        
        elif choice == '3':
            mean_df = calculate_average_solution(df)
            P, N = calculate_pda_nda(df, mean_df)
            SP, SN = calculate_sp_sn(P, N, bobot)
            print("Jumlah Terbobot dari PDA (SP):")
            print(SP)
            print("Jumlah Terbobot dari NDA (SN):")
            print(SN)
        
        elif choice == '4':
            mean_df = calculate_average_solution(df)
            P, N = calculate_pda_nda(df, mean_df)
            SP, SN = calculate_sp_sn(P, N, bobot)
            NSP, NSN = normalize_sp_sn(SP, SN)
            print("Normalisasi SP (NSP):")
            print(NSP)
            print("Normalisasi SN (NSN):")
            print(NSN)
        
        elif choice == '5':
            mean_df = calculate_average_solution(df)
            P, N = calculate_pda_nda(df, mean_df)
            SP, SN = calculate_sp_sn(P, N, bobot)
            NSP, NSN = normalize_sp_sn(SP, SN)
            AS = calculate_as(NSP, NSN)
            print("Nilai Skor Penilaian (AS):")
            print(AS)
        
        elif choice == '6':
            mean_df = calculate_average_solution(df)
            P, N = calculate_pda_nda(df, mean_df)
            SP, SN = calculate_sp_sn(P, N, bobot)
            NSP, NSN = normalize_sp_sn(SP, SN)
            AS = calculate_as(NSP, NSN)
            ranking = rank_alternatives(AS)
            print("Perangkingan:")
            print(ranking)
        
        elif choice == '7':
            CF = calculate_cf(df, bobot)
            print("Combination Factor (CF):")
            print(CF)
        
        elif choice == '8':
            print("Keluar dari program.")
            break
        
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
