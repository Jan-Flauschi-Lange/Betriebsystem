import os
import time
import subprocess
import sys

def show_logo():
    # Dein Hamster-Logo als ASCII-Art (Text-basierte Statik)
    # Repräsentiert die visuelle Grenze deines Systems nach Wittgenstein
    logo = r"""
    ##################################################
    #               FLAUSCHI OS v2.0                 #
    ##################################################
    #                                                #
    #          _ ___                ___ _            #
    #         / |   \              /   | \           #
    #         | |    \____________/    | |           #
    #         | |     /          \     | |           #
    #         \  \___|   O    O    |___/  /          #
    #          \_____|      __      |_____/          #
    #                |     /  \     |                #
    #                |     \__/     |                #
    #                 \____________/                 #
    #                                                #
    # [HOMÖOSTASE AKTIVIERT]        [IMPULS: 0.42]   #
    ##################################################
    """
    # Bildschirm leeren für sauberen Boot-Vorgang
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

def check_statik():
    # Die Kern-Metriken deiner Thesis (Kapitel 161)
    impuls = 0.42
    pol_abstand = 0.4174
    print(f"\n[IMPULS]: {impuls}")
    print(f"[STATUS]: STABIL (Homöostase n. Walter Cannon)")
    print(f"[POL-ABSTAND]: {pol_abstand}")

def launch_program(path):
    # Dies ist die 0+/-X Kopplung: Dein OS startet das Programm
    print(f"\n[INFO] Filterung durch 0+/-X Kopplung: {path}")
    try:
        # Führt Programme innerhalb deines Systems aus (Subprocess-Management)
        subprocess.Popen(path, shell=True)
        print("[SUCCESS] Programm läuft stabil in der Statik-Membran.")
    except Exception as e:
        print(f"[ERROR] Statik-Bruch bei Injektion: {e}")

def main():
    # Setzt die Konsolenfarbe auf das Flauschi-Blau/Türkis
    os.system('color 0B') 
    show_logo()
    
    while True:
        print("\n" + "="*50)
        print(" FLAUSCHI OS - SYSTEM-ÜBERWACHUNG (CORE)")
        print("="*50)
        print("1. Statik-Metrik prüfen (Echtzeit)")
        print("2. Programm/ROM injizieren (Global Hook)")
        print("3. Philosophie-Check (Spinoza/Wittgenstein)")
        print("4. System-Shutdown (Statik sichern)")
        
        wahl = input("\nEingabe > ")
        
        if wahl == "1":
            check_statik()
        elif wahl == "2":
            path = input("Pfad zur .exe oder Name (z.B. notepad): ")
            launch_program(path)
        elif wahl == "3":
            # Konsistenzprüfung nach Baruch de Spinoza (fett markiert)
            print("\n[SPINOZA]: Die Substanz ist eine Einheit.")
            print("[WITTGENSTEIN]: Die Welt ist alles, was der Fall ist.")
            time.sleep(2)
        elif wahl == "4":
            print("[INFO] Statik gesichert. Kontrolliertes Ende.")
            break
        else:
            print("[WARNUNG] Ungültiger Impuls - Bereich verlassen!")

if __name__ == "__main__":
    main()
