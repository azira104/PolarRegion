$(document).ready(function () {
    $("#showTableBtn").on("click", function () {
      $("#dataDescription").hide(); // Hide data description
      $("#card-content").fadeIn(); // Show the table
    });
    $('#hotpoints_table').DataTable( {
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

    $('#antarticmass_table').DataTable( {
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
  