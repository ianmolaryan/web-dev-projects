document.addEventListener("DOMContentLoaded", () => {
    const cardContainer = document.getElementById("cardContainer");

    // Fetch data from JSON file
    fetch("projects.json")
        .then(response => response.json())
        .then(data => {
            data.forEach((project, index) => {
                // Create card element
                const card = document.createElement("div");
                card.classList.add("card");

                // Create and set thumbnail image
                const img = document.createElement("img");
                img.src = project.thumbnail;
                img.alt = project.title;
                card.appendChild(img);

                // Create content wrapper
                const cardContent = document.createElement("div");
                cardContent.classList.add("card-content");

                // Create and set title
                const title = document.createElement("h3");
                title.textContent = project.title;
                cardContent.appendChild(title);

                // Create and set "Read More" button
                const readMore = document.createElement("a");
                readMore.href = `project.html?index=${index}&title=${encodeURIComponent(project.title)}&readme=${project.readme}`;
                readMore.classList.add("btn");
                readMore.textContent = "Read More";
                
                // Append title and button to card content, then to card
                cardContent.appendChild(readMore);
                card.appendChild(cardContent);

                // Append card to container
                cardContainer.appendChild(card);
            });
        })
        .catch(error => console.error("Error loading projects:", error));
});
