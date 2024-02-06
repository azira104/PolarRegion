$(document).ready(function() {
  $('#simpsonlagoon_table').DataTable({
    "paging": true,  // Enable pagination
    "pageLength": 10,  // Number of rows per page
    "lengthMenu": [10, 25, 50, 75, 100],  // Rows per page options
    "info": true,  // Show info (pagination controls)
  });
});