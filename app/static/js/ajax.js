class AjaxRequest{
  // **********SEND request
  ajax = function(url, msg) {
    return new Promise(function (resolve, reject) {
      let req = new XMLHttpRequest()
      req.open('POST', url, true)
      req.setRequestHeader("Content-Type", "application/json");
      req.onreadystatechange = function() {
        if (req.readyState == 4) {
           if(req.status == 200)
             resolve(req.responseText)
           else
             reject(req)
        }
      };
      let jsonBody = { "message" : msg};
      req.send(JSON.stringify(jsonBody));
    })
  }
  // ********** GET RESPONSE
  getResponse = async function(url, msg){
    let response = await this.ajax(url, msg);
    response = JSON.parse(response)
    console.log(response)

    return response
  }
  // ********* GPB THINKS
  thinkngGPB = function(url, msg){
    this.getResponse(url, msg).then(function(response){
      let message = response.message
      // let coordinates = response.coordinates
      // let extractWiki = "response.extractWiki à venir"
      return message, coordinates, extractWiki
  });
}

}







