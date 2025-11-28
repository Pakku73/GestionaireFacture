# FactureFlow

## Introduction
Application Django de gestion de produits, factures et génération de PDF

**Présentation :**

FactureFlow est une application web développée avec Django 5 permettant de gérer des produits, des factures, des lignes de factures, ainsi que l’export des factures en PDF.

L’objectif est de fournir une interface simple et efficace pour créer des factures, y ajouter des produits, suivre les montants et télécharger les documents au format PDF.

**Fonctionnalités**


Produits

    Création, édition, suppression de produits

    Affichage paginé des produits

    Validation de la date de péremption (impossible d’ajouter une date passée)

    ID généré automatiquement et non modifiable

Factures

    Création d’une facture

    Redirection automatique vers l’ajout d’items

    Possibilité d’ajouter plusieurs fois le même produit → fusion automatique dans une seule ligne

    Calcul automatique du total par ligne et du total de la facture

    Aperçu détaillé d'une facture

Export PDF

    Génération d’un PDF propre et formaté via xhtml2pdf

    Export avec numéro de facture dans le nom du fichier

Navigation

    Barre de navigation "Produits" / "Factures"

    Boutons stylisés changeant de couleur selon la page active

    Pagination sur toutes les listes

## Technologies utilisées

    Python 3.13

    Django 5.2

    SQLite (par défaut)

    Bootstrap 5 pour le style

    xhtml2pdf pour la génération de PDF


## Structure du projet

```
factureflow/
│
├── apps/
│   ├── products/
│   └── invoices/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   ├── products/
│   ├── invoices/
│   └── base.html
│
└── manage.py
```

## Installation & utilisation

### 1. Cloner le projet

git clone https://github.com/Pakku73/GestionaireFacture
cd factureflow

### 2. Créer un environnement virtuel

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

### 3. Installer les dépendances

pip install -r requirements.txt

### 4. Appliquer les migrations

python manage.py migrate

### 5. Lancer le serveur

python manage.py runserver