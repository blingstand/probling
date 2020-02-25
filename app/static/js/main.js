//my var
// let myQuestion = "as-tu des informations sur bordeaux ?";

let message = new Message()
//I need the url
let url = document.location.href + "index/question";

let validate = function(event){
    //starts a search when user push entry (keyCode = 13)
    if(event.keyCode == 13){
        InteractionWithGPB()
    }
}
//main =)
let InteractionWithGPB = function(){
    let triangle = document.getElementById('triangle')
    triangle.style.display="block"
    triangle.classList.add('animation')
    console.log("searching ...")

    //user asks a question
    let myQuestion = message.getMessage("myInput");
    message.question(myQuestion);
    let height = chatlogs.scrollHeight;
    setTimeout(function(){message.scrollDown(height)},1000);
    //grandPy thinks
    const ajaxRequest = new AjaxRequest();
    gPBMemory = ajaxRequest.getResponse(url, myQuestion);

    //grandPy answers if he can
    timeoutID = window.setTimeout(function(){
      gPBMemory.then(function(resp){
          lastChatMessage = message.response();
          if (resp["is_response"]){
          const responseGPB = new Response(resp);
          console.log(resp)
          responseGPB.greatMessage(lastChatMessage);
          }else{
              lastChatMessage.textContent = resp['message']
              let chatlogsSize = chatlogs.scrollHeight;
              
              message.scrollDown(chatlogsSize); 
          }
        })
      triangle.classList.remove("animation");
      triangle.style.display="none"
      console.log("disparition")

    }, 2*1000)

    
}
