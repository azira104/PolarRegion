$(document).ready(function () {
    $("#showTableBtn").on("click", function () {
      $("#dataDescription").hide(); // Hide data description
      $("#card-content").fadeIn(); // Show the table
    });
    $('#climate_table').DataTable( {
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

    $('#iceextent_table').DataTable( {
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

      $('#simpsonlagoon_table').DataTable( {
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

      $('#streamgages_table').DataTable( {
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
  