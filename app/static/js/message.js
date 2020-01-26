class Message{

    question(msg){
        //creates elements to ask a question
        myInput.value = "";

        // creates container and content in chatlogs with message from msgforGPB
        let selfChat = document.createElement("div");
        let userPhoto = document.createElement("div");
        let selfMessage = document.createElement("p");

        //class from css
        // container.classList.add('container');
        selfChat.classList.add('Self');
        selfChat.classList.add('chat');
        userPhoto.classList.add("SELF-photo");
        selfMessage.classList.add('chat-message');

        //fills content
        selfMessage.textContent = msg;

        //appends new elements
        chatlogs.appendChild(selfChat);
        selfChat.appendChild(userPhoto);
        selfChat.appendChild(selfMessage);
    };
    response(){
        //creates element to answer
        let gPBChat = document.createElement("div");
        let userPhoto = document.createElement("div");
        let gPBMessage = document.createElement("p");

        //class from css
        // container.classList.add('container');
        gPBChat.classList.add('GPB');
        gPBChat.classList.add('chat');
        userPhoto.classList.add("GPB-photo");
        gPBMessage.classList.add('chat-message');


        //appends new elements
        chatlogs.appendChild(gPBChat);
        gPBChat.appendChild(userPhoto);
        gPBChat.appendChild(gPBMessage);

        //returns id of gPBMessage
        let classNameChatMessage = document.getElementsByClassName("chat-message");
        let lastChatMessage =  classNameChatMessage[classNameChatMessage.length - 1];
        lastChatMessage.style.margin_top="5px";


        return lastChatMessage

    }
    getMessage(element){
        //gets elements from input
        let myInput = document.getElementById(element);

        let msgforGPB = myInput.value;

        return msgforGPB
    }

    scrollDown = function (level){
        let chatLogs = document.getElementById("chatlogs");
        chatlogs.scrollTo(0, level);
    }
}
