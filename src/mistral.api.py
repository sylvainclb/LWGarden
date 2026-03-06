import requests

with open("./src/mistral.config.json", "r") as configfile:
        config = json.load(configfile)


leek_id = 81638
fight_id = 51202636

lw_api = LWApi()

headers = {
    "Authorization": f"Bearer {config.api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "mistral-small-latest",
    "messages": [
        {"role": "system", "content": "Tu es un assistant spécialisé dans l'optimisation d'IA pour le jeu LeekWars. Voici un log de debug, analyse-le et propose des améliorations."},
        {"role": "user", "content": "Voici un extrait de log : [insérer ici ton log structuré]"}
    ]
}

response = requests.post(config.api_key, headers=headers, json=data)
print(response.json())