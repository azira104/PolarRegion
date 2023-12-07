$(document).ready(function () {
  $("#showTableBtn").on("click", function () {
    $("#dataDescription").hide(); // Hide data description
    $("#hero2").fadeIn(); // Show the table
  });
  $('#sulfur_table').DataTable( {
    deferRender: true,
    scrollCollapse: true,
    fixedColumns: true,
    paging: true,
    responsive: true,
    fixedHeader: {
      header: true,
      footer: true,
    },

    dom: "Bfrtip",
    buttons: ["csv", "pdf"],
  });

  // $(document).ready(function () {
  //   $(
  //     "div.dt-buttons>.dt-button, div.dt-buttons>div.dt-button-split .dt-button"
  //   ).css({
  //     color: "white",
  //     // Add any other styles for these buttons as needed
  //   });
  //   $(
  //     ".dataTables_paginate .paginate_button.disabled, .dataTables_paginate .paginate_button.disabled:hover, .dataTables_paginate .paginate_button.disabled:active"
  //   ).css({
  //     cursor: "default",
  //     color: "white",
  //     border: "1px solid white",
  //     background: "white",
  //     boxShadow: "none",
  //   });
  //   $(
  //     ".dataTables_length select, .dataTables_filter input, .dataTables_info, .dataTables_paginate"
  //   ).css("color", "white");
  // });
});
