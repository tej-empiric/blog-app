document.addEventListener("DOMContentLoaded", function() {
    var blogTitles = document.querySelectorAll(".blog-title");
    var content = document.getElementById("content");

    blogTitles.forEach(function(title) {
        title.addEventListener("click", function() {
            var blogId = this.getAttribute("data-blog-id");
            fetch(`/blog/${blogId}/content/`)
                .then(response => response.text())
                .then(data => {
                    content.innerHTML = data;
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
});