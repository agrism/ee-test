# -*- coding: utf-8 -*-
"""
Builder script to generate the complete Latvian translation and modern interactive HTML
for the Estonian procurement "Veebide ja infosüsteemide analüüsi, arendus- ning hooldustööd 2026 - 2029" (Ref 315313).
"""
import json, os

# Load CFR translated data
with open("cfr_translated_complete.json", "r", encoding="utf-8") as f:
    cfr_items = json.load(f)

# Load raw texts for cross-referencing
with open("extracted_raw.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

print("Building procurement application...")
