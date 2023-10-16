document.getElementById('toggleLabs').addEventListener('click', function() {
    var labsContent = document.getElementById('labsContent');
    if (labsContent.style.display === 'none') {
        labsContent.style.display = 'block';
    } else {
        labsContent.style.display = 'none';
    }
});

