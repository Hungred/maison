    var cart = new Array();
    var foodcount = 0;
    function modifyAmount(operator,fid){
            if(operator==0){
                curAmount = parseInt(document.getElementById("quantityTextbox-"+String(fid)).value, 10)
                curAmount -=1;
                if(curAmount ==0){
                curAmount =1;}
                document.getElementById("quantityTextbox-"+String(fid)).value = curAmount;
            }
            else if(operator==1){
                curAmount = parseInt(document.getElementById("quantityTextbox-"+String(fid)).value, 10)
                curAmount +=1;
                document.getElementById("quantityTextbox-"+String(fid)).value = curAmount;
            }else if(operator==2){
                curAmount = parseInt(document.getElementById("ItemQuantity-"+String(fid)).innerHTML)
                curAmount -=1;
                if(curAmount ==0){
                curAmount =1;}
                cart[fid].foodAmount=curAmount;
                drawCart();
            }else if(operator==3){
                curAmount = parseInt(document.getElementById("ItemQuantity-"+String(fid)).innerHTML)
                curAmount +=1;
                cart[fid].foodAmount=curAmount;
                drawCart();
            }

    }
    function addtocart(fid){
        var item = {};
        item.foodid = String(fid);
        curFoodAmount=parseInt(document.getElementById("quantityTextbox-"+String(fid)).value, 10);
        item.foodAmount = curFoodAmount;
        var ice = document.getElementById("iceOption-"+fid)
        var sug = document.getElementById("sugOption-"+fid)
        if(ice!=null){
            item.ice = ice.value;
        }else{
            ice = "null";
            item.ice = null;
        }
        if(sug!=null){
            item.sug = sug.value;
        }else{
            sug = "null";
            item.sug = null;
        }
        curFoodTip= document.getElementById("tip-"+String(fid)).value.replace(" ", "");
        item.tip = curFoodTip;
        var present = presentOfFood(String(fid),ice.value,sug.value,curFoodTip);
        if(present!=null){cart[present].foodAmount += curFoodAmount;
        }else{cart.push(item);}

        document.getElementById("quantityTextbox-"+String(fid)).value=1;
        document.getElementById("tip-"+String(fid)).value=null;
        drawCart();}
    function removeCartItem(index){
    cart.splice(index,1);
    drawCart();
    }
    function drawCart(){
        var text="";
        for (var i = 0; i < cart.length; i++) {
            var Tip="";
             if(cart[i].tip!=null){
             var hereTip=cart[i].tip}
             Tip += "<p>"+String(hereTip)+"</p><br>"
            var SugIce="";
            if(cart[i].ice!=null && cart[i].sug!=null){
                var hereIce;
                var hereSug;
                switch(cart[i].ice) {
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
                }
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
                }
                SugIce = `<p>`+hereSug+hereIce+`</p>`
            }

            var addText = `<div class="shopCartItem">
                            <a href="#">
                            <img src="`+foodlist[indexOfFood(cart[i].foodid)].foodImg+`" />

                            <div>
                                <p>`+foodlist[indexOfFood(cart[i].foodid)].foodname+`</p>`+SugIce+Tip+`
                                <span>$`+foodlist[indexOfFood(cart[i].foodid)].foodPrice+`</span>
                            </div>
                            </a>
                            <span>
                                    <button type="button" class="quantity-left-minus btn" data-type="minus" onclick="modifyAmount(2,'`+i+`')">
                                        <i class="fas fa-minus"></i>
                                    </button>
                                </span>
                                <span class="ItemQuantity" id="ItemQuantity-`+i+`">`+cart[i].foodAmount+`</span>
                                <span>
                                    <button type="button" class="quantity-right-plus btn" data-type="plus" onclick="modifyAmount(3,'`+i+`')">
                                        <i class="fas fa-plus"></i>
                                    </button>
                            </span>

                        <button class="DelBtn btn btn-outline-secondary" onclick="removeCartItem(`+i+`)"><span class="fas fa-trash-alt"></span></button>

                    </div>`
            text +=addText;
        }
        var totalprice =0;
        for (var i = 0; i < cart.length; i++) {
                totalprice += parseInt(cart[i].foodAmount) * parseInt(foodlist[indexOfFood(cart[i].foodid)].foodPrice)
        }
        document.getElementById("shopCartTotal").innerHTML=totalprice;
     document.getElementById("shopCartContent").innerHTML=text;}