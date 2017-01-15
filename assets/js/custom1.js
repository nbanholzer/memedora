function refreshImageUp() {
  $.ajax({
    type: "get",
    dataType:"json"
    url: "/memedora.byethost13.com/up",
    success: function (status) {
        var source = JSON.parse(data);
        document.getElementById('the-meme').src = source;
    }
  });

}

function refreshImageDown() {
  $.ajax({
    type: "get",
    dataType:"json"
<<<<<<< HEAD
    url: "/memedora.byethost13.com/down",
    success: function (status) {
=======
    url: "/htdocs/up.py",
    data: $('Up').serialize(),
    success: function (data, status) {
>>>>>>> 0941e74b19f565b4626f48ce92bc09296d0f4d4d
        var source = JSON.parse(data);
        document.getElementById('the-meme').src = source;
    }
  });

}

function reset() {
  $.ajax({
    type: "get",
    dataType:"json"
<<<<<<< HEAD
    url: "/memedora.byethost13.com/reset",
    success: function (status) {
        console.log('...');
=======
    url: "/htdocs/down.py",
    data: $('Down').serialize(),
    success: function (data, status) {
        var source = JSON.parse(data);
        document.getElementById('the-meme').src = source;
>>>>>>> 0941e74b19f565b4626f48ce92bc09296d0f4d4d
    }
  });

}

//
// $('#reset-btn').click(function(){
//
//  $.ajax({
//       type:'get',
//       url:"/path/to/url/",
//       cache:false,
//       async:asynchronous,
//       dataType:json, //if you want json
//       success: function(data) {
//         console.log('...');
//       },
//       error: function(request, status, error) {
//         console.log('...');
//       }
//    });
// });
