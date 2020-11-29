//*********更新请假管理遮罩层************
function edit_leaveManagment(the){
    var lid = $(the).parents("tr").children("td").eq(0).text();
    var ltype = $(the).parents("tr").children("td").eq(1).text();
    var ltime = $(the).parents("tr").children("td").eq(2).text();
    var ldate = $(the).parents("tr").children("td").eq(3).text();
    var lplace = $(the).parents("tr").children("td").eq(4).text();

    $('#updateModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var modal = $(this);
        modal.find('#lid').val(lid);
        modal.find('#ltype').val(ltype);
        modal.find('#ltime').val(ltime);
        modal.find('#ldate').val(ldate);
        modal.find('#lplace').val(lplace);
    })
//*********更新请假管理遮罩层************
}
function delete_confirm(){
    var a=confirm("删除请假信息","确认删除？")
    if(a==true)
    {
        alert("已经删除！");
    }
    else
        return false;
}
//**************删除功能*********************