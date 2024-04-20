$(document).ready(function() {
    // Initialize DataTable without buttons
    $("#datatable").DataTable();

    // Initialize DataTable with buttons and icons
    var table = $("#datatable-buttons").DataTable({
        lengthChange: false, // Remove the "Show X entries" dropdown
        buttons: [
            {
                extend: 'copy',
                className: 'btn btn-soft-primary',
                text: '<i class="fas fa-copy"></i>',
                titleAttr: 'Copy'
            },
            {
                extend: 'excel',
                className: 'btn btn-soft-danger',
                text: '<i class="fas fa-file-excel"></i>',
                titleAttr: 'Export to Excel'
            },
            {
                extend: 'pdf',
                className: 'btn btn-soft-secondary',
                text: '<i class="fas fa-file-pdf"></i>',
                titleAttr: 'Export to PDF'
            },
            {
                extend: 'csv',
                className: 'btn btn-soft-warning',
                text: '<i class="fas fa-file-csv"></i>',
                titleAttr: 'Export to CSV'
            }
        ],
        lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
        pageLength: 10 // Show 10 entries per page by default
    }).buttons().container().appendTo("#datatable-buttons_wrapper .col-md-6:eq(0)");

    // Add Bootstrap classes to DataTables length select dropdown
    $(".dataTables_length select").addClass("form-select form-select-sm");

    // Add margin between buttons
    table.buttons().container().find('button').each(function() {
        $(this).addClass('mr-2'); // Adjust the value as needed
    });
});
