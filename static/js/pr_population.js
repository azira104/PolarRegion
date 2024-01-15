$(document).ready(function () {
    $("#showTableBtn").on("click", function () {
      $("#dataDescription").hide(); // Hide data description
      $("#card-content").fadeIn(); // Show the table
    });
    $('#palmerIter_table').DataTable( {
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

    $('#palmerSize_table').DataTable( {
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

      $('#penguinpopu_table').DataTable( {
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
  