var carts = new Array();
var cart;
$(document).ready(function() {
            encoded_order_id =window.location.toString().substr(window.location.toString().lastIndexOf("/")+1, 20)
            order_id = atob(encoded_order_id)
            $.ajax({
               type: 'POST',
               data: {csrfmiddlewaretoken: csrftoken},
               url: "\\order\\checkout\\"+encoded_order_id,
               success: function(data) {
                  cart =carts.concat(data);
                  try {
                     getFoodlist();
                     DrawCartCheckout();
                    } catch (error) {
                    var foodlist;
                     getFoodlist();
                     DrawCartCheckout();
                     }
            }});
});

function DrawCartCheckout(){
        var text="<!--產品1-->";
        for (var i = 0; i < this.cart.length; i++) {
            var Tip="";
             if(cart[i].tip!=null){
             var hereTip=cart[i].tip}
             Tip += "<p>"+String(hereTip)+"</p>"
            var SugIce="";
           if(cart[i].ice!=null || cart[i].sug!=null){
                var hereIce;
                var hereSug;
               try { switch(cart[i].ice) {
                     case "0":
                        hereIce = "去冰";
                        break;
                     case "1":
                        hereIce = "微冰";
                        break;
                     case "2":
                         hereIce = "正常冰";
                        break;
                     default:
                     hereIce = "";
                }
               } catch (error) {var hereIce = ""}
               try {
                    switch(cart[i].sug) {
                         case "0":
                            hereSug = "無糖";
                            break;
                         case "1":
                            hereSug = "微糖";
                            break;
                         case "2":
                             hereSug = "正常糖";
                            break;
                         default:
                            hereSug = "";
                    }
                }catch(error){var hereSug = ""}
                SugIce = `<p>`+hereSug+hereIce+`</p>`
            }
            var addText =`
                <article class="product">
                    <header>
                        <a class="remove" onclick="modifyAmount(2,`+i+`)">
                            <img src="`+foodlist[indexOfFood(cart[i].foodid)].foodImg+`" />
                            <h3>刪除</h3>
                        </a>
                    </header>
                    <div class="content">
                        <h1>`+foodlist[indexOfFood(cart[i].foodid)].foodname+`</h1>

                            `+SugIce+Tip+`

                    </div>
                    <footer class="content">

                        <span class="qt-minus" onclick="modifyAmount(1,`+i+`)">-</span>
                        <span class="qt">`+cart[i].foodAmount+`</span>
                        <span class="qt-plus" onclick="modifyAmount(0,`+i+`)">+</span>

                        <h2 class="full-price">
                            `+cart[i].foodAmount*foodlist[indexOfFood(cart[i].foodid)].foodPrice+`
                        </h2>

                        <h2 class="price">
                            `+foodlist[indexOfFood(cart[i].foodid)].foodPrice+`
                        </h2>
                    </footer>
                </article>`
            text +=addText;

        }
        var totalprice =0;
        for (var i = 0; i < cart.length; i++) {
                totalprice += parseInt(cart[i].foodAmount) * parseInt(foodlist[indexOfFood(cart[i].foodid)].foodPrice)
        }
//        document.getElementById("shopCartTotal").innerHTML=totalprice;
     document.getElementById("cartListDiv").innerHTML=text;
}

  function modifyAmount(operator,fid){
            if(operator==0){
                cart[fid].foodAmount+=1;
            }
            else if(operator==1){
                if(cart[fid].foodAmount>1){
                cart[fid].foodAmount-=1;
                }

            }else if(operator==2){
                cart[fid].foodAmount=0;
                }
            }