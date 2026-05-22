v2.0.1 - 2026-05-22

**KiCad** :

Project conversion to KiCad V9

**Schematic** :

Updated hierarchical labels to net labels, default footprints
Updated LED resistors (R5 -> R10) from 270K to 330K like toggle switches (MCP)
Updated bloc with line dots and title diagrams
Added Rasperry Pi Pico modified symbol (for vertical headers)
Updated BOM document

**PCB** :

Added some silkscreen informations (LEDs, encoders...)

**AISLER** :

Removed simple quotes in AISLER DRC (A.Soldermask_Margin_Override == null) since KiCad >= V9
Added mention in README.md to change the plugin PushForKiCad default repository
