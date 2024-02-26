document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('attendanceForm');
    const entryTimeInput = document.getElementById('entryTime');
    const leavingTimeInput = document.getElementById('leavingTime');

    // Set default value for "Time of Entry" field
    const currentEntryTime = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
    entryTimeInput.value = currentEntryTime;

    // Set default value for "Time of Leaving" field
    const currentLeavingTime = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
    leavingTimeInput.value = currentLeavingTime;

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission
        
        // Get form data
        const employeeName = document.getElementById('employeeName').value;
        const entryTime = entryTimeInput.value;
        const leavingTime = leavingTimeInput.value;
        const entryLocation = document.getElementById('entryLocation').value;
        const leavingLocation = document.getElementById('leavingLocation').value;

        // Format data as CSV row
        const csvRow = `${employeeName},${entryTime},${leavingTime},${entryLocation},${leavingLocation}\n`;

        // Call function to save data to Excel file
        saveToExcel(csvRow);
        
        // Reset form fields
        form.reset();
    });

    function saveToExcel(data) {
        // Create Blob with CSV data
        const blob = new Blob([data], { type: 'text/csv;charset=utf-8' });

        // Create URL for Blob
        const url = window.URL.createObjectURL(blob);

        // Create link element
        const link = document.createElement('a');
        link.href = url;

        // Set filename for download
        link.setAttribute('download', 'attendance.csv');

        // Append link to DOM and trigger click event to start download
        document.body.appendChild(link);
        link.click();

        // Cleanup
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
    }
});
