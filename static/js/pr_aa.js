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
});
