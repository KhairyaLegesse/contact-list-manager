document.getElementById('searchButton').addEventListener('click', function() { // Add click event listener to the search button
    const searchText = document.getElementById('searchInput').value.toLowerCase(); // Get the search query from the input field and convert to lowercase
    const rows = document.querySelectorAll('tbody tr'); // Select all rows inside the table body

    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(searchText) ? '' : 'none';
    });
}); 


