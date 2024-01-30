import mysql.connector
from mysql.connector import errorcode
import folium
import webbrowser

from pyAddLegend import addLe
from pyDefineDF import *

# Construction des dico d'après la bdd
# pour la carto
def retDic(cnx, maTable):
    dic = {}
    req = "SELECT * FROM accidentologie." + maTable + ";"
    with cnx.cursor() as c:
        c.execute(req)
        resultats = c.fetchall()
        for data in resultats:
            dic[data[0]] = data[1]
        pass
        return dic


#def DessinCarto():
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
    dAtm = retDic(cnx, "atm")
    dTypeCol = retDic(cnx, "col")
    dObs = retDic(cnx, "obs")
    dObsm = retDic(cnx, "obsm")
    cnx.close()

    #-----------------------------------------------------------------------------------------------------------
    df = DefineDF(['78'])
    # print(df)

    tMois = [
        "Janvier",
        "Février",
        "Mars",
        "Avril",
        "Mai",
        "Juin",
        "juillet",
        "Aout",
        "Septembre",
        "Octobre",
        "Novembre",
        "Decembre",
    ]

    idPrecAcc = ""

    # init carto
    mappo = folium.Map(location=[48.866, 2.333], zoom_start=12)

    #mappo = folium.Map(location=[44.4475, 1.4419], zoom_start=12, min_zoom=1, max_zoom=18, control_scale=True)

    i=1
    for i, ligne in df.iterrows():
        if idPrecAcc != ligne["Num_Acc"]:
            idPrecAcc = ligne["Num_Acc"]
            nbDead = 0
            nbHospi = 0
            nbHurt = 0
            nbOk = 0
            nbCatGrav = 0
            idIco = 99
            idGrav = 9
            suitePopUp = ""
            monIcone = ""
            maCouleur = ""

        # data du popup
        maDate = str(ligne["jour"]) + " " + str(tMois[ligne["mois"] - 1])  # date

        # choix de l'iconne en fonction de l'importance du Vh
        if ligne["catv"] in [0, 99]:
            if ligne["Num_Acc"] != idPrecAcc:
                idIco = 99
                monIcone = "people"
        elif ligne["catv"] in [1, 80]:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 1
            ):
                monIcone = "bike"  # vélo
                idIco = 1
        elif ligne["catv"] in [2, 4, 5, 30, 41, 50, 60, 80]:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 2
            ):
                monIcone = "moped"  # petit moteur
                idIco = 2
        elif ligne["catv"] in [6, 31, 32, 33, 34, 35, 36, 42, 43]:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 3
            ):
                monIcone = "moto"  # moto
                idIco = 3
        elif ligne["catv"] in [3, 7]:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 4
            ):
                monIcone = "car"  # VL
                idIco = 4
        elif ligne["catv"] in [18, 19, 37, 38, 40]:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 5
            ):
                monIcone = "bus"  # transport co
                idIco = 5
        elif ligne["catv"] in [8, 9, 10, 13]:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 6
            ):
                monIcone = "smallTruck"  # VU
                idIco = 6
        elif ligne["catv"] in [14, 15]:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 7
            ):
                monIcone = "bigTruck"  # PL
                idIco = 7
        elif ligne["catv"] in [16, 17, 21]:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 8
            ):
                monIcone = "tractor"  # agricol
                idIco = 8
        elif ligne["catv"] == 39:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 9
            ):
                monIcone = "train"  # train
                idIco = 9
        elif ligne["catv"] == 20:
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idIco > 10
            ):
                monIcone = "plowTruck"  # chantier payant
                idIco = 10
        else:
            idIco = 99
            monIcone = "people"

        # couleur en fonction de la gravité
        if ligne["grav"] in [-1, 1]:
            nbOk += 1
            if ligne["Num_Acc"] != idPrecAcc:
                idGrav = 9
                maCouleur = "green"
        elif ligne["grav"] == 2:
            nbDead += 1
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idGrav > 1
            ):
                maCouleur = "black"
                idGrav = 1
        elif ligne["grav"] == 3:
            nbHospi += 1
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idGrav > 2
            ):
                maCouleur = "red"
                idGrav = 2
        elif ligne["grav"] == 4:
            nbHurt += 1
            if (
                ligne["Num_Acc"] != idPrecAcc
                or ligne["Num_Acc"] == idPrecAcc
                and idGrav > 3
            ):
                maCouleur = "orange"
                idGrav = 3

        if nbDead > 0 or nbHospi > 0 or nbHurt > 0 or nbOk > 0:
            suitePopUp = "<tr>"
            if nbDead > 0:
                nbCatGrav += 1
                if nbDead == 1:
                    suitePopUp = (
                        suitePopUp
                        + '<td bgcolor="black"><font color="white"> Tué :'
                        + str(nbDead)
                        + " personne </font></td>"
                    )
                else:
                    suitePopUp = (
                        suitePopUp
                        + '<td bgcolor="black"><font color="white"> Tuées :'
                        + str(nbDead)
                        + " personnes </font></td>"
                    )
            if nbHospi > 0:
                nbCatGrav += 1
                if nbHospi == 1:
                    suitePopUp = (
                        suitePopUp
                        + '<td bgcolor="red"> Hospitalisé :'
                        + str(nbHospi)
                        + " personne </td>"
                    )
                else:
                    suitePopUp = (
                        suitePopUp
                        + '<td bgcolor="red"> Hospitalisées :'
                        + str(nbHospi)
                        + " personnes </td>"
                    )
            if nbHurt > 0:
                nbCatGrav += 1
                if nbHurt == 1:
                    suitePopUp = (
                        suitePopUp
                        + '<td bgcolor="orange"> Blessé leger :'
                        + str(nbHurt)
                        + " personne </td>"
                    )
                else:
                    suitePopUp = (
                        suitePopUp
                        + '<td bgcolor="orange"> Blessées légers :'
                        + str(nbHurt)
                        + " personnes </td>"
                    )
            if nbOk > 0:
                nbCatGrav += 1
                if nbOk == 1:
                    suitePopUp = (
                        suitePopUp
                        + '<td bgcolor="green"><font color="white"> Indemne : '
                        + str(nbOk)
                        + " personne </td>"
                    )
                else:
                    suitePopUp = (
                        suitePopUp
                        + '<td bgcolor="green"><font color="white"> Indemnes : '
                        + str(nbOk)
                        + " personnes </td>"
                    )
            suitePopUp = suitePopUp + "</tr>"

        libPopUp = (
            ("<table >" "<thead>" "<tr>" "<th bgcolor='grey' colspan=")
            + str(nbCatGrav)
            + (
                "><center>" + str(ligne["Num_Acc"]) + "</center></th>"
                "</tr>"
                "</thead>"
                "<tbody>"
                "<tr>"
                "<td colspan="
            )
            + str(nbCatGrav)
            + (">le " + str(maDate) + "</td>" "</tr>" "<tr>" "<td colspan=")
            + str(nbCatGrav)
            + (
                ">Condition atmosphérique : " + dAtm[ligne["atm"]] + "</td>"
                "</tr>"
                "<tr>"
                "<td colspan="
            )
            + str(nbCatGrav)
            + (
                ">Type de colision : " + dTypeCol[ligne["col"]] + "</td>"
                "</tr>"
                "<tr>"
                "<td colspan="
            )
            + str(nbCatGrav)
            + (
                ">Objet fixe heurté : " + dObs[ligne["obs"]] + "</td>"
                "</tr>"
                "<tr>"
                "<td colspan="
            )
            + str(nbCatGrav)
            + (">Objet mobile heurté : " + dObsm[ligne["obsm"]] + "</td>" "</tr>")
            + str(suitePopUp)
            + ("</tbody></table>")
        )

        # gestion de folium
        popup = folium.Popup(libPopUp, max_width=1000)

        ligne["lat"] = float(ligne["lat"].replace(",", "."))
        ligne["long"] = float(ligne["long"].replace(",", "."))
        if monIcone == "":
            monIcone = "people"
        #if ligne["dep"] in Idf:
        folium.map.Marker(
            location=[ligne["lat"], ligne["long"]],
            popup=popup,
            # icon = folium.Icon(color=maCouleur, icon_color=maCouleurIco, icon= "fa-sharp fa-solid fa-car", perfix='fa')
            icon=folium.features.CustomIcon(
                "C:/Users/saphi/OneDrive/Documents/miniProjPy/icone/"
                + monIcone
                + maCouleur
                + ".png",
                icon_size=(30, 30),
            ),
        ).add_to(mappo)

    addLe(mappo)

    #mappo.fit_bounds([41.3888, -5.3333], [51.1888, 9.5])
    #mappo.fit_bounds(mappo.get_bounds(), padding=(30,30))
    mappo.save("C:/Users/saphi/OneDrive/Documents/miniProjPy/mappo.html")
    webbrowser.open("C:/Users/saphi/OneDrive/Documents/miniProjPy/mappo.html")
