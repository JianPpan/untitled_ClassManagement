//*********更新活动管理遮罩层************
function edit_activityManagment(the){
    var aid = $(the).parents("tr").children("td").eq(0).text();
    var atype = $(the).parents("tr").children("td").eq(1).text();
    var atime = $(the).parents("tr").children("td").eq(2).text();
    var members = $(the).parents("tr").children("td").eq(3).text();

    $('#updateModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var modal = $(this);
        modal.find('#aid').val(aid);
        modal.find('#atype').val(atype);
        modal.find('#atime').val(atime);
        modal.find('#members').val(members);
    })
//*********更新活动管理遮罩层************
}
function delete_confirm(){
    var a=confirm("删除活动信息","确认删除？")
    if(a==true)
    {
        alert("已经删除！");
    }
    else
        return false;
}
//**************删除功能*********************