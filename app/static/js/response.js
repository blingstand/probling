class Response{
    constructor(resp){
        this.firstResponse = this.firstResponse(resp["message"]);
        this.secondResponse = this.secondResponse(resp["coordinates"]);
        this.thirdResponse = this.thirdResponse(resp["summary"], resp["url"]);
    }
    greatMessage = function(container){
        //gathers the three parts of the answer
        container.appendChild(this.firstResponse);
        container.appendChild(this.secondResponse);
        container.appendChild(this.thirdResponse);
        //scroll down
        let height = chatlogs.scrollHeight;
        setTimeout(function(){message.scrollDown(height);},1000);
    }
    firstResponse = function(parsed){
    //displays parsed answer
    let elemP = document.createElement("p");
    elemP.innerHTML = "Laisse-moi t'en parler un peu :) Tout d'abord, cela se trouve ici :";
    return elemP;
    };

    secondResponse = function(coordinates){
    //inits the map from google map api
    let mapContainer = document.createElement("p");
    let myMap = new google.maps.Map(mapContainer, {
      center: {lat: coordinates[0], lng: coordinates[1]},
      zoom: 16
    });
    //adds a marker
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(coordinates[0], coordinates[1]),
        map: myMap // la variable js représentant la carte
    });
    mapContainer.style.height = "300px";
    mapContainer.style.width = "300px";
    mapContainer.style.margin = "10px auto";
    mapContainer.style.borderRadius = "10% 0%";
    mapContainer.style.overflow = "hidden";

    return mapContainer;
    }

    thirdResponse = function(wikiSum, wikiUrl){
    let elemP = document.createElement("p");
    elemP.maxLength = 100;
    elemP.innerHTML = wikiSum + "<br/> Si d'aventure tu veux plus d'informations <a href='"+ wikiUrl+"' target='_blank'>clique ici</a> !"
    return elemP;
    };
}


