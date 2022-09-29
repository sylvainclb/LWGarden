Root = "https://leekwars.com/api/"

# Farmer endpoints
Login = "farmer/login-token" # /login, password 
RegisterTournamentFarmer = "farmer/register-tournament"
RegisterGardenFarmer = "farmer/set-in-garden/in_garden"
SetAvatar = "farmer/set-avatar"

# AI endpoints
GetAIs = "ai/get-farmer-ais"
GetAI = "ai/get"

# Garden
GetFarmerOpponents = "garden/get-farmer-opponents"
StartFarmerFight = "garden/start-farmer-fight/target_id"
GetLeekOpponents = "garden/get-leek-opponents/leek_id"
StartLeekFight = "garden/start-solo-fight/leek_id/target_id"
GetTeamOpponents = "garden/get-composition-opponents/composition_id"
StartTeamFight = "garden/start-team-fight/composition_id/target_id"

# Fight
GetFullMoon = "fight/fullmoon"

# Leek
RegisterTournamentLeek = "leek/register-tournament/leek_id"
RegisterGardenLeek = "leek/set-in-garden/leek_id/in_garden"
RegisterBRLeek = "leek/register-auto-br/leek_id"
GetRegisters = "leek/get-registers/leek_id"
SetRegister = "leek/set-register/leek_id/key/value"
DeleteRegister = "leek/delete-register/leek_id/key"

# Various
GetScheme = "scheme/get-all"
GetServices = "service/get-all"
GetFunctions = "function/get-all"
GetDocFunctions = "function/doc/locale"

# Trophy
GetFarmerTrophies = "trophy/get-farmer-trophies/farmer_id/lang"

# History
GetFarmerHistory = "history/get-farmer-history/farmer_id"