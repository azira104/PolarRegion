$(document).ready(function() {
    $('#Cdata_table').DataTable({
      paging: true, // Enable pagination
      dom: 'Bfrtip',
      buttons: [
        {
          extend: 'csv',
          className: 'csv-btn', 
          text: 'Export to CSV' // Optionally change the button text
      }
    ]
  
    });
    $('#edaphic_table').DataTable({
        paging: true, // Enable pagination
        dom: 'Bfrtip',
        buttons: [
          {
            extend: 'csv',
            className: 'csv-btn', 
            text: 'Export to CSV' // Optionally change the button text
        }
      ]
    
      });
      $('#nucleotide_table').DataTable({
        paging: true, // Enable pagination
        dom: 'Bfrtip',
        buttons: [
          {
            extend: 'csv',
            className: 'csv-btn', 
            text: 'Export to CSV' // Optionally change the button text
        }
      ]
    
      });
  });