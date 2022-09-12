let totalForms = $("#id_form-TOTAL_FORMS");

let formNum = $('.moduleForm').length;
var tempId = 0;

console.log(currentModulePeriods)

console.log($('#add-form-1'));


$(document).ready(function(){
    for (period in currentModulePeriods){
        let btn = '#add-form-' + currentModulePeriods[period];
        $(btn).click();
        $('#'+tempId).val(currentModuleNames[period]);

    }
})



$(".addFormButton").click(function(){
    addForm(this);
});

function addForm(e){
    //Setup
    let cellNum = parseInt(e.parentElement.id.match(/[0-9]+$/));
    let cellId = "#" + e.parentElement.id;
    if(formNum===0){
        var newForm = document.createElement('span');
        newForm.classList.add("moduleFormSpan")
        newForm.innerHTML=`
        <input type="text" name="form-0-moduleName" placeholder="Enter a Module" class="form-control moduleForm" id="name-1-1">
        <input type="text" name="form-0-modulePeriod" value="mon-1" id="period-1-1" hidden="True">
        <input type="number" name="form-0-moduleWeek" value="1" hidden="True">
        </br>
        `
    }else{
        var newForm = $('.moduleFormSpan')[0].cloneNode(true);
    }
    let moduleCount = $(cellId + " .moduleForm").length+1;
    let formCount = formNum-1;
    let newId = cellNum + "-" + moduleCount;
    let newName = "form-" + formNum + "-module";
    newForm.children[0].setAttribute('id', "name-" + newId);
    newForm.children[0].setAttribute('name', newName + "Name");
    newForm.children[1].setAttribute('id', "period-" + newId);
    newForm.children[1].setAttribute('name', newName + "Period");
    newForm.children[2].setAttribute('name', newName + "Week");
    newForm.children[0].value='';
    if(cellNum<26){
        newForm.children[1].setAttribute('value', periods[cellNum-1]);
        newForm.children[2].setAttribute('value', 1);
    }else{
        newForm.children[1].setAttribute('value', periods[cellNum-26]);
        newForm.children[2].setAttribute('value', 2);
    }
    e.parentElement.insertBefore(newForm, e);
    formNum++;
    totalForms.val(formNum);
    tempId =  "name-"+newId;
}