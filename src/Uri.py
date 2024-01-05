root = "https://leekwars.com/api/"

# Farmer endpoints
login = "farmer/login-token" # /login, password
register_tournament_farmer = "farmer/register-tournament"
register_garden_farmer = "farmer/set-in-garden/in_garden"
set_avatar = "farmer/set-avatar"
get_farmer = "farmer/get" # farmer_id
get_self =  "farmer/get-from-token" # no params

# AI endpoints
get_ais = "ai/get-farmer-ais"
get_ai = "ai/get"
new_ai = "ai/new-name"
save_ai = "ai/save"
rename_ai = "ai/rename"
new_folder_ai = "ai-folder/new-name"
rename_folder_ai = "ai-folder/rename"

# Garden
get_farmer_opponents = "garden/get-farmer-opponents"
start_farmer_fight = "garden/start-farmer-fight/target_id"
get_leek_opponents = "garden/get-leek-opponents/leek_id"
start_leek_fight = "garden/start-solo-fight/leek_id/target_id"
get_team_opponents = "garden/get-composition-opponents/composition_id"
start_team_fight = "garden/start-team-fight/composition_id/target_id"

# Fight
get_fullmoon = "fight/fullmoon"

# Leek
register_tournament_leek = "leek/register-tournament/leek_id"
register_garden_leek = "leek/set-in-garden/leek_id/in_garden"
register_battle_royal_leek = "leek/register-auto-br/leek_id"
get_registers = "leek/get-registers/leek_id"
set_register = "leek/set-register/leek_id/key/value"
delete_register = "leek/delete-register/leek_id/key"

# Various
get_scheme = "scheme/get-all"
get_services = "service/get-all"
get_functions = "function/get-all"
get_doc_functions = "function/doc/locale"

# Trophy
get_farmer_trophies = "trophy/get-farmer-trophies" # farmer_id, lang

# History
get_farmer_history = "history/get-farmer-history" # farmer_id