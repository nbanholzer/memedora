function setFirstPref() {
  $.ajax({
    type: "post",
    dataType:"text"
    url: "/cgi-bin/python1.py",
    data: {param : text},
    success: function (data, status) {
        var source = JSON.parse(data);
        window.location.href = "b2.html";
        document.getElementById('the-meme').src = source;
    }
  });

}

function refreshImageUp() {
  $.ajax({
    type: "get",
    dataType:"json"
    url: "/cgi-bin/python1.py",
    data: $('Up').serialize(),
    success: function (data, status) {
        var source = JSON.parse(data);
        document.getElementById('the-meme').src = source;
    }
  });

}

function refreshImageDown() {
  $.ajax({
    type: "get",
    dataType:"json"
    url: "/cgi-bin/python1.py",
    data: $('Down').serialize(),
    success: function (data, status) {
        var source = JSON.parse(data);
        document.getElementById('the-meme').src = source;
    }
  });

}

function resetVars() {
  $.ajax({
    type: "POST",
    url: "~/pythoncode.py",
    data: { param: text}
  }).done(function( o ) {
   // do something
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
