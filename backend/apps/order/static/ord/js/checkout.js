$(document).ready(function() {
            encoded_order_id =window.location.toString().substr(window.location.toString().lastIndexOf("/")+1, 20)
            order_id = atob(encoded_order_id)
            $.ajax({
               type: 'POST',
               data: {csrfmiddlewaretoken: csrftoken},
               url: "\\order\\checkout\\"+encoded_order_id,
               success: function(data) {
                  data = JSON.parse(data);
                  console.log(data);
                    }
            });
});
