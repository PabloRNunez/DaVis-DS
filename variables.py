import pandas as pd

ds_a_min = pd.read_excel('excels/ds_armors_min.xlsx')
ds_a_max = pd.read_excel('excels/ds_armors_max.xlsx')
ds_a_min = pd.read_excel('excels/ds_weapons_min.xlsx')
ds_a_max = pd.read_excel('excels/ds_weapons_max.xlsx')
ds_a_min = pd.read_excel('excels/ds_shields_min.xlsx')
ds_a_max = pd.read_excel('excels/ds_shields_max.xlsx')


variables = [
    'set', 'name', 'level', 'position', 'poise', 'weight', 
    'phy_reduction', 'mag_reduction', 'fir_reduction', 'lig_reduction',
    'ble_resist', 'poi_resist', 'cur_resist', 
    'buffable','skill','damage_type',
    'stability', 'critical', 'bleed', 'poison', 'frost',
    'phy_damage', 'mag_damage', 'fir_damage', 'lig_damage', 'dar_damage', 'tot_damage',
    'str_bonus', 'dex_bonus', 'int_bonus', 'fai_bonus',
    'str_req', 'dex_req', 'int_req', 'fai_req',
    'class', 'upgrade_path', 'status_effect']

ft_variables = [
    'poise', 'weight', 
    'phy_reduction', 'mag_reduction', 'fir_reduction', 'lig_reduction',
    'ble_resist', 'poi_resist', 'cur_resist','bleed','poison','frost',
    'stability','critical',
    'phy_damage', 'mag_damage', 'fir_damage', 'lig_damage','dar_damage', 'tot_damage',
    'str_bonus', 'dex_bonus', 'int_bonus', 'fai_bonus',
    'str_req', 'dex_req', 'int_req', 'fai_req']
fl_variables = [
    'set', 'name', 'position',
    'class', 'upgrade_path', 'status_effect',
    'buffable','skill','damage_type']

cod_variables = [
    'str_bonus', 'dex_bonus', 'int_bonus', 'fai_bonus', 'level']
cn_variables = [
    'set', 'name', 'position',
    'class', 'upgrade_path', 'status_effect','buffable','damage_type','skill']
cc_variables = [
    'poise', 'weight', 
    'phy_reduction', 'mag_reduction', 'fir_reduction', 'lig_reduction',
    'ble_resist', 'poi_resist', 'cur_resist','bleed','poison','frost',
    'stability', 'critical',
    'phy_damage', 'mag_damage', 'fir_damage', 'lig_damage', 'dar_damage', 'tot_damage',
    'str_req', 'dex_req', 'int_req', 'fai_req']

ds1_up_d = {
    'Standard':'grey', 
    'Raw':'brown', 
    'Crystal':'purple', 
    'Magic':'blue', 
    'Enchanted':'darkblue', 
    'Divine':'green',
    'Occult':'darkgreen', 
    'Fire':'red', 
    'Chaos':'darkred', 
    'Lightning':'gold', 
    'Unique':'silver', 
    'Dragon':'orange'}
ds1_se_d = {
    '-':'grey', 
    'Bleed':'red', 
    'Poison':'green', 
    'Toxic':'darkgreen'}

ds1_a_d = {
    'set':'Set', 
    'name':'Name', 
    'position':'Position', 
    'poise':'Poise', 
    'weight':'Weight',
    'phy_reduction':'Physical Reduction', 
    'mag_reduction':'Magic Reduction',
    'fir_reduction':'Fire Reduction', 
    'lig_reduction':'Lightning Reduction',
    'ble_resist':'Bleed Resistance', 
    'poi_resist':'Poison Resistance', 
    'cur_resist':'Curse Resistance'}
ds1_w_d = {
    'name':'Name', 
    'level':'Level', 
    'class':'Class', 
    'stability':'Stability', 
    'weight':'Weight',
    'phy_damage':'Physical Damage', 
    'mag_damage':'Magic Damage', 
    'fir_damage':'Fire Damage', 
    'lig_damage':'Lightning Damage', 
    'tot_damage':'Total Damage',
    'upgrade_path':'Upgrade Path', 
    'status_effect':'Status Effect',
    'phy_reduction':'Physical Reduction', 
    'mag_reduction':'Magic Reduction',
    'fir_reduction':'Fire Reduction', 
    'lig_reduction':'Lightning Reduction',
    'str_bonus':'Strength Bonus', 
    'dex_bonus':'Dexterity Bonus',
    'int_bonus':'Intelligence Bonus', 
    'fai_bonus':'Faith Bonus',
    'str_req':'Strength Requirement', 
    'dex_req':'Dexterity Requirement',
    'int_req':'Intelligence Requirement', 
    'fai_req':'Faith Requirement'}
ds1_s_d = {
    'name':'Name', 
    'level':'Level', 
    'class':'Class', 
    'stability':'Stability', 
    'weight':'Weight',
    'phy_damage':'Physical Damage', 
    'mag_damage':'Magic Damage', 
    'fir_damage':'Fire Damage', 
    'lig_damage':'Lightning Damage', 
    'tot_damage':'Total Damage',
    'upgrade_path':'Upgrade Path',
    'phy_reduction':'Physical Reduction', 
    'mag_reduction':'Magic Reduction',
    'fir_reduction':'Fire Reduction', 
    'lig_reduction':'Lightning Reduction',
    'ble_resist':'Bleed Resistance', 
    'poi_resist':'Poison Resistance', 
    'cur_resist':'Curse Resistance',
    'str_bonus':'Strength Bonus', 
    'dex_bonus':'Dexterity Bonus',
    'int_bonus':'Intelligence Bonus', 
    'fai_bonus':'Faith Bonus',
    'str_req':'Strength Requirement', 
    'dex_req':'Dexterity Requirement',
    'int_req':'Intelligence Requirement', 
    'fai_req':'Faith Requirement'}

ds3_w_d = {
    'name':'Name', 
    'level':'Level', 
    'class':'Class', 
    'stability':'Stability',
    'critical':'Critical', 
    'weight':'Weight',
    'phy_damage':'Physical Damage', 
    'mag_damage':'Magic Damage', 
    'fir_damage':'Fire Damage', 
    'lig_damage':'Lightning Damage',
    'dar_damage':'Dark Damage', 
    'tot_damage':'Total Damage',
    'upgrade_path':'Upgrade Path',
    'bleed':'Bleed',
    'poison':'Poison',
    'frost':'Frost',
    'phy_reduction':'Physical Reduction', 
    'mag_reduction':'Magic Reduction',
    'fir_reduction':'Fire Reduction', 
    'lig_reduction':'Lightning Reduction',
    'str_bonus':'Strength Bonus', 
    'dex_bonus':'Dexterity Bonus',
    'int_bonus':'Intelligence Bonus', 
    'fai_bonus':'Faith Bonus',
    'damage_type':'Damage Type',
    'skill':'Skill',
    'buffable':'Buffable',
    'str_req':'Strength Requirement', 
    'dex_req':'Dexterity Requirement',
    'int_req':'Intelligence Requirement', 
    'fai_req':'Faith Requirement'}
