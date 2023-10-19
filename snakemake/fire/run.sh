#gets data from google drive
wget -O Argrofood_co2_emission.csv 'https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr'

#his example: gets data for Afghanistan (using get_data.py) and makes historgram (using hist.py)
python get_data.py Argrofood_co2_emission.csv Afghanistan Afghanistan.txt
python hist.py Afghanistan.txt Afghanistan.png Afghanistan Fires Freq.