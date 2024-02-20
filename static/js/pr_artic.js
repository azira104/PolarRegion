$(document).ready(function() {
  $('#simpsonlagoon_table').DataTable({
    paging: true,  // Enable pagination
    pageLength: 10,  // Number of rows per page
    lengthMenu: [10, 25, 50, 75, 100],  // Rows per page options
    info: true,  // Show info (pagination controls)
  });

  $(document).ready(function() {
    $('#streamgages_table').DataTable({
      paging: true, // Enable pagination
      buttons: [
        {
          extend: 'csv',
          className: 'csv-btn', 
          text: 'Export to CSV' // Optionally change the button text
      }
    ]
  
    });
  });
  
});
document.addEventListener('DOMContentLoaded', function() {
  // Add an event listener to the download button
  document.getElementById('downloadIceExtent').addEventListener('click', function() {
      // When the button is clicked, redirect to the URL that triggers data download
      window.location.href = "{% url 'download_ice_extent_data' %}";
  });
});