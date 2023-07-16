"strict";

console.log("loaded");
// get cookie using jQuery <js.cookie.min.js>
const csrftoken = Cookies.get("csrftoken");
console.log(csrftoken);
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
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            // csrfmiddlewaretoken: csrftoken,
        };
        // send AJAX request
        $.ajax({
            url: "importData", // url that send request
            type: "POST", // type of request （GET|POST|PUT|DELETE)
            data: JSON.stringify(data), // data that request to send to server
            contentType: "application/json", // content that request, set 'application/json' if using json data
            // dataType: "json", // data type that server response
            success: function () {
                alert("Data saved !");
                console.log(data);
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
    $("#scTable1").DataTable();
    $("#scTable2").DataTable();
    submitBtn.on("click", submitForm);
});
