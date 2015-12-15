/*
 * 任意のフォームから検索したレコードのルックアップフィールドを更新する
 * 
 * Variables:
 *   SEARCH_TARGET_FIELDS: 検索対象のフィールドの配列
 *   CREATE_FORM: フォームを作成する関数
 *   FORM_TO_DATA: 作成したフォームから検索/更新用データを抽出する処理
 *   LOOKUP_FIELD: 更新するルックアップフィールド
 * 
 * Licensed under the MIT License
 */
(function(global) {
    "use strict";

    //指定したキーワードでアプリ内を検索する
    global.searchRecords = function(keywords, searchFields){
        var appId = kintone.app.getId();
        var query = searchFields.map(function(f){
                        var cond = keywords.map(function(k){ return f + ' like "' + k + '"' }).join(" and ");
                        return "(" + cond + ")";
                    }).join(" or ");

        var data = {
            "app": appId,
            "query": query
        };

        return kintone.api("/k/v1/records", "GET", data)
    }

    //指定したidsのレコードを更新する
    global.updateLookup = function(records, lookupId){
        var LOOKUP_FIELD = "wkLookup";
        var appId = kintone.app.getId();

        var data = {
            "app": appId,
            "records": []
        }

        for(var i = 0; i < records.length; i++){
            var u = {}
            u[LOOKUP_FIELD] = {
                "value": lookupId
            }
            data["records"].push({
                "id": records[i]["$id"]["value"],
                "record": u
            })
        }

        return kintone.api("/k/v1/records", "PUT", data)
    }

    //一覧にフォームを追加
    kintone.events.on("app.record.index.show", function(event){
        var SEARCH_TARGET_FIELDS = ["title", "description"];
        var CREATE_FORM = function(targetElement){
            var form = "";
            form += '<div id="inputForm">';
            form += '<input id="inputText" class="input-text-cybozu" type="text" value="" autocomplete="off" placeholder="WF名">';
            form += '<button id="searchAndUpdate" type="button" >SEARCH & UPDATE</button>';
            form += '</div>';
            $(targetElement).append(form);
        }
        var FORM_TO_DATA = function(){
            var text = $("#inputText").val();
            return text;
        };

        var el = kintone.app.getHeaderSpaceElement();
        CREATE_FORM(el);

        $("#searchAndUpdate").click(function(){
            var text = FORM_TO_DATA();
            if(text != ""){
                var keywords = text.replace(/　/g, " ").split(" ");
                searchRecords(keywords, SEARCH_TARGET_FIELDS).then(function(resp){
                    var wfid = 2;  //have to set created record
                    updateLookup(resp["records"], wfid).then(function(result){
                         console.log("success.");
                     }, function(err){
                         console.log("failed.");
                     });
                });
            }
        })
    });
       
}(this));
