import mysql.connector
from mysql.connector import errorcode
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

from pyDefineDF import *

# pour les graphes

maRegion = laFranceEntiere

def retDic(cnx, maTable):   #creer un dico depuis la SGBD
    dic = {}
    req = (
        "SELECT * FROM accidentologie." + str(maTable) + ";"
    ) 
    with cnx.cursor() as c:
        c.execute(req)
        resultats = c.fetchall()
        for data in resultats:
            dic[data[0]] = data[1]
        pass
        return dic


def retAnEnCours():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    return year


def retClasseAge(monAge):
    monAge = str(monAge)
    if int(monAge) >= 85:
        return "85_"
    if len(monAge) > 1:
        if int(monAge[1:]) < 5:
            return monAge[:1] + "0_" + monAge[:1] + "4"
        else:
            return monAge[:1] + "5_" + monAge[:1] + "9"
    else:
        if int(monAge[:1]) < 5:
            return "0_4"
        else:
            return "5_9"
        
def retNivSecu3(nivSecu3):
    if int(nivSecu3) > 0:
        return 3
    else:
        return 0
    
def retNivSecu2(nivSecu2):
    if int(nivSecu2) > 0:
        return 2
    else:
        return 0
    
def retNivSecu1(nivSecu1):
    if int(nivSecu1) > 0:
        return 1
    else:
        return 0

def creationCam(df,col, dic, titre, ligne, colonne, numGraph):
    df2 = (
        df[col].value_counts().rename_axis("id_" + col).to_frame("Nb_Accident")
    )  # on compte les valeurs de la table et on reconverti en df
    # on transforme le dico en df
    dfDic = pd.DataFrame(list(dic.items()), columns=["id_" + col, "lib_" + col])
    #dfDic = dfDic.astype({"id_" + col: "str"})
    
    df2 = df2.merge(dfDic, on="id_" + col)
    data = df2["Nb_Accident"]
    labels = df2["lib_" + col]
    colors = sns.color_palette("bright")
    ax = plt.subplot(ligne, colonne, numGraph)
    ax.set_title(titre, fontsize="small")
    ax.pie(data, labels=labels, colors=colors, autopct="%0.0f%%")


# def dessinGraphe():
# connexion a mysql
try:
    cnx = mysql.connector.connect(
        user="root",
        password="ToToleharicot22+",
        host="localhost",
        database="accidentologie",
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    # def des dicos
    dAgg = retDic(cnx, "agg") 
    dAtm = retDic(cnx, "atm")
    dCatr = retDic(cnx, "catr")
    dCatv = retDic(cnx, "catv")
    dEtatp = retDic(cnx, "etatp")
    dInfra = retDic(cnx, "infra")
    dInter = retDic(cnx, "inter")
    dLocp = retDic(cnx, "locp")
    dLum = retDic(cnx, "lum")
    dManv = retDic(cnx, "manv")
    dMotor = retDic(cnx, "motor")
    dPlan = retDic(cnx, "plan")
    dProf = retDic(cnx, "prof")
    dSexe = retDic(cnx, "sexe")
    dSitu = retDic(cnx, "situ")
    dSurf = retDic(cnx, "surf")
    dTrajet = retDic(cnx, "trajet")
    dVosp = retDic(cnx, "vosp")
    dGrav = retDic(cnx, "grav")
    dCol = retDic(cnx, "col")
    dInt = retDic(cnx, "inter")
    dObs = retDic(cnx, "obs")
    dObsm = retDic(cnx, "obsm")
    dChoc = retDic(cnx, "choc")
    dManv = retDic(cnx, "manv")
    dCirc = retDic(cnx, "circ")
    #dSecu1 = retDic(cnx, "secu1")
    #dSecu2 = retDic(cnx, "secu2")
    #dSecu3 = retDic(cnx, "secu3")
    dActp = retDic(cnx, "actp")
    
    cnx.close()

    fig = plt.figure(1, figsize=(85, 85), dpi=85)
    #ax = plt.subplots_adjust(left=0, right=0.95, bottom=0, top=0.95)
    fig.canvas.manager.set_window_title('Données des usagers')
    # graphe usagers-----------------------------------------------------------------------------------------------
    df = DefineDFus(maRegion)

    # Personnes impliquées
    df2 = (
        df["sexe"]
        .value_counts()
        .rename_axis("id_sexe")
        .to_frame("Nb_PersonnesImpactees")
    )  # on compte les valeurs de la table et on reconverti en df
    # on transforme le dico en df
    dfDicSe = pd.DataFrame(list(dSexe.items()), columns=["id_sexe", "lib_sexe"])
    df2 = df2.merge(dfDicSe, on="id_sexe")

    data = df2["Nb_PersonnesImpactees"]
    labels = df2["lib_sexe"]
    colors = sns.color_palette("bright")
    ax = plt.subplot(2, 3, 1)
    ax.set_title("Part d'accident par sexe", fontsize="small")
    ax.pie(data, labels=labels, colors=colors, autopct="%0.0f%%")

    # gravité par sexe
    df2 = df[["sexe", "grav"]]
    dfDicGr = pd.DataFrame(list(dGrav.items()), columns=["id_grav", "lib_grav"])
    df2 = df2.merge(dfDicSe, left_on=["sexe"], right_on=["id_sexe"])
    df2 = df2.merge(dfDicGr, left_on=["grav"], right_on=["id_grav"])
    df2 = (
        df2.groupby(["sexe", "grav"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )

    dfTue = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Tué")
    dfTue = dfTue.dropna()
    dfHos = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé hospitalisé")
    dfHos = dfHos.dropna()
    dfLeg = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé léger")
    dfLeg = dfLeg.dropna()
    dfInd = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Indemne")
    dfInd = dfInd.dropna()

    ax = plt.subplot(2, 3, 2)
    ax.set_title("Victimes")
    largeur_barre = 0.8
    y1 = dfTue
    y2 = dfHos
    y3 = dfLeg
    y4 = dfInd
    x = df2["lib_sexe"].unique()  # position en abscisse des barres
    # Tracé
    p = ax.bar(x, y1, width=largeur_barre, color="grey")
    ax.bar_label(p, label_type="center")
    p = ax.bar(x, y2, width=largeur_barre, bottom=y1, color="red")
    ax.bar_label(p, label_type="center")
    p = ax.bar(x, y3, width=largeur_barre, bottom=y2, color="orange")
    ax.bar_label(p, label_type="center")
    p = ax.bar(x, y4, width=largeur_barre, bottom=y3, color="green")
    ax.bar_label(p, label_type="center")

    # pyramide des ages
    classeAge = [
        "85_",
        "80_84",
        "75_79",
        "70_74",
        "65_69",
        "60_64",
        "55_59",
        "50_54",
        "45_49",
        "40_44",
        "35_39",
        "30_34",
        "25_29",
        "20_24",
        "15_19",
        "10_14",
        "5_9",
        "0_4",
    ]

    df2 = df[["sexe", "an_nais"]]
    df2 = df2[~df2["an_nais"].isnull()]
    df2 = df2.astype({"an_nais": "int"})
    df2 = df2.assign(AnEnCours=int(retAnEnCours()))
    df2 = df2.assign(monAge=df2["AnEnCours"] - df2["an_nais"])

    df2["classeAge"] = df2["monAge"].apply(lambda x: retClasseAge(x))

    df2 = df2.merge(dfDicSe, left_on=["sexe"], right_on=["id_sexe"])
    df2 = df2.drop(columns=["sexe", "AnEnCours", "an_nais", "id_sexe"])

    df2 = (
        df2.groupby(["classeAge", "lib_sexe"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )

    dfH = df2.where(df2["lib_sexe"] == "Masculin")
    dfH = dfH.dropna()
    dfH["Nb_PersonnesImpactees"] = dfH["Nb_PersonnesImpactees"] * -1
    dfH = dfH.sort_values(by=["monAge"], ascending=True)

    dfF = df2.where(df2["lib_sexe"] == "Féminin")
    dfF = dfF.dropna()
    dfF = dfF.sort_values(by=["monAge"], ascending=True)
    ax = plt.subplot(2, 3, 3)
    ax = sns.barplot(
        x="Nb_PersonnesImpactees",
        y="classeAge",
        errorbar = None,
        data=dfH,
        order=classeAge,
        color="Blue",
    )
    ax = sns.barplot(
        x="Nb_PersonnesImpactees",
        y="classeAge",
        errorbar = None,
        data=dfF,
        order=classeAge,
        color="Pink",
    )
    ax.set_title("Victimes par genre", fontsize="small")
    # ax.xlabel("M/F")
    ax.grid()

    # pyramides par tué
    df2 = df.where(df["grav"] == 2)
    df2 = df2.dropna()

    df2 = df2[["sexe", "an_nais"]]
    df2 = df2[~df2["an_nais"].isnull()]
    df2 = df2.astype({"an_nais": "int"})
    df2 = df2.assign(AnEnCours=int(retAnEnCours()))
    df2 = df2.assign(monAge=df2["AnEnCours"] - df2["an_nais"])

    df2["classeAge"] = df2["monAge"].apply(lambda x: retClasseAge(x))

    df2 = df2.merge(dfDicSe, left_on=["sexe"], right_on=["id_sexe"])
    df2 = df2.drop(columns=["sexe", "AnEnCours", "an_nais", "id_sexe"])

    df2 = (
        df2.groupby(["classeAge", "lib_sexe"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )

    dfH = df2.where(df2["lib_sexe"] == "Masculin")
    dfH = dfH.dropna()
    dfH["Nb_PersonnesImpactees"] = dfH["Nb_PersonnesImpactees"] * -1
    dfH = dfH.sort_values(by=["monAge"], ascending=True)

    dfF = df2.where(df2["lib_sexe"] == "Féminin")
    dfF = dfF.dropna()
    dfF = dfF.sort_values(by=["monAge"], ascending=True)

    ax = plt.subplot(2, 3, 4)
    ax = sns.barplot(
        x="Nb_PersonnesImpactees",
        y="classeAge",
        errorbar = None,
        data=dfH,
        order=classeAge,
        color="Blue",
    )
    ax = sns.barplot(
        x="Nb_PersonnesImpactees",
        y="classeAge",
        errorbar = None,
        data=dfF,
        order=classeAge,
        color="Pink",
    )
    ax.set_title("tué par genre", fontsize="small")
    # ax.xlabel("M/F")
    ax.grid()
    # ax.xticks(ticks=[-2000, -1000, 0, 1000, 2000], labels=['2,000k', '1,000k', '0', '1,000k', '2,000k'])

    # femmes aux volants
    df2 = df.where(df["grav"] == 2)
    df2 = df2.dropna()
    df2 = df2.drop(
        columns=[
            "id_vehicule",
            "num_veh",
            "place",
            "an_nais",
            "trajet",
            "secu1",
            "secu2",
            "secu3",
            "locp",
            "actp",
            "etatp",
            "catu",
            "grav",
            "sexe",
        ]
    )
    df3 = df.where(df["catu"] == 1)
    df3 = df3.dropna()
    df3 = df3.drop(
        columns=[
            "id_vehicule",
            "num_veh",
            "place",
            "an_nais",
            "trajet",
            "secu1",
            "secu2",
            "secu3",
            "locp",
            "actp",
            "etatp",
            "catu",
            "grav",
        ]
    )

    df2 = df2.merge(df3, on=["Num_Acc"])

    df2 = df2.merge(dfDicSe, left_on=["sexe"], right_on=["id_sexe"])
    df2 = df2.drop(columns=["Num_Acc"])
    df2 = df2.groupby(["sexe"]).value_counts().reset_index(name="Nb_Accident_mortel")

    data = df2["Nb_Accident_mortel"]
    labels = df2["lib_sexe"]
    ax = plt.subplot(2, 3, 5)
    ax.set_title("Genre ayant causé un accident mortel", fontsize="small")
    ax.pie(data, labels=labels, colors=colors, autopct="%0.0f%%")

    # place du mort ?
    df2 = df.where(df["place"] == 2)
    df2 = df2.dropna()
    df2 = df2["grav"].value_counts().rename_axis("id_grav").to_frame("Gravité_passager")
    df2 = df2.merge(dfDicGr, on=["id_grav"])

    data = df2["Gravité_passager"]
    labels = df2["lib_grav"]
    ax = plt.subplot(2, 3, 6)
    ax.set_title("Gravité de l'accident pour le passager ", fontsize="small")
    ax.pie(data, labels=labels, colors=colors, autopct="%0.0f%%")

    # graphes caracteristiques-------------------------------------------------------------------------------------
    fig = plt.figure(2, figsize=(85, 85), dpi=85)
    fig.canvas.manager.set_window_title('Caracteristiques des accidents')
    df = DefineDFca(maRegion)
    # Agg
    creationCam(df,"agg", dAgg, "Part d'accident en / hors agglomération", 2, 3, 1)

    # lum
    creationCam(df,"lum", dLum, "Part d'accident en fonction de la luminosité", 2, 3, 2)

    # atm
    creationCam(
        df,"atm", dAtm,
        "Part d'accident en fonction des conditions atmosphériques",
        2, 3, 3,
    )

    # col
    creationCam(df,"col", dCol, "Part d'accident part type de colision", 2, 3, 4)

    # int
    creationCam(df,"int", dInt, "Part d'accident aux intersections", 2, 3, 5)

    # departement--------------------------------------------------------------------------------------------------
    df = DefineDF(maRegion)
    fig = plt.figure(3, figsize=(85, 85), dpi=85)
    fig.canvas.manager.set_window_title('Données par départements')
    ax = plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95)

    df2 = df[["dep", "grav"]]
    dfDicGr = pd.DataFrame(list(dGrav.items()), columns=["id_grav", "lib_grav"])
    df2 = df2.merge(dfDicGr, left_on=["grav"], right_on=["id_grav"])
    df2 = (
        df2.groupby(["dep", "grav"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )
    dfTue = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Tué")
    dfTue = dfTue.dropna()
    dfHos = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé hospitalisé")
    dfHos = dfHos.dropna()
    dfLeg = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé léger")
    dfLeg = dfLeg.dropna()
    dfInd = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Indemne")
    dfInd = dfInd.dropna()

    ax = plt.subplot(2, 1, 1)
    plt.xticks(rotation=90)
    ax.set_title("Victimes par département")
    largeur_barre = 0.8
    y1 = dfTue
    y2 = dfHos
    y3 = dfLeg
    y4 = dfInd
    x = df2["dep"].unique()  # position en abscisse des barres
    # Tracé
    p = ax.bar(x, y1, width=largeur_barre, color="grey")
    ax.bar_label(p, label_type="center")
    p = ax.bar(x, y2, width=largeur_barre, bottom=y1, color="red")
    p = ax.bar(x, y3, width=largeur_barre, bottom=y2, color="orange")
    p = ax.bar(x, y4, width=largeur_barre, bottom=y3, color="green")

    dfPo = DefineDFpo(maRegion)
    df2 = df[["dep", "grav"]]
    df2 = df2.astype({"dep": "str"})
    dfDicGr = pd.DataFrame(list(dGrav.items()), columns=["id_grav", "lib_grav"])
    df2 = df2.merge(dfDicGr, left_on=["grav"], right_on=["id_grav"])
    df2 = (
        df2.groupby(["dep", "grav"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )
    df2 = df2.merge(dfPo, left_on=["dep"], right_on=["CODDEP"])
    df2["Nb_PersonnesImpactees"] = df2["Nb_PersonnesImpactees"] / df2["PTOT"] #* 100000

    df2 = df2.sort_values(
        by=["lib_grav", "Nb_PersonnesImpactees"], ascending=[False, True]
    )

    dfTue = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Tué")
    dfTue = dfTue.dropna()
    dfHos = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé hospitalisé")
    dfHos = dfHos.dropna()
    dfLeg = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé léger")
    dfLeg = dfLeg.dropna()
    dfInd = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Indemne")
    dfInd = dfInd.dropna()

    # la meme ramené a la population
    ax = plt.subplot(2, 1, 2)
    plt.xticks(rotation=90)
    ax.set_title("Victimes ramenées à la population")
    largeur_barre = 0.8
    y1 = dfTue
    y2 = dfHos
    y3 = dfLeg
    y4 = dfInd
    x = df2["dep"].unique()  # position en abscisse des barres
    # Tracé
    p = ax.bar(x, y1, width=largeur_barre, color="grey")
    p = ax.bar(x, y2, width=largeur_barre, bottom=y1, color="red")
    p = ax.bar(x, y3, width=largeur_barre, bottom=y2, color="orange")
    p = ax.bar(x, y4, width=largeur_barre, bottom=y3, color="green")

    # Accident par mois---------------------------------------------------------------------------------------------
    fig = plt.figure(4, figsize=(85, 85), dpi=85)
    fig.canvas.manager.set_window_title('Le meilleur jour pour rester au parking')
    dMois = {
        "1": "Janvier",
        "2": "Février",
        "3": "Mars",
        "4": "Avril",
        "5": "Mai",
        "6": "Juin",
        "7": "juillet",
        "8": "Aout",
        "9": "Septembre",
        "10": "Octobre",
        "11": "Novembre",
        "12": "Decembre",
    }

    df2 = df[["mois", "grav"]]
    dfDicGr = pd.DataFrame(list(dGrav.items()), columns=["id_grav", "lib_grav"])
    dfDicMois = pd.DataFrame(list(dMois.items()), columns=["id_Mois", "lib_Mois"])
    df2 = df2.astype({"mois": "int"})
    dfDicMois = dfDicMois.astype({"id_Mois": "int"})
    df2 = df2.merge(dfDicGr, left_on=["grav"], right_on=["id_grav"])
    df2 = df2.merge(dfDicMois, left_on=["mois"], right_on=["id_Mois"])

    df2 = (
        df2.groupby(["mois", "grav"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )
    df2 = df2.sort_values(by=["mois", "lib_grav"], ascending=[True, True])

    dfTue = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Tué")
    dfTue = dfTue.dropna()
    dfHos = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé hospitalisé")
    dfHos = dfHos.dropna()
    dfLeg = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé léger")
    dfLeg = dfLeg.dropna()
    dfInd = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Indemne")
    dfInd = dfInd.dropna()

    # la meme ramené a la population
    ax = plt.subplot(2, 1, 1)
    # plt.xticks(rotation = 90)
    ax.set_title("Victimes par mois")
    largeur_barre = 0.8
    y1 = dfTue
    y2 = dfHos
    y3 = dfLeg
    y4 = dfInd
    x = df2["lib_Mois"].unique()  # position en abscisse des barres
    # Tracé
    p = ax.bar(x, y1, width=largeur_barre, color="grey")
    p = ax.bar(x, y2, width=largeur_barre, bottom=y1, color="red")
    p = ax.bar(x, y3, width=largeur_barre, bottom=y2, color="orange")
    p = ax.bar(x, y4, width=largeur_barre, bottom=y3, color="green")

    # accident par jour
    dJour = {
        "0": "Lundi",
        "1": "Mardi",
        "2": "Mercredi",
        "3": "Jeudi",
        "4": "Vendredi",
        "5": "Samedi",
        "6": "Dimanche",
    }
    df2 = df[["jour", "mois", "an", "grav"]]
    df2 = df2.astype({"jour": "str"})
    df2 = df2.astype({"mois": "str"})
    df2 = df2.astype({"an": "str"})
    df2["datejour"] = df2["an"] + "-" + df2["mois"] + "-" + df2["jour"]
    df2 = df2.astype({"datejour": "datetime64[ns]"})
    df2["jour"] = df2["datejour"].dt.dayofweek

    dfDicGr = pd.DataFrame(list(dGrav.items()), columns=["id_grav", "lib_grav"])
    dfDicjour = pd.DataFrame(list(dJour.items()), columns=["id_jour", "lib_jour"])
    df2 = df2.astype({"jour": "int"})
    dfDicjour = dfDicjour.astype({"id_jour": "int"})
    df2 = df2.merge(dfDicGr, left_on="grav", right_on="id_grav")
    df2 = df2.merge(dfDicjour, left_on="jour", right_on="id_jour")
    df2 = df2.drop(columns=["an", "mois", "datejour", "jour", "grav", "id_grav"])
    df2 = (
        df2.groupby(["lib_jour", "lib_grav"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )
    df2 = df2.sort_values(by=["id_jour", "lib_grav"], ascending=[True, True])
    dfTue = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Tué")
    dfTue = dfTue.dropna()
    dfHos = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé hospitalisé")
    dfHos = dfHos.dropna()
    dfLeg = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Blessé léger")
    dfLeg = dfLeg.dropna()
    dfInd = df2["Nb_PersonnesImpactees"].where(df2["lib_grav"] == "Indemne")
    dfInd = dfInd.dropna()

    # la meme ramené a la journee
    ax = plt.subplot(2, 1, 2)
    ax.set_title("Victimes par journée")
    largeur_barre = 0.8
    y1 = dfTue
    y2 = dfHos
    y3 = dfLeg
    y4 = dfInd
    x = df2["lib_jour"].unique()  # position en abscisse des barres
    # Tracé
    p = ax.bar(x, y1, width=largeur_barre, color="grey")
    p = ax.bar(x, y2, width=largeur_barre, bottom=y1, color="red")
    p = ax.bar(x, y3, width=largeur_barre, bottom=y2, color="orange")
    p = ax.bar(x, y4, width=largeur_barre, bottom=y3, color="green")

    # vehicule--------------------------------------------------------------------------------------------------
    df = DefineDFvh(maRegion)
    fig = plt.figure(5, figsize=(85, 85), dpi=85)
    fig.canvas.manager.set_window_title('Accidents par type de véhicule')

    # cat vh
    creationCam(df,"catv", dCatv, "Part d'accident part type de véhicule", 1, 1, 1)

    fig = plt.figure(6, figsize=(85, 85), dpi=85)
    fig.canvas.manager.set_window_title("Envenement lors de l'accident")
    # obs
    creationCam(df,"obs", dObs, "Part d'accident part type d'obstacle fixe", 2, 3, 1)

    # obsm
    creationCam(df,"obsm", dObsm, "Part d'accident part type d'obstacle mobile", 2, 3, 2)

    # type de choc
    creationCam(df,"choc", dChoc, "Type de choc lors d'un accident", 2, 3, 3)

    # manoeuvre
    creationCam(df,"manv", dManv, "Accident lors de manoeuvre", 2, 3, 4)

    # motorisation
    creationCam(df,"motor", dMotor, "Part d'accident par type de motorisation", 2, 3, 5)

    # Lieux---------------------------------------------------------------------------------------------------------
    df = DefineDFli(maRegion)
    fig = plt.figure(7, figsize=(85, 85), dpi=85)
    fig.canvas.manager.set_window_title('Lieux des accidents')

    # type de route
    creationCam(df,"catr", dCatr, "Part d'accident par type de route", 2, 3, 1)

    # regime de circulation
    creationCam(df,"circ", dCirc, "Part d'accident par régime de ciculation", 2, 3, 2)

    # existence d'une voie réservée
    creationCam(
        df,"vosp", dVosp, "Part d'accident en présence d'une voie reservée", 2, 3, 3
    )

    # Profil de route
    creationCam(df,"prof", dProf, "Part d'accident en fonction du profil", 2, 3, 4)

    # Plan
    creationCam(df,"plan", dPlan, "Part d'accident par tracé en plan", 2, 3, 5)

    # Surface
    creationCam(df,"surf", dSurf, "Part d'accident par type de surface", 2, 3, 6)


    #survie en moto-------------------------------------------------------------------------------------------------
    df = DefineDFVhUs(maRegion)
    fig = plt.figure(8, figsize=(85, 85), dpi=85)
    fig.canvas.manager.set_window_title('Le cas des deux roues')

    df2 = df[df.catv.isin([2, 30, 31, 32, 33, 34,41,42,43])]
    df2 = df2[df2.catu.isin([1, 2,])]    
    df2 = df2[['catv', 'grav', 'secu1', 'secu2', 'secu3']]

    dfDicCv = pd.DataFrame(list(dCatv.items()), columns=["id_catv", "lib_catv"])
    dfDicGr = pd.DataFrame(list(dGrav.items()), columns=["id_grav", "lib_grav"])
    #dfDicS1 = pd.DataFrame(list(dSecu1.items()), columns=["id_secu1", "lib_secu1"]) 
    #dfDicS2 = pd.DataFrame(list(dSecu2.items()), columns=["id_secu2", "lib_secu2"])
    #dfDicS3 = pd.DataFrame(list(dSecu3.items()), columns=["id_secu3", "lib_secu3"])

    df2 = df2.merge(dfDicCv, left_on="catv", right_on="id_catv")
    df2 = df2.merge(dfDicGr, left_on="grav", right_on="id_grav")
    #df2 = df2.merge(dfDicS1, left_on="secu1", right_on="id_secu1")
    #df2 = df2.merge(dfDicS2, left_on="secu2", right_on="id_secu2")
    #df2 = df2.merge(dfDicS3, left_on="secu3", right_on="id_secu3")

    df2 = df2.drop(columns=["id_catv", "id_grav",])# "id_secu1", "id_secu2", "id_secu3",]) 

    #survie
    creationCam(df2,'grav', dGrav, "Impact sur les moto", 2, 2, 1)

    #2 roues le plus assassin
    df3 = df2.where(df2["grav"] == 2)
    df3 = df3.dropna()

    creationCam(df3,'catv', dCatv, "2 roues motorisés le plus mortel", 2, 2, 2)

    #survie par niveau de sécurité
    dfTtl = df2[['lib_catv', 'lib_grav',]]#pour le graphe suivant
    df2["nivSecu1"] = df2["secu1"].apply(lambda x: retNivSecu1(x))
    df2["nivSecu2"] = df2["secu2"].apply(lambda x: retNivSecu2(x))
    df2["nivSecu3"] = df2["secu3"].apply(lambda x: retNivSecu3(x))
    df2["nivSecu"] = df2[["nivSecu1", "nivSecu2", "nivSecu3"]].max(axis=1)
    df2 = df2.astype({"nivSecu": "str"})
    df2 = df2.sort_values(by=["nivSecu"], ascending=True)
    df2 = df2.drop(columns=["catv", "grav", "secu1", "secu2", "secu3", "nivSecu1", "nivSecu2", "nivSecu3"])
    df2 = (
        df2.groupby(["lib_catv", "lib_grav", "nivSecu"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )

    #creationCam(df2,'nivSecu', dCatv, "Nombre de personne impactées par niveau de sécurité", 2, 2, 3)

    ax = plt.subplot(2, 2, 3)
    plt.xticks(rotation=90)
    ax = sns.stripplot(data=df2, x="Nb_PersonnesImpactees", y="nivSecu", hue="lib_grav", s=7, jitter=True, dodge = True)
    ax.set(ylabel="")




    fig = plt.figure(9, figsize=(85, 85), dpi=85) # moto 2ème-------------------------------------------------------
    fig.canvas.manager.set_window_title("moto la suite : niveau d'équipement")

    df2 = df[df.catv.isin([2, 30, 31, 32, 33, 34,41,42,43])]
    df2 = df2[df2.catu.isin([1, 2,])]    
    df2 = df2[['catv', 'grav', 'secu1', 'secu2', 'secu3']]

    dfDicCv = pd.DataFrame(list(dCatv.items()), columns=["id_catv", "lib_catv"])
    dfDicGr = pd.DataFrame(list(dGrav.items()), columns=["id_grav", "lib_grav"])
    df2 = df2.merge(dfDicCv, left_on="catv", right_on="id_catv")
    df2 = df2.merge(dfDicGr, left_on="grav", right_on="id_grav")
    df2 = df2.drop(columns=["id_catv", "id_grav",])

    df2["nivSecu1"] = df2["secu1"].apply(lambda x: retNivSecu1(x))
    df2["nivSecu2"] = df2["secu2"].apply(lambda x: retNivSecu2(x))
    df2["nivSecu3"] = df2["secu3"].apply(lambda x: retNivSecu3(x))
    df2["nivSecu"] = df2[["nivSecu1", "nivSecu2", "nivSecu3"]].max(axis=1)
    df2 = df2.sort_values(by=["nivSecu"], ascending=True)
    df2 = df2.astype({"nivSecu": "str"})

    df3 = df2.where(df2["grav"] == 2)
    df3 = df3.dropna()
    df3 = df3.drop(columns=["catv", "grav", "secu1", "secu2", "secu3", "nivSecu1", "nivSecu2", "nivSecu3"])
    df3 = (
        df3.groupby(["lib_catv", "lib_grav", "nivSecu"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )
    x=df3["nivSecu"].unique()
    ax = plt.subplot(2, 2, 1)
    plt.xticks(rotation=90)
    ax = sns.barplot(
        x="nivSecu",
        y="Nb_PersonnesImpactees",
        errorbar = None,
        data=df3,
        order=x,
        hue="lib_catv",
    )
    ax.set_title("Niveau d'équipement pour les personnes tuées en 2 roues", fontsize="small")
    ax.grid()

    df3 = df2.where(df2["grav"] == 3)
    df3 = df3.dropna()
    df3 = df3.drop(columns=["catv", "grav", "secu1", "secu2", "secu3", "nivSecu1", "nivSecu2", "nivSecu3"])
    df3 = (
        df3.groupby(["lib_catv", "lib_grav", "nivSecu"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )
    ax = plt.subplot(2, 2, 2)
    plt.xticks(rotation=90)
    ax = sns.barplot(
        x="nivSecu",
        y="Nb_PersonnesImpactees",
        errorbar = None,
        data=df3,
        order=x,
        hue="lib_catv",
    )
    ax.set_title("Niveau d'équipement pour les personnes hospitalisées en 2 roues", fontsize="small")
    ax.grid()

    df3 = df2.where(df2["grav"] == 4)
    df3 = df3.dropna()
    df3 = df3.drop(columns=["catv", "grav", "secu1", "secu2", "secu3", "nivSecu1", "nivSecu2", "nivSecu3"])
    df3 = (
        df3.groupby(["lib_catv", "lib_grav", "nivSecu"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )
    ax = plt.subplot(2, 2, 3)
    plt.xticks(rotation=90)
    ax = sns.barplot(
        x="nivSecu",
        y="Nb_PersonnesImpactees",
        errorbar = None,
        data=df3,
        order=x,
        hue="lib_catv",
    )
    ax.set_title("Niveau d'équipement pour les personnes legerement bléssées en 2 roues", fontsize="small")
    ax.grid()

    df3 = df2.where(df2["grav"] == 4)
    df3 = df3.dropna()
    df3 = df3.drop(columns=["catv", "grav", "secu1", "secu2", "secu3", "nivSecu1", "nivSecu2", "nivSecu3"])
    df3 = (
        df3.groupby(["lib_catv", "lib_grav", "nivSecu"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )
    ax = plt.subplot(2, 2, 4)
    plt.xticks(rotation=90)
    ax = sns.barplot(
        x="nivSecu",
        y="Nb_PersonnesImpactees",
        errorbar = None,
        data=df3,
        order=x,
        hue="lib_catv",
    )
    ax.set_title("Niveau d'équipement pour les personnes indemnes en 2 roues", fontsize="small")
    ax.grid()



    #accident de pieton-------------------------------------------------------------------------------------------
    df = DefineDFus(maRegion)
    fig = plt.figure(10, figsize=(85, 85), dpi=85)
    fig.canvas.manager.set_window_title('accident de pieton')

    df = df.where(df["catu"] == 3)
    df = df.dropna()

    #localisation du pieton
    creationCam(df,"locp", dLocp, "Localisation du pieton lors de l'accident", 2, 2, 1)

    #action du pieton lors de l'accident
    creationCam(df,"actp", dActp, "Action du pieton lors de l'accident", 2, 2, 2)

    #etait il seul ou accompagné
    creationCam(df,"etatp", dEtatp, "Etait-il seul ou accompagné", 2, 2, 3)

    #plage d'age pour un accident pieton 
    df2 = df[["an_nais"]]
    
    df2 = df2[~df2["an_nais"].isnull()]
    df2 = df2.astype({"an_nais": "int"})
    df2 = df2.assign(AnEnCours=int(retAnEnCours()))
    df2 = df2.assign(monAge=df2["AnEnCours"] - df2["an_nais"])

    df2["classeAge"] = df2["monAge"].apply(lambda x: retClasseAge(x))

    df2 = df2.drop(columns=["AnEnCours", "an_nais"])

    df2 = (
        df2.groupby(["classeAge"])
        .value_counts()
        .reset_index(name="Nb_PersonnesImpactees")
    )
    df2 = df2.sort_values(by=["monAge"], ascending=True)
    
    ax = plt.subplot(2, 2, 4)
    plt.xticks(rotation=90)

    ax = sns.barplot(
        x="classeAge",
        y="Nb_PersonnesImpactees",
        errorbar = None,
        data=df2,
        order=classeAge,
        color="Blue",
    )
    ax.set_title("Accident de pieton par plage d'age", fontsize="small")
    ax.grid()

    #plein ecran
#    figmgr = plt.get_current_fig_manager()
#    bkend = plt.get_backend()
    #print (bkend)
#    figmgr.resize(*figmgr.window.maxsize())

    plt.show()
