import numpy as np
import time

# Anzahl der Datenpunkte
n = 300

# Startzeitpunkt (Unix Timestamp für heute)
start_timestamp = int(time.time())

# Zeitintervall in Sekunden (1 Tag in Sekunden)
time_interval = 86400  # Tägliche Daten

# Saisonale Schwankungen und Trend für die Geschwindigkeit
season_length = 365  # Annahme: 365 Tage im Jahr für saisonale Schwankungen
trend_slope = 0.05  # Geschwindigkeit steigt pro Tag um 0.05

# Generiere Zeitstempel
timestamps = np.array([start_timestamp + i * time_interval for i in range(n)])

# Generiere Geschwindigkeiten mit saisonalem Muster und Trend
seasonal_effect = 10 * np.sin(np.linspace(0, 2 * np.pi * n / season_length, n))  # Sinuswellenmuster
trend_effect = np.linspace(0, trend_slope * n, n)
speeds = 30 + seasonal_effect + trend_effect + np.random.normal(0, 2, n)  # Basisgeschwindigkeit von 30

# FIN und Ort sind konstant
fin = "F1000001"
ort = "Stuttgart"

# Erstelle eine Liste von Dictionaries für die Datensätze
data = [{"fin": fin, "zeit": int(ts), "geschwindigkeit": int(speed), "ort": ort} for ts, speed in zip(timestamps, speeds)]

# Zeige die ersten 5 Datensätze zur Überprüfung
data[:5]
