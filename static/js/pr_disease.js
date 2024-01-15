$(document).ready(function () {
    $("#showTableBtn").on("click", function () {
      $("#dataDescription").hide(); // Hide data description
      $("#card-content").fadeIn(); // Show the table
    });
    $('#crypto_giardia_table').DataTable( {
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

    $('#bELISA_table').DataTable( {
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

      $('#hi_table').DataTable( {
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