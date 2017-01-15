function upDown(yn) {
  $.ajax({
    type: "post",
    dataType:"json",
    url: "http://45.55.226.27/upOrDown:3000",
    data: { yes_no : yn },
    success: function (data) {
        var source = JSON.parse(data);
        document.getElementById('the-meme').src = source;
    }
  });

}
//
// function reset() {
//   $.ajax({
//     type: "get",
//     dataType:"json"
//     url: "/htdocs/down.py",
//     data: $('Down').serialize(),
//     success: function (data, status) {
//         var source = JSON.parse(data);
//         document.getElementById('the-meme').src = source;
//     }
//   });
//
// }

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
