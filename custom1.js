function upDown(yny) {
  $.ajax({
    type: "get",
    dataType:"json"
    url: "http://40.55.226.27:3000/up",
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
    url: "/memedora.byethost13.com/down",
    success: function (status) {
        var source = JSON.parse(data);
        document.getElementById('the-meme').src = source;
    }
  });

}

function reset() {
  $.ajax({
    type: "get",
    dataType:"json"
    url: "/memedora.byethost13.com/reset",
    success: function (status) {
        console.log('...');
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
