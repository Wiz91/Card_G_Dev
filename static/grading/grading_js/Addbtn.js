var btnCount = 0;
var btnRemove = 0;
function add(){
        btnRemove--;
        btnCount++;
        if(btnRemove === 1) {
          var btn = document.getElementById('remove-btn');
           btn.disabled = false;
           }
        if(btnCount > 5) {
       var btn = document.getElementById('add-move-button');
        btn.disabled = true;
        var btn = document.getElementById('remove-btn');
        btn.disabled = false;
        }
    var new_chq_no = parseInt($('#total_chq').val())+1;
    var new_input="<div id='new_"+new_chq_no+"' class='flx' ><input type='text'  name='Key"+new_chq_no+"' placeholder='Add details"+new_chq_no+"'  class='form-control mr27'><input type='text'  name='Value"+new_chq_no+"' placeholder='Add details"+new_chq_no+"' class='form-control'></div>";
    
   
    $('#new_chq').append(new_input);
    $('#total_chq').val(new_chq_no)
  }


  function remove(){
    btnCount--;
    btnRemove++;
        if(btnCount < 4) {
       var btn = document.getElementById('add-move-button');
        btn.disabled = false; 
        }
        
        if(btnRemove > 1) {
          var btn = document.getElementById('remove-btn');
           btn.disabled = true;
           }
    var last_chq_no = $('#total_chq').val();
    if(last_chq_no>1){
      $('#new_'+last_chq_no).remove();
      $('#total_chq').val(last_chq_no-1);
    }
  }