$(document).ready(function () {
    $("#showTableBtn").on("click", function () {
      $("#dataDescription").hide(); // Hide data description
      $("#card-content").fadeIn(); // Show the table
    });
    $('#coral_table').DataTable( {
      deferRender: true,
      scrollCollapse: true,
      fixedColumns: true,
      paging: true,
      responsive: true,
      fixedHeader: {
        header: true,
        footer: true,
      },
      paging:true,
      dom: "Bfrtip",
      buttons: [
        {
          extend: 'csv',
          className: 'csv-btn', 
          text: 'Export to CSV' // Optionally change the button text
      }
    ]
    });

    $('#adelie_table').DataTable( {
        deferRender: true,
        scrollCollapse: true,
        fixedColumns: true,
        paging: true,
        responsive: true,
        fixedHeader: {
          header: true,
          footer: true,
        },
        paging: true,
        dom: "Bfrtip",
        buttons: [
          {
            extend: 'csv',
            className: 'csv-btn', 
            text: 'Export to CSV' // Optionally change the button text
        }
      ]
      });

      $('#gentoo_table').DataTable( {
        deferRender: true,
        scrollCollapse: true,
        fixedColumns: true,
        paging: true,
        responsive: true,
        fixedHeader: {
          header: true,
          footer: true,
        },
        paging:true,
        dom: "Bfrtip",
        buttons: [
          {
            extend: 'csv',
            className: 'csv-btn', 
            text: 'Export to CSV' // Optionally change the button text
        }
      ]
      });

      $('#chinstrap_table').DataTable( {
        deferRender: true,
        scrollCollapse: true,
        fixedColumns: true,
        paging: true,
        responsive: true,
        fixedHeader: {
          header: true,
          footer: true,
        },
        paging:true,
        dom: "Bfrtip",
        buttons: [
          {
            extend: 'csv',
            className: 'csv-btn', 
            text: 'Export to CSV' // Optionally change the button text
        }
      ]
      });

      $('#bird_table').DataTable( {
        deferRender: true,
        scrollCollapse: true,
        fixedColumns: true,
        paging: true,
        responsive: true,
        fixedHeader: {
          header: true,
          footer: true,
        },
        paging:true,
        dom: "Bfrtip",
        buttons: [
          {
            extend: 'csv',
            className: 'csv-btn', 
            text: 'Export to CSV' // Optionally change the button text
        }
      ]
      });

      $('#bearblood_table').DataTable( {
        deferRender: true,
        scrollCollapse: true,
        fixedColumns: true,
        paging: true,
        responsive: true,
        fixedHeader: {
          header: true,
          footer: true,
        },
        paging:true,
        dom: "Bfrtip",
        buttons: [
          {
            extend: 'csv',
            className: 'csv-btn', 
            text: 'Export to CSV' // Optionally change the button text
        }
      ]
      });

      $('#bearAbdTemp_table').DataTable( {
        deferRender: true,
        scrollCollapse: true,
        fixedColumns: true,
        paging: true,
        responsive: true,
        fixedHeader: {
          header: true,
          footer: true,
        },
        paging:true,
        dom: "Bfrtip",
        buttons: [
          {
            extend: 'csv',
            className: 'csv-btn', 
            text: 'Export to CSV' // Optionally change the button text
        }
      ]
      });

      $('#bearCapSeq_table').DataTable( {
        deferRender: true,
        scrollCollapse: true,
        fixedColumns: true,
        paging: true,
        responsive: true,
        fixedHeader: {
          header: true,
          footer: true,
        },
        paging:true,
        dom: "Bfrtip",
        buttons: [
          {
            extend: 'csv',
            className: 'csv-btn', 
            text: 'Export to CSV' // Optionally change the button text
        }
      ]
      });
  });
  