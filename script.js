document.addEventListener("DOMContentLoaded", () => {
  const cardContainer = document.getElementById("cardContainer");
  const searchInput = document.getElementById("searchInput");

  // Fetch data from JSON file
  fetch("projects.json")
    .then((response) => response.json())
    .then((data) => {
      // Store original data for filtering
      let projects = data;

      function renderProjects(filteredProjects) {
        // Clear previous cards
        cardContainer.innerHTML = "";

        filteredProjects.forEach((project, index) => {
          // Create card element
          const card = document.createElement("div");
          card.classList.add("card");

          // Add data attributes
          card.setAttribute("data-aos", "fade-up");
          card.setAttribute("data-aos-delay", "300");

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
          readMore.href = `project.html?index=${index}&title=${encodeURIComponent(
            project.title
          )}&readme=${project.readme}`;
          readMore.classList.add("btn");
          readMore.textContent = "Read More";

          // Append title and button to card content, then to card
          cardContent.appendChild(readMore);
          card.appendChild(cardContent);

          // Append card to container
          cardContainer.appendChild(card);
        });
      }

      // Initial rendering of projects
      renderProjects(projects);

      let debounceTimeout; // Variable to store timeout

      // Filter functionality with debounce
      searchInput.addEventListener("input", () => {
        clearTimeout(debounceTimeout); // Clear previous timeout
        debounceTimeout = setTimeout(() => {
          const searchTerm = searchInput.value.toLowerCase();
          const filteredProjects = projects.filter((project) =>
            project.title.toLowerCase().includes(searchTerm)
          );
          renderProjects(filteredProjects);
        }, 500); // half second delay
      });
    })
    .catch((error) => console.error("Error loading projects:", error));
});
