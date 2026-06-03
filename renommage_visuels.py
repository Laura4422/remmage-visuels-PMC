import io
import os
import zipfile
import pandas as pd
import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Rénommateur de Visuels EAN -> IFLS", page_icon="📸")

st.title("📸 Renommage EAN > IFLS PMC")
st.write(
    "Importez votre fichier Excel et vos images pour les renommer instantanément par IFLS."
)

# 1. Zone d'import du fichier Excel
st.subheader("1. Fichier de correspondance (Excel)")
excel_file = st.file_uploader(
    "Choisissez votre fichier Excel (.xlsx)", type=["xlsx"]
)

# 2. Zone d'import des visuels
st.subheader("2. Vos visuels à renommer")
uploaded_images = st.file_uploader(
    "Sélectionnez toutes vos images d'un coup",
    type=["jpg", "jpeg", "png", "webp"],
    accept_multiple_files=True,
)

if excel_file and uploaded_images:
    try:
        # Lecture du fichier Excel
        df = pd.read_excel(excel_file)

        # ---- AJUSTEMENT DES COLONNES ----
        col_ean = "Ean"
        col_code = "Ref"

        # Vérification que les colonnes existent bien dans le fichier Excel fourni
        if col_ean not in df.columns or col_code not in df.columns:
            st.error(
                f"❌ Erreur : Les colonnes doivent s'appeler exactement `{col_ean}` et `{col_code}`."
            )
            st.warning(
                f"Colonnes actuellement trouvées dans votre fichier : {list(df.columns)}"
            )
            st.stop()

        st.info(
            f"ℹ️ Correspondance activée : `{col_ean}` ➔ `{col_code}`"
        )

        # Nettoyage et création du dictionnaire de correspondance
        mapping = {}
        for _, row in df.iterrows():
            ean_raw = str(row[col_ean]).strip().split(".")[0]  # Enlève les .0 des formats nombres
            ean_13 = ean_raw[:13]  # On prend les 13 premiers caractères
            new_code = str(row[col_code]).strip().split(".")[0]

            if len(ean_13) == 13 and new_code and new_code != "nan":
                mapping[ean_13] = new_code

        # Bouton pour lancer le traitement
        if st.button("⚡ Préparer les visuels", type="primary"):
            # Création d'un fichier ZIP en mémoire
            zip_buffer = io.BytesIO()

            with zipfile.ZipFile(
                zip_buffer, "w", zipfile.ZIP_DEFLATED
            ) as zip_file:
                success_count = 0
                not_found_count = 0

                # Boucle sur les images téléversées
                for img in uploaded_images:
                    original_name = img.name
                    ext = os.path.splitext(original_name)[1]  # Extension (.jpg, etc.)
                    img_ean_13 = original_name[:13]  # On isole l'EAN du nom de fichier

                    # Si l'EAN du fichier est dans l'Excel
                    if img_ean_13 in mapping:
                        # Nouveau nom = la valeur de "Ref" + l'extension
                        new_name = f"{mapping[img_ean_13]}{ext}"
                        zip_file.writestr(new_name, img.getvalue())
                        success_count += 1
                    else:
                        not_found_count += 1

            zip_buffer.seek(0)

            # Affichage des résultats
            if success_count > 0:
                st.success(
                    f"✅ {success_count} visuel(s) renommé(s) avec succès !"
                )
                if not_found_count > 0:
                    st.warning(
                        f"⚠️ {not_found_count} visuel(s) n'ont pas trouvé de correspondance dans l'Excel."
                    )

                # 3. Bouton de téléchargement du ZIP
                st.subheader("3. Télécharger le résultat")
                st.download_button(
                    label="📥 Télécharger les visuels renommés (ZIP)",
                    data=zip_buffer,
                    file_name="visuels_renommes.zip",
                    mime="application/zip",
                )
            else:
                st.error(
                    "❌ Aucun visuel n'a pu être associé. Vérifiez que les 13 premiers caractères de vos images correspondent bien aux valeurs de la colonne 'Ean'."
                )

    except Exception as e:
        st.error(
            f"Une erreur est survenue lors du traitement : {e}"
        )
else:
    st.info(
        "Veuillez importer le fichier Excel ET les visuels pour activer l'outil."
    )
    
