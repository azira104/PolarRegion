$('#palmerIter_table').DataTable({
    paging: true,
    paging:true,
        dom: 'Bfrtip',
        
        buttons: [
            {
                extend: 'csv',
                className: 'csv-btn', 
                text: 'Export to CSV' // Optionally change the button text
            }
        ]
});
$('#palmerSize_table').DataTable({
    paging: true,
    paging:true,
        dom: 'Bfrtip',
        
        buttons: [
            {
                extend: 'csv',
                className: 'csv-btn', 
                text: 'Export to CSV' // Optionally change the button text
            }
        ]
});