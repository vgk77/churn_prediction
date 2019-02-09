function formClear() {
      $("#client_id").val('');
      $("#gender").val('');
      $("#senior").val('');
      $("#partner").val('');
      $("#dependents").val('');
      $("#tenure").val('');
      $("#phone_service").val('');
      $("#multilines").val('');
      $("#internet_service").val('');
      $("#online_security").val('');
      $("#streaming_tv").val('');
      $("#online_backup").val('');
      $("#streaming_movies").val('');
      $("#devprotect").val('');
      $("#support").val('');
      $("#contract").val('');
      $("#paperless").val('');
      $("#payment_method").val('');
      $("#monthly_charges").val('');
      $("#total_charges").val('');
    }
  
  $(document).ready(function(){
    $("#phone_service").change(function(){
      if ($("#phone_service")[0].value == 0){
        $("#multiplelines").val('NO_PHONE');
      }
      else {
        $("#multilines").val('No');
      }
    });

    $("#internet_service").change(function(){
      if ($("#internet_service")[0].value == 'no'){
        $("#online_security").val('no_internet_service');
        $("#online_backup").val('no_internet_service');
        $("#streaming_tv").val('no_internet_service');
        $("#streaming_movies").val('no_internet_service');
        $("#devprotect").val('no_internet_service');
        $("#support").val('no_internet_service');
      }
      else {
        $("#online_security").val('');
        $("#online_backup").val('');
        $("#streaming_tv").val('');
        $("#streaming_movies").val('');
        $("#devprotect").val('');
        $("#support").val('');
      }
    });
  });