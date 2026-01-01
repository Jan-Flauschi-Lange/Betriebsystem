# ======================================================
# ZERO-OS: DIE LOGISCHE EXEKUTIVE (VOLLSTÄNDIGE KOPPLUNG)
# Architektur: Der Mittelpunkt des Universums
# Basierend auf: 0±X Theorie & Homöostase nach Cannon
# ======================================================

import time
import random

class StaticKernel:
    def __init__(self):
        self.target_zero = 0.0
        self.tolerance_x = 1.0  # Kapitel 161 
        self.current_state = 0.0
        self.recovery_rate = -0.1 # Homöostase nach Cannon 

    def process_impulse(self, impulse):
        # Die mathematische Rückstellkraft zur Stabilisierung 
        recovery = self.recovery_rate * (self.current_state - self.target_zero)
        self.current_state += impulse + recovery
        
        # Prüfung der Statik nach Kapitel 161 
        if abs(self.current_state - self.target_zero) > self.tolerance_x:
            status = "INSTABIL - REGENERATION EINGELEITET"
            self.current_state = self.target_zero # Notfall-Stabilisierung
        else:
            status = "STABIL"
        return status

def user_interface():
    kernel = StaticKernel()
    print("========================================")
    print("Zero-OS Logik-Kern aktiviert.")
    print("Systemzustand: Statik gesichert.")
    print("========================================\n")

    while True:
        print("1. Statik-Status prüfen (Echtzeit-Überwachung)")
        print("2. ROM / Programm injizieren (0±X Kopplung)")
        print("3. System-Stabilität nach Kapitel 161")
        print("4. Beenden")
        
        wahl = input("\nWahl der Statik: ")
        
        if wahl == "1":
            # Simuliert einen Lebens-Impuls (X) 
            impulse = random.uniform(-0.5, 0.5)
            status = kernel.process_impulse(impulse)
            print(f"\n[IMPULS]: {impulse:.2f}")
            print(f"[STATUS]: {status}")
            print(f"[POL-ABSTAND]: {kernel.current_state:.4f}\n")
            
        elif wahl == "2":
            file_path = input("Dateipfad der ROM: ")
            print(f"\nInitialisiere {file_path} im statischen Raum...")
            time.sleep(1) # Simulation der Kopplung
            print("Kopplung abgeschlossen. Programm läuft im 0±X Filter.\n")
            
        elif wahl == "3":
            print(f"\nKonfigurations-Parameter (Kapitel 161):")
            print(f"Nullpunkt: {kernel.target_zero}")
            print(f"Toleranz X: {kernel.tolerance_x}")
            print(f"Rückstellkraft: {kernel.recovery_rate}\n")
            
        elif wahl == "4":
            print("System wird im statischen Zustand versiegelt. Auf Wiedersehen.")
            break
        else:
            print("Ungültiger Vektor. Bitte wählen Sie 1, 2 oder 3.")

if __name__ == "__main__":
    user_interface()
