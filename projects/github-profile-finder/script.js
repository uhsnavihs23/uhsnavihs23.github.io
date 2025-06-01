async function fetchProfile() {
    const username = document.getElementById("username").value.trim();
    const profileDiv = document.getElementById("profile");
    if (!username) {
        profileDiv.innerHTML = "<p>Please enter a username.</p>";
        return;
    }
    profileDiv.innerHTML = "<p>Loading...</p>";
    try {
        const response = await fetch(`https://api.github.com/users/${username}`);
        if (!response.ok) throw new Error("User not found");
        const data = await response.json();
        profileDiv.innerHTML = `
        <img src="${data.avatar_url}" alt="${data.login}" width="100">
        <h2>${data.name || data.login}</h2>
        <p>${data.bio || "No bio available"}</p>
        <p>Repositories: ${data.public_repos}</p>
        <p>Followers: ${data.followers}</p>
        <a href="${data.html_url}" target="_blank">View Profile</a>
      `;
    } catch (error) {
        profileDiv.innerHTML = `<p>Error: ${error.message}</p>`;
    }
}