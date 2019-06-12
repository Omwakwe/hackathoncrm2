$(document).ready(function() {
  // using jQuery
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  var csrftoken = getCookie("csrftoken");

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
  }

  $("#book_room_form").on("submit", function(event) {
    event.preventDefault();
    // $("#save_booking").removeClass("btn-success");
    // $("#save_booking").addClass("btn-default");

    $("#save_booking").prop("disabled", true);
    console.log("book_room_form called");
    save_booking();
  });

  function save_booking() {
    var formdata = $("#book_room_form").serializeArray();
    $.ajax({
      url: "/booking/",
      type: "POST",
      data: formdata,

      success: function(json) {
        //Display row results from database
        // $("#save_booking").removeClass("btn-default");
        // $("#save_booking").addClass("btn-success");
        // $("#save_booking").html("Save");
        $("#save_booking").prop("disabled", false);
        console.log("json", json);

        //call the function that returns a string('verdict') to check if
        //errors present. If no errors, we proceed to print rows(table)
        // returned_verdict = success_checker(json.success, json.success_msg);
      },
      error: function(xhr, errmsg, err) {
        //remove loading gif, enable add button
        $("#save_booking").prop("disabled", false);
      }
    });
  } //end

  //CSRF protetction for Django to work with Ajax
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
});