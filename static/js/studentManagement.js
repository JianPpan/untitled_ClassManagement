//*********更新学生管理遮罩层************
function edit_studentManagment(the){
    var sno = $(the).parents("tr").children("td").eq(0).text();
    var sname = $(the).parents("tr").children("td").eq(1).text();
    var spassword = $(the).parents("tr").children("td").eq(2).text();
    var ssage = $(the).parents("tr").children("td").eq(3).text();
    var ssex = $(the).parents("tr").children("td").eq(4).text();
    var politics = $(the).parents("tr").children("td").eq(5).text();
    var phone = $(the).parents("tr").children("td").eq(6).text();
    var homeph = $(the).parents("tr").children("td").eq(7).text();
    var address = $(the).parents("tr").children("td").eq(8).text();
    var cet = $(the).parents("tr").children("td").eq(9).text();
    var compgrade = $(the).parents("tr").children("td").eq(10).text();
    var teachgrade = $(the).parents("tr").children("td").eq(11).text();
    var mandarin = $(the).parents("tr").children("td").eq(12).text();

    $('#updateModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var modal = $(this);
        modal.find('#sno').val(sno);
        modal.find('#sname').val(sname);
        modal.find('#spassword').val(spassword);
        modal.find('#ssage').val(ssage);
        modal.find('#ssex').val(ssex);
        modal.find('#politics').val(politics);
        modal.find('#phone').val(phone);
        modal.find('#homeph').val(homeph);
        modal.find('#address').val(address);
        modal.find('#cet').val("abc");
        modal.find('#compgrade').val(compgrade);
        modal.find('#teachgrade').val(teachgrade);
        modal.find('#mandarin').val(mandarin);
    })
}
//*********更新学生管理遮罩层************
//*********删除功能************
function delete_confirm(){
    var a=confirm("删除学生信息","确认删除？");
    if(a==true)
    {
        alert("已经删除！");
    }
    else
        return false;
}
//*********删除功能************
