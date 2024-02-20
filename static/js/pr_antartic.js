$('.tabmenu-wrap .custom-tab-nav').find('.tab-link').on('click', function(e) {
    var $this = $(this);
    var $all_tab_nav = $this.parents('.custom-tab-nav').find('.tab-item');
    var $tab_contents = $this.parents('.tabmenu-wrap').find('.con-box');
    var id = $this.attr('href');

    e.preventDefault();
    $all_tab_nav.removeClass('on');
    $this.parent().addClass('on');
    $tab_contents.hide();
    $(id).show();
});
$(document).ready(function() {
    $('#antarticmass_table').DataTable({
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

  });

  $(document).ready(function() {
    $('#hotpoints_table').DataTable({
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