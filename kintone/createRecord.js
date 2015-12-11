/*
 * 任意のフォームからデータを受け取り、別のアプリにレコードの登録を行う
 * 
 * Variables:
 *   targetAppId: レコード登録先のアプリID
 *   data: 登録するデータをディクショナリ形式で受け取る(ターゲットのアプリのフィールドとマッチしない場合、エラーとなる)
 * 
 * Licensed under the MIT License
 */
(function(global) {
    "use strict";
    
    //指定したアプリにレコードを登録する処理
    global.createRecord = function(targetAppId, data){
        var _data = {
            "app": targetAppId,
            "record": {}
        };
        for(var k in data){
            _data["record"][k] = {
                "value": data[k]
            };
        }
        
        return kintone.api("/k/v1/record", "POST", _data);
    }
    
    //一覧にフォームを追加
    kintone.events.on("app.record.index.show", function(event){
        var TARGET_APP_ID = "24";        
        var el = kintone.app.getHeaderSpaceElement();
        var form = "";
        form += '<div id="inputForm">';
        form += '<input id="inputText" class="input-text-cybozu" type="text" value="" autocomplete="off" placeholder="WF名">';
        form += '<button id="createWF" type="button" >CREATE</button>';
        form += '</div>';
        $(el).append(form);
        
        $("#createWF").click(function(){
            var text = $("#inputText").val();
            if(text != ""){
                var data = {
                    "name": text
                };
                createRecord(TARGET_APP_ID, data).then(function(resp){
                    console.log("create record");
                });
            }
        })
    });
       
}(this));
