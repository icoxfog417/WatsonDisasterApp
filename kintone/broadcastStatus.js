/*
 * アプリAからWFアプリBにLOOKUPでリンクが張ってある場合に、アプリB側でWFのステータスを更新するとアプリA側でLOOKUPによりBを参照しているレコードのステータスフィールドを更新する
 * 
 * Variables: 
 *   LOOKUP_APP_ID: LOOKUPしている側のアプリ番号
 *   WF_LOOKUP_FIELD: WFをLOOKUPしているフィールド名(※レコード番号が入っている必要あり)
 *   LINKED_STATUS_FIELD: WFのステータスを格納するフィールド
 * 
 * Licensed under the MIT License
 */
(function() {
    "use strict";
    
    //プロセス管理のアクション実行イベント(pc)をハンドル
    kintone.events.on("app.record.detail.process.proceed", function(event){
        var LOOKUP_APP_ID = "323";
        var WF_LOOKUP_FIELD = "wkLookup"; //lookup field in the target app.
        var LINKED_STATUS_FIELD = "status";
        
        var status = event.status.value;
        var nextStatus = event.nextStatus.value;
        if(status == nextStatus){
            return true; // nothing to do
        }
        
        var myId = event.record["$id"]["value"];
        var query = WF_LOOKUP_FIELD + " = " + myId;
        var extractTargets = kintone.api("/k/v1/records", "GET", {app: LOOKUP_APP_ID, fields: ["レコード番号"], query: query});
        extractTargets.then(function(resp){
            if(resp["records"].length == 0){
                return true;
            }
            
            var records = [];
            for(var i = 0; i < resp["records"].length; i++){
                var rId = resp["records"][i]["レコード番号"]["value"];
                var r = {};
                r[LINKED_STATUS_FIELD] = {"value": nextStatus};
                records.push({
                    "id": rId,
                    "record": r
                })
            }
            
            var data = {
                "app": LOOKUP_APP_ID,
                "records": records
            };
            kintone.api("/k/v1/records", "PUT", data).then(function(result){
                console.log("update related records.");
            })
        })
    });
    
})();
