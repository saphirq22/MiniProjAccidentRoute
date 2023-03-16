from branca.element import Template, MacroElement

def addLe(mappo):
  template = """
  {% macro html(this, kwargs) %}

  <!doctype html>
  <html lang="fr">
  <head>

  </head>
  <body>
  
  <div id='maplegend' class='maplegend' 
      style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
      border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
      
  <div class='legend-title'>Accidents routiers</div>
    <div class='legend-scale'>
      <ul class='legend-labels'>
        <li><span style='background:black;opacity:0.7;'></span>Tué(s)</li>
        <li><span style='background:red;opacity:0.7;'></span>Blessé(s)Kospitalisé(s)</li>
        <li><span style='background:orange;opacity:0.7;'></span>Blessé(s)Leger(s)</li>
        <li><span style='background:green;opacity:0.7;'></span>Indemne(s)</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/peopleBlack.png"> Piéton</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/bikeBlack.png"> Vélo</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/busBlack.png"> Bus et tramway</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/carBlack.png"> Voiture et microcar</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/mopedBlack.png"> 2 Roues <=50cm3 et trotinette</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/motoBlack.png"> 2 Roues >50cm3</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/plowTruck.png"> Engin de chantier</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/smallTruckBlack.png"> Véhicule utilitaire</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/bigTruckBlack.png"> Camion</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/tractorBlack.png"> Engin agricole</li>
        <li><img width=26 hight=26 src="http://127.0.1.22/miniProjPy/icone/trainBlack.png"> Train</li>
      </ul>
    </div>
  </div>
  </body>
  </html>

  <style type='text/css'>
    .maplegend .legend-title {
      text-align: left;
      margin-bottom: 5px;
      font-weight: bold;
      font-size: 90%;
      }
    .maplegend .legend-scale ul {
      margin: 0;
      margin-bottom: 5px;
      padding: 0;
      float: left;
      list-style: none;
      }
    .maplegend .legend-scale ul li {
      font-size: 80%;
      list-style: none;
      margin-left: 0;
      line-height: 18px;
      margin-bottom: 2px;
      }
    .maplegend ul.legend-labels li span {
      display: block;
      float: left;
      height: 16px;
      width: 30px;
      margin-right: 5px;
      margin-left: 0;
      border: 1px solid #999;
      }
    .maplegend a {
      color: #777;
      }
  </style>
  {% endmacro %}"""

  macro = MacroElement()
  macro._template = Template(template)

  mappo.get_root().add_child(macro)