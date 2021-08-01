
//購物車==================================================================

//行動裝置：當視窗小於374時運作----
var csrftoken = $("[name=csrfmiddlewaretoken]").val();
if ($(window).width() < 376) {

    //位置在下，刪除top的樣式
    $('.shopCart').css({
        "bottom": "3rem",
        "top": "",
    });

}
else {

    //位置在上，刪除bottom樣式
    $('.shopCart').css({
        "top": "2.8rem",
        "bottom": "",
    });

}





$(function () {  
    
    //行動裝置：當視窗小於1024時運作---- 
    if ($(window).width() < 1025) {

        //購物車顯示/隱藏
        $('.navShopCart').click(function () {
            $('.shopCart').toggle('slow');
        });
    }
    

    //網頁版：
    $('.navShopCart').hover(function () {
        $('.shopCart').show('slow');
    });

    $('.shopCart').hover(function () {
        //滑鼠移入事件

    }, function () {
        //滑鼠移出事件--------

        //隱藏購物車
        $('.shopCart').hide();

    });
    
    
});

main();

function main() { 

    NoItemCart();
}



//無商品的購物車--------------------------------
function NoItemCart() {
    var cartCount = document.getElementsByClassName("shopCartItem");

    if (cartCount.length <= 0) {
        //購物車無商品
        $('.noItem').show();
        $('.shopCartFooter').hide();
    }
    else {
        //購物車有商品
        $('.noItem').hide();
        $('.shopCartFooter').show();
    }
}
function checkout(){
            if (cart.length == 0) {
                alert("请至少點一道菜！");
                return;
            }


            $.ajax({
               type: 'POST',
               url: "\\order\\product",
               data: {cart:JSON.stringify(cart),csrfmiddlewaretoken: csrftoken},
               success: function(data) {
                        // 加载新的页面 (订单页) url: /order/q{order_id}

                        data = JSON.parse(data);
                        oid = data["order_id"];
                        console.log(data);
                        $(location).attr(
                            "href",
                            "/order/checkout/"+String(oid)
                        );
                    }
            });
       }
function comfirmOrder(){
            encoded_order_id =window.location.toString().substr(window.location.toString().lastIndexOf("/")+1, 19)
            order_id = atob(encoded_order_id)
            $.ajax({
               type: 'POST',
               data: {csrfmiddlewaretoken: csrftoken},
               url: "\\order\\checkout\\"+encoded_order_id,
               success: function(data) {
                    }
            });
       }
