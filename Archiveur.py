#!/usr/bin/env python

# =============================================================================
# Titre : Archiveur.py
# Description : Commande console qui archive et extrait des fichiers.
# Auteur : Nicolas Bisson
# Date : 2015/04/9
# Version : 1.0
# Usage : python3 Archiveur.py
# Notes :
# python_version : 3.4.0
# =============================================================================

import sys


def tailleFichier(FICHIER_ARCHIVAGE, *fichiers):
    """ Inscrit la taille de chaque fichier dans un fichier.
    """
    numeroFichier = 0
    tailles = open(FICHIER_ARCHIVAGE+"_TaillesFichier.txt", mode="a+")
    while numeroFichier < len(fichiers):
        fichier = open(fichiers[numeroFichier], mode="r")
        fichier.seek(0, 0)
        tailles.write(str(fichier.seek(0, 2))+" ")
        fichier.close()
        numeroFichier += 1
    tailles.close()


def archiver(FICHIER_ARCHIVAGE, *fichiers):
    """ Copie le contenu de chaque fichier entrer en argument dans un
        autre fichier pour les archiver au même endroit.
    """
    archivage = open(FICHIER_ARCHIVAGE, mode="ab")
    for nomFichier in fichiers:
        for lignes in nomFichier:
            archivage.write(lignes)
    archivage.close()


def extraire(FICHIER_ARCHIVAGE, *fichiers):  # Extrait le fichier au complet...
    """ Extrait le contenu de chaque numéro de fichier entrer en argument
        dans un autre fichier et ce pour chaque fichier.
    """
    desarchiver = open("fichierExtrait", mode="ab")
    for nomFichier in fichiers:
        for lignes in nomFichier:
            desarchiver.write(lignes)
    desarchiver.close()


def gestionArgument(arguments):
    """ Permet de gérer les arguments entrer dans l'invite de commande,
        pour le bon fonctionnement du programme.
    """
    if len(arguments) < 4:
        print("Utilisation: <programme> <action> <fichier_archivage> <fichier1> <fichier2>...")
        sys.exit(1)
    
    if sys.argv[1] != "archiver" and sys.argv[1] != "extraire":
        print("Utilisation: <action> = archiver ou extraire")

    if sys.argv[1] == "archiver":
        fichier1 = 0
        nbFichier1 = 3
        while fichier1 < len(sys.argv[3:]):
            tailleFichier(sys.argv[2], sys.argv[nbFichier1])
            nbFichier1 += 1
            fichier1 += 1

        fichier2 = 0
        nbFichier2 = 3
        while fichier2 < len(sys.argv[3:]):
            archivage = open(sys.argv[nbFichier2], mode="rb")
            archiver(sys.argv[2], archivage)
            archivage.close()
            nbFichier2 += 1
            fichier2 += 1

    elif sys.argv[1] == "extraire":  # Extrait le fichier au complet...
        fichier3 = 0
        nbFichier3 = 0
        while fichier3 < len(sys.argv[3:]):
            extraction = open(sys.argv[nbFichier3], mode="rb")
            extraire(sys.argv[2], extraction)
            nbFichier3 += 1
            fichier3 += 1

gestionArgument(sys.argv)