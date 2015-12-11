/*
 * kintone javaScriptカスタマイズのテンプレート
 * 
 * Licensed under the MIT License
 */
(function() {
    "use strict";
    
    //プロセス管理のアクション実行イベント(pc)
    kintone.events.on("app.record.detail.process.proceed", function(event){
        var targetAppId = "16";
        var linkedField = "wkLookup"; //lookup field in the target app.
        var linkedStatusField = "status";
        
        var status = event.status.value;
        var nextStatus = event.nextStatus.value;
        if(status == nextStatus){
            return true; // nothing to do
        }
        
        var myId = event.record["$id"]["value"];
        var query = linkedField + " = " + myId;
        var extractTargets = kintone.api("/k/v1/records", "GET", {app: targetAppId, fields: ["レコード番号"], query: query});
        extractTargets.then(function(resp){
            if(resp["records"].length == 0){
                return true;
            }
            
            var records = [];
            for(var i = 0; i < resp["records"].length; i++){
                var rId = resp["records"][i]["レコード番号"]["value"];
                var r = {};
                r[linkedStatusField] = {"value": nextStatus};
                records.push({
                    "id": rId,
                    "record": r
                })
            }
            
            var data = {
                "app": targetAppId,
                "records": records
            };
            kintone.api("/k/v1/records", "PUT", data).then(function(result){
                console.log("update related records.");
            })
            
        })
    });
    
})();
