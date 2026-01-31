# 🚀 NUSUK Session Keepalive (Hajj.nusuk.sa)
Automatisation hybride : Cloudflare manuel → Login/OTP/Dashboard/Keepalive 100% AUTO.


## 🎯 Fonctionnalités
✅ Cloudflare manuel (anti-blocage)

🤖 Login + OTP automatique (6 chiffres)

🔄 Keepalive infini : Dashboard → Packages → Profile → Family

💾 Menu dropdown Profile précis (#user-profile-menu)

🛡️ Anti-stale elements + retry robuste

## 📋 Prérequis

Windows 10/11

Google Chrome (143+) : Télécharger

Internet (Cloudflare et  OTP manuel )

## 🛠️ Installation DOUBLE-CLIC (2 min)
### 1️⃣ Double-cliquez install_nusuk_env.bat

```
✅ Installe Python 3.12 (winget)
✅ Crée environnement virtuel (.venv)
✅ selenium + webdriver-manager + python-dotenv
```

### 2️⃣ Éditez .env
```
SESSION_USERNAME=votre.email@domaine.com
SESSION_PASSWORD=votre_mot_de_passe
LOGIN_URL=https://hajj.nusuk.sa/account/authorize
KEEPALIVE_INTERVAL= 10 # 10 seconde et vous pouvez l'augmenter
```

### 3️⃣ Lancer le programme:
Double-cliquez run_nusuk.bat
OU python selenium_keepalive.py

## ▶️ Utilisation

1. Chrome → hajj.nusuk.sa
2. 🖱️ COCHE MANUEL Cloudflare → "Succès!" VERT (10-30s)
3. ⏸️ ENTRÉE dans console
4. 📱 Tape OTP (6 chiffres de l'OTP reçu par mail)
5. 🎉 DASHBOARD → Keepalive ∞ automatique

### Logs attendus :

```
✅ LOGIN!
📱 OTP → 592476
✅ OTP - Dashboard...
🎉 DASHBOARD!
🔄 Cycle 1 → Dashboard ✅ → Packages ✅ → Profile ✅ → Family
😴 300s...
```

## 📁 Structure projet

```
nusuk/
├── selenium_keepalive.py     # Script principal
├── requirements.txt          # selenium webdriver-manager python-dotenv
├── .env.example             # Template config
├── .env                     # ← à adapter avec vos infos
├── install_nusuk_env.bat    # 🎉 DOUBLE-CLIC install
├── run_nusuk.bat            # 🎉 DOUBLE-CLIC run
└── README.md
```

## 🐛 Dépannage

|   Problème                  |    Solution                            |
|---                          |---                                     |	
| chrome not found            |	Installer Chrome                       |
| Timeout ChromeDriver        |	install_nusuk_env.bat recrée tout      |
| Cloudflare bloqué	MANUEL    | coche → Entrée                         |
| OTP 6 champs introuvables	  | Attendez.. lent le jour de la vente    |
| DEPRECATED_ENDPOINT         |	Ignorez (Google GCM bénin)             |


## 🔄 Keepalive Cycle

```
1. a[href="/profile/dashboard"] → Dashboard
2. a[href="/packages"] → Packages  
3. #user-profile-menu → "My Profile"
4. a[name="ApplicantMyFamily"] → My Family
→ 🔄 Repeat ∞
```
## ❌ Bug a fixer sur une autre branche

à la permière ouverture du navigateur la Captcha ne se valide qu'à la 2eme fois.

Si vous arrivez à le résoudre mettez le sur une branche et demandez une MR.


