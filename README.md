# remmage-visuels-PMC

# 📸 Convertisseur & renommage de visuels (EAN ➔ Code Interne)

## 🎯 Contexte & Problématique Business
Dans l'édition et les arts graphiques, le renommage des visuels produits est souvent un casse-tête logistique. Les studios photo nomment généralement les fichiers par leur code du type EAN-13, tandis que les outils ERP ou de gestion de contenu (PIM/CMS) nécessitent souvent une nomenclature basée sur des références internes.

De plus, les fichiers sources contiennent régulièrement des suffixes superflus (ex: `3600541234567_HD_zoom.jpg`). Effectuer ce renommage à la main sur des milliers de lignes est source d'erreurs et surtout extrêmement chronophage.

Ma solution :
Une application web d'automatisation locale et cloud qui traite, nettoie et renomme des milliers d'images en moins de 3 secondes à partir d'un simple fichier Excel de correspondance.

---

## ⚡ Fonctionnalités Clés
* **Parsing intelligent :** Extraction automatique des 13 premiers caractères du nom de fichier pour isoler l'EAN, faisant abstraction du texte superflu.
* **Nettoyage à la volée :** Suppression des suffixes inutiles pour renommer le fichier avec le code interne "pur", tout en conservant dynamiquement l'extension d'origine (`.jpg`, `.png`, `.webp`, etc.).
* **Appairage par dictionnaire (Mapping Excel) :** Analyse dynamique d'un fichier Excel basé sur les colonnes configurables `Ean` et `Ref`.
* **Traitement 100% en mémoire (Sécurité) :** Les fichiers sont traités et encapsulés directement dans un fichier `.zip` téléchargeable sans stockage persistant sur le serveur, garantissant la confidentialité des données.

---

## 🛠️ Stack Technique & Compétences Démontrées

En développant ce projet, j'ai mis en application les compétences techniques suivantes :

* **Python 3** : Logique algorithmique, manipulation de chaînes de caractères (clipping de chaînes) et gestion du système de fichiers en mémoire.
* **Streamlit** : Conception d'une interface utilisateur (UI/UX) moderne, fluide et interactive, orientée "Data Application".
* **Pandas & OpenPyXL** : Ingestion, nettoyage et requêtage de structures de données tabulaires (DataFrames Excel).
* **Gestion des flux de données (I/O)** : Utilisation des modules `io` et `zipfile` pour manipuler des flux binaires en mémoire tampon (`BytesIO`), optimisant la vitesse d'exécution et évitant l'écriture de fichiers temporaires sur le disque.
* **Déploiement Cloud & DevOps** : Containerisation légère via le gestionnaire de paquets ultra-rapide `uv` (Astral) et déploiement continu (CI/CD) sur Streamlit Community Cloud.

---

## 🚀 Comment l'utiliser ?

### En ligne (Cloud)
L'application est déployée et accessible par l'équipe à l'adresse suivante : 
🔗 https://remmage-visuels-pmc-2026.streamlit.app/

### En local (Développeur)
Pour exécuter le projet dans un environnement virtuel isolé et sécurisé sans installation lourde :

```bash
# Utilisation du gestionnaire moderne 'uv' pour une exécution instantanée
uvx --with pandas --with openpyxl streamlit run renommage_visuels.py

---
💡 *Projet conçu et réalisé par **Laura Sébille** dans une optique d'optimisation des processus internes et de transition numérique des outils de gestion de catalogue.*
📅 *03/06/2026*
