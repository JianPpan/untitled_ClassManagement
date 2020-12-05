//*********更新班费管理遮罩层************
function edit_classFeeManagment(the) {
    var fid = $(the).parents("tr").children("td").eq(0).text();
    var famount = $(the).parents("tr").children("td").eq(1).text();
    var fdate = $(the).parents("tr").children("td").eq(2).text();

    $('#updateModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var modal = $(this);
        modal.find('#fid').val(fid);
        modal.find('#famount').val(famount);
        modal.find('#fdate').val(fdate);
    })
}
//*********更新班费管理遮罩层************

function delete_confirm(){
    var a=confirm("删除班费信息","确认删除？")
    if(a==true)
    {
        alert("已经删除！");
    }
    else
        return false;
}
//**************删除功能*********************