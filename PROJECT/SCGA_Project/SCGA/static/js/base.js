"strict";
// get csrftoken
// const getCookie = function (name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie != "") {
//         let cookies = document.cookie.split(";");
//         for (let i = 0; i < cookies.length; i++) {
//             let cookie = jQuery.trim(cookies[i]);
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) == name + "=") {
//                 cookieValue = decodeURIComponent(
//                     cookie.substring(name.length + 1)
//                 );
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// };

// let csrftoken = getCookie("csrftoken");
// get cookie using jQuery <js.cookie.min.js>
const csrftoken = Cookies.get("csrftoken");
console.log(csrftoken);
// console.log("loaded");
console.log($("input[name=csrfmiddlewaretoken]").val());

// Ajax call
const crsfSafeMethod = function (method) {
    // there HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
};

$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function (xhr, settings) {
        if (!crsfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    },
});

const importBtn = $("#importBtn");
const submitBtn = $("#submitBtn");
const submitForm = function () {
    // fetch form data
    $project = $("#project-name").val();
    $func = $("#function-name").val();
    $load = $("#load-id").val();
    if ($project && $func && $load) {
        // create JSON object
        data = {
            project: $project,
            function: $func,
            load: $load,
            // csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        };
        // send AJAX request
        $.ajax({
            url: "insert", // url that send request
            type: "POST", // type of request （GET|POST|PUT|DELETE)
            data: JSON.stringify(data), // data that request to send to server
            contentType: "application/json", // content that request, set 'application/json' if using json data
            // dataType: "json", // data type that server response
            success: function () {
                alert("Data saved !");
                $("#project-name").val("");
                $("#function-name").val("");
                $("#load-id").val("");
                window.location = "/";
            },
            error: function (xhr, status, error) {
                // logic for request error
                alert("request error: " + error);
            },
        });
    } else {
        alert("Please complete field");
    }
};

// importBtn.click(function (e) {
//     console.log("Form submit");
// });
$(document).ready(function () {
    submitBtn.on("click", submitForm);
});
