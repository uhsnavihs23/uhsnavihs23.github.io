---
layout: page
title: Timeline
icon: fas fa-history
order: 2
permalink: /timeline/
---

<style>
.tl-wrap { max-width: 680px; margin: 0 auto; padding: 1rem 0 4rem; }
.tl-year-block { margin-bottom: 2.5rem; }
.tl-year {
  font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.1em; color: var(--text-muted-color);
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 0.4rem; margin-bottom: 1.2rem;
}
.tl-tree { position: relative; padding-left: 1.8rem; }
.tl-tree::before {
  content: ''; position: absolute; left: 0.55rem; top: 0; bottom: 0;
  width: 2px; background: var(--border-color);
}
.tl-item { position: relative; margin-bottom: 1.2rem; }
.tl-item::before {
  content: ''; position: absolute; left: -1.27rem; top: 0.45rem;
  width: 10px; height: 10px; border-radius: 50%;
  background: var(--main-bg); border: 2px solid #3b6cf8;
}
.tl-item:first-child::before { background: #3b6cf8; }
.tl-card {
  border: 1.5px solid var(--border-color); border-radius: 10px;
  padding: 0.9rem 1.1rem; background: var(--card-bg);
  transition: border-color 0.2s, transform 0.2s;
}
.tl-card:hover { border-color: #3b6cf8; transform: translateX(4px); }
.tl-card-top { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.3rem; flex-wrap: wrap; }
.tl-tag {
  font-size: 0.65rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.05em; padding: 0.15rem 0.45rem; border-radius: 4px;
}
.tl-tag--blue  { background: #dbeafe; color: #1e40af; }
.tl-tag--slate { background: var(--highlight-bg); color: var(--text-muted-color); }
.tl-tag--warm  { background: #fef3c7; color: #92400e; }
.tl-tag--green { background: #dcfce7; color: #166534; }
.tl-date { font-size: 0.75rem; color: var(--text-muted-color); margin-left: auto; }
.tl-title {
  font-size: 0.97rem; font-weight: 600;
  color: var(--text-color); text-decoration: none; display: block; line-height: 1.4;
}
.tl-title:hover { color: #3b6cf8; text-decoration: none; }
.tl-desc { font-size: 0.83rem; color: var(--text-muted-color); margin-top: 0.2rem; line-height: 1.5; }
</style>

<div class="tl-wrap">

  <!-- 2026 -->
  <div class="tl-year-block">
    <div class="tl-year">2026</div>
    <div class="tl-tree">
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--warm">Policy Tool</span>
            <span class="tl-date">Mar 2026</span>
          </div>
          <a href="/projects/policy-brief-generator/" class="tl-title">India Policy Brief Generator</a>
          <p class="tl-desc">Generate structured policy briefs from live Indian news headlines on any topic.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- 2025 -->
  <div class="tl-year-block">
    <div class="tl-year">2025</div>
    <div class="tl-tree">
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--warm">Policy</span>
            <span class="tl-date">Jun 2025</span>
          </div>
          <a href="/posts/fixing-urban-governance-india/" class="tl-title">Urban Governance in India</a>
          <p class="tl-desc">A structural analysis of what's broken in urban governance and how cities can be fixed.</p>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--slate">Web App</span>
            <span class="tl-date">Jun 2025</span>
          </div>
          <a href="/posts/image-filter-app/" class="tl-title">Image Editor Web App</a>
          <p class="tl-desc">Browser-based image editing tool with filters, adjustments, and multi-format export.</p>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--slate">Web App</span>
            <span class="tl-date">Jun 2025</span>
          </div>
          <a href="/posts/github-profile-finder/" class="tl-title">GitHub Profile Finder</a>
          <p class="tl-desc">Search and explore GitHub user profiles and public repositories.</p>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--blue">Data Analytics</span>
            <span class="tl-date">Jun 2025</span>
          </div>
          <a href="/projects/data-analyst-projects/food-delivery-analytics/" class="tl-title">Food Delivery Analytics</a>
          <p class="tl-desc">End-to-end analysis of food delivery dataset — customer behaviour, order trends, revenue insights.</p>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--blue">Data Analytics</span>
            <span class="tl-date">Jun 2025</span>
          </div>
          <a href="/projects/data-analyst-projects/project-1-customer-shopping-trends-analysis/" class="tl-title">Customer Shopping Trends</a>
          <p class="tl-desc">Consumer shopping pattern analysis with segmentation and visual dashboards.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- 2024 -->
  <div class="tl-year-block">
    <div class="tl-year">2024</div>
    <div class="tl-tree">
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--slate">Web App</span>
            <span class="tl-date">Feb 2024</span>
          </div>
          <a href="/posts/movie-recommender/" class="tl-title">Interactive Movie Recommender</a>
          <p class="tl-desc">Discover movies by genre with posters and descriptions, powered by TMDB API.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- 2023 -->
  <div class="tl-year-block">
    <div class="tl-year">2023</div>
    <div class="tl-tree">
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--slate">Web App</span>
            <span class="tl-date">Nov 2023</span>
          </div>
          <a href="/posts/news/" class="tl-title">News Headlines App</a>
          <p class="tl-desc">Aggregates live news headlines across categories using a public news API.</p>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--slate">Web App</span>
            <span class="tl-date">Jan 2023</span>
          </div>
          <a href="/posts/book-recommender/" class="tl-title">Book Recommender</a>
          <p class="tl-desc">Explore and discover books using the Google Books API with search and preview.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- 2022 -->
  <div class="tl-year-block">
    <div class="tl-year">2022</div>
    <div class="tl-tree">
      <div class="tl-item">
        <div class="tl-card">
          <div class="tl-card-top">
            <span class="tl-tag tl-tag--green">Academic</span>
            <span class="tl-date">Jun 2022</span>
          </div>
          <a href="/posts/electricity-analysis/" class="tl-title">Campus Electricity Analysis — IIT Gandhinagar</a>
          <p class="tl-desc">Identified 10% reduction potential (13 lakh kWh/year) in campus electricity consumption.</p>
        </div>
      </div>
    </div>
  </div>

</div>
