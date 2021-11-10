gen_vars = [
    'set', 'name', 'level', 'position', 'poise', 'weight', 
    'phy_reduction', 'mag_reduction', 'fir_reduction', 'lig_reduction',
    'ble_resist', 'poi_resist', 'cur_resist', 
    'buffable','skill','damage_type',
    'stability', 'critical', 'bleed', 'poison', 'frost',
    'phy_damage', 'mag_damage', 'fir_damage', 'lig_damage', 'dar_damage', 'tot_damage',
    'str_bonus', 'dex_bonus', 'int_bonus', 'fai_bonus',
    'str_req', 'dex_req', 'int_req', 'fai_req',
    'class', 'upgrade_path', 'status_effect']

ft_vars = [
    'poise', 'weight', 
    'phy_reduction', 'mag_reduction', 'fir_reduction', 'lig_reduction',
    'ble_resist', 'poi_resist', 'cur_resist','bleed','poison','frost',
    'stability','critical',
    'phy_damage', 'mag_damage', 'fir_damage', 'lig_damage','dar_damage', 'tot_damage',
    'str_bonus', 'dex_bonus', 'int_bonus', 'fai_bonus',
    'str_req', 'dex_req', 'int_req', 'fai_req']
fl_vars = [
    'set', 'name', 'position',
    'class', 'upgrade_path', 'status_effect',
    'buffable','skill','damage_type']

cod_vars = [
    'str_bonus', 'dex_bonus', 'int_bonus', 'fai_bonus', 'level']
cn_vars = [
    'set', 'name', 'position',
    'class', 'upgrade_path', 'status_effect','buffable','damage_type','skill']
cc_vars = [
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

ds1_d = {
    'set':'Set', 
    'name':'Name', 
    'level':'Level', 
    'class':'Class', 
    'position':'Position', 
    'stability':'Stability', 
    'poise':'Poise', 
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
    'fai_req':'Faith Requirement',
    'ble_resist':'Bleed Resistance', 
    'poi_resist':'Poison Resistance', 
    'cur_resist':'Curse Resistance'}

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

command_list = ["data:", "filter:", "plot:", "color:", "label:"]

filter_list = ["since", "until", "only"]
filter_combine = ["and", "or"]


success_response = "\n [+] Your plot was successfully completed."

err_response = "\n [-] ERROR: "
err_response_data = "dataset was not defined correclty."
err_response_filter = "filters were not defined correclty."
err_response_vars = "plot variables were not defined correclty."
err_response_color = "color variable was not defined correclty."
err_response_label = "label was not defined correclty."
err_response_command = "a basic command is missing."