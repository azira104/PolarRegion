$(document).ready(function () {
  var table = $("#sulfur_table").DataTable({
    processing: true,
    deferRender: true,
    scrollCollapse: true,
    fixedColumns: true,
    paging: true,
    responsive: true,
    // fixedHeader: {
    //   header: true,
    //   footer: true,
     
    // },
    
    dom: "Bfrtip",
    buttons: ['csv', 'pdf'],
  });
  $(".dataTables_length select, .dataTables_filter input, .dataTables_info, .dataTables_paginate").css('color', 'white');
});
$(".dataTables_paginate .paginate_button.disabled, .dataTables_paginate .paginate_button.disabled:hover, .dataTables_paginate .paginate_button.disabled:active")
    .css({
      cursor: 'default',
      color: 'white',
      border: '1px solid white',
      background: 'white',
      boxShadow: 'none'
    });
    $("div.dt-buttons>.dt-button, div.dt-buttons>div.dt-button-split .dt-button")
    .css({
      color: 'white'
      // Add any other styles for these buttons as needed
    });