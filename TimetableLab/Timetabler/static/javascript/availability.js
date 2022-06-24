for (const period of list){
    let id='#'+period
    $('#'+period).prop('checked', true);
    $('#cell-'+period).addClass('bg-success')
}
$('.form-check-input').change(function(){
    if(this.checked){
        $('#cell-'+this.id).addClass('bg-success')
    }else{
        $('#cell-'+this.id).removeClass('bg-success')
    }
});

$('#selectAll').click(function(){
    $('.form-check-input').prop('checked', true);
    $('.table-cell').addClass('bg-success');
});

$('#clearSelect').click(function(){
    $('.form-check-input').prop('checked', false);
    $('.table-cell').removeClass('bg-success');
});

