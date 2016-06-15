var socket = io.connect('http://147.91.203.60:3001/client-home');
var link = '#';
var slobodno = false;
socket.on('slobodno', function(data){
  if ($('#dugme').hasClass('disabled')){
    $('#dugme').removeClass('disabled');
  }
  $('#vreme').hide();
  $('#vremeOpis').hide();
  link = data;
  slobodno = true;
  console.log(data);
});
socket.on('zauzeto', function(data){
  $('#vremeOpis').show();
  $('#vreme').show();
  $('#vreme').text(data);
  if (!$('#dugme').hasClass('disabled')){
    $('#dugme').addClass('disabled');
    link = '#'
    slobodno = false;
  }
  console.log(data);
});

$(document).ready(function(){
  if (!$('#dugme').hasClass('disabled')){
    $('#dugme').addClass('disabled');
  }
  $('#dugme').click(function(dugme){
    if (slobodno) {
      dugme.preventDefault();
      window.location.href = 'http://147.91.203.60:3001/lab/' + link;
      console.log('zasto');
    }
  });
});
