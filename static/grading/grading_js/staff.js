
      $(document).ready(function(){
        $("#link").ready(function(){
          $("#test").show();
          $("#demo").hide();
          $("#myform").hide();
        });
      });
    

    
    $(document).ready(function(){
      $("#link").click(function(){
        $("#test").show();
        $("#demo").hide();
        $("#myform").hide();
      });
    });
    
  $(document).ready(function(){
    $("#same").click(function(){
      $("#demo").show();
      $("#test").hide();
      $("#myform").hide();
    });
  });
  

    $(document).ready(function(){
      $("#add").click(function(){
        $("#myform").show();
        $("#test").hide();
        $("#demo").hide();
      });
    });
