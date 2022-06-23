// $(document).ready(function () {
//   $('form').on('submit', function (event) {
//     var Generate = $('#Generate-Text').val();
//     // alert(Generate)
//     $.ajax({
//       // type: 'POST',
//       url: '/predict',
//       data: $('form').serialize(),
//       contentType: 'application/json',
//       success: function (data) {
//         console.log(data);
//         // alert("sucess" + data)
//       },
//       error: function (data) {
//         // alert("error " + data.error);
//       }
//     })
//       .done(function (data) {
//         if (data.error) {
//           $('#error-alert').text(data.error).show();
//         }
//         else {
//           $('#success-alert').text(data.Generate).show();
//         }
//       });

//     event.preventDefault();
//   });

// })


$('form').on('submit', function (event) {
  var text=$("#Generate-Text").val()
  $.ajax({
    type: 'GET',
    url: 'http://127.0.0.1:5000//prediction1/'+text,
    datatype:'json',
    crossdomain:true,
    success: function (data) {
      // Process on success
       console.log(data);
      $('#greedy-method').text(data).show();
    
    },
    error: function (data) {
    }
  });
  $.ajax({
    type: 'GET',
    url: 'http://127.0.0.1:5000//prediction2/'+text,
    datatype:'json',
    crossdomain:true,
    success: function (data) {
      // Process on success
      console.log(data);
     $('#top-k-sampling').text(data).show();
    
    },
    error: function (data) {
    }
  });
  $.ajax({
    type: 'GET',
    url: 'http://127.0.0.1:5000//prediction3/'+text,
    datatype:'json',
    crossdomain:true,
    success: function (data) {
      // Process on success
      console.log(data);
     $('#generic-sampling').text(data).show()
    },
    error: function (data) {
    }
  });
  event.preventDefault();
});