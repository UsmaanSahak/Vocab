//Fill the div with id 'choices' with the appropriate choices, depending on if on question or answer.

//if question, then show 'flip'
//if answer, then show 'correct' or 'incorrect' and go to next on their press.

function flip() {
  if ($("#flashcard").attr("class") == "qside") {
    $("#flashcard").attr("class","aside");
    $("#h1qbit").text("A:");
    $("#questionText").hide();
    $("#answerText").show();
    $("#selectRes").show();
    $("#selectFlip").hide();

  }
  else {
    $("#flashcard").attr("class","qside");
    $("#h1qbit").text("Q:");
    $("#questionText").show();
    $("#answerText").hide();
    $("#selectRes").hide();
    $("#selectFlip").show();
  } 
}


function updateEntry(res) {
  flip();
  //displayCards();
  $("#loadingIcon").show();
  id = $("#qid").text();
  type = $("qtype").text();
  if (res == false) {
    //update model with id to binNum == 1 and new date
    console.log(id, " is being changed. False.");
  }
  else if (res == true) { 
    //update model with id to binNum++ and new date 
    console.log(id, " is being changed. True.");
  }
///* //updateEntry uses view

  $("#questionText").text("...");
  $.ajax({
    url: "updateEntry",
    data: {
      id: id,
      res: res,
      type: type 
    },
    success: function(data) {
      console.log("Success!");
      console.log(data);
      if (data["binNum"] == "Temporarily") {
        $("#qid").hide();
        $("#questionText").text("You are temporarily done; please come back later to review more words.");
        $("#answerText").text("");
        $("#binNumText").text(""); 
        $("#dateText").text("");
        $("#selectFlip").hide()
        $("#currStats").hide()
      } 
      if (data["binNum"] == "Permanently") {
        $("#qid").hide();
        $("#questionText").text("You have no more words to review; you are permanently done!");
        $("#answerText").text("");
        $("#binNumText").text(""); 
        $("#dateText").text("");
      }
      else {
        $("#qid").text(data["id"]);
        $("#questionText").text(data["question"]);
        $("#answerText").text(data["answer"]);
        $("#binNumText").text("Bin: " + data["binNum"]); 
        $("#dateText").text(data["month"] + "/" + data["day"] + "/" + data["year"] + ", " + data["hour"] + ":" + data["minute"] + ":" + data["second"]);
      }

    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      console.log(errorThrown);
    } 
  });
}

function displayCards() {
  $.ajax({
      url: "displayCards",
      data: {
      },
      success: function(data) {
        //iterate through data["NewCards"], data["ReviewCards"], and data["OldCards"].
        //For each, fill the dislaycards div
        
        for (var i=0; i < data["NewCards"].size(); i++) {
          var div = document.createElement("div");
          div.classList.add("stacking newcard");
        }
      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
        console.log(errorThrown);
     }
  });
}
