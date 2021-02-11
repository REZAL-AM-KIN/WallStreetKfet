# WallStreetKfet

A teleharger sur la vm:

MYSQL



Bon j'ai pas fini mais là l'idée c'est que dans config y'ait toute les variables à utiliser (sauf variables locales de calcul)
J'ai pas relu tout ton code mais j'ai rangé un peu le tout et testé les requetes, elles sont ok.

Faudrait notamment que tu fasses propre la fonction CalculPrix() en adaptant à la nouvelle structure (pas besoin du temps car déjà traité sur SQL, et les requêtes sont à utiliser depuis QUERRY)

"produit" est bcp utilisé mais je comprends pas trop d'ou il sort et ce qu'il est, peut etre changer son nom?


### Optionnel 1: Sauvegarde des informations pour un éventuel check de négat's kfet.

### optionnel 2: Sauvegarde dans une nouvelle table de la bdd de la variation des prix pour un futur affichage web.

Sal's hawking



// function drawChart() {
      //   var conso = JSON.parse('{{ conso|tojson }}');
		    // var prix = JSON.parse('{{ pprix|tojson }}');

      //   var options = {
      //     title: 'Company Performance',
      //     curveType: 'function',
      //     legend: { position: 'bottom' }
      //   };

      //   var chart = new google.visualization.LineChart(document.getElementById('prix_chart'));

      //   chart.draw(prix, options);

      //   var chart = new google.visualization.LineChart(document.getElementById('prix_chart'));

      //   chart.draw(conso, options);
      // }