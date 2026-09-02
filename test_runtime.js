const { JSDOM } = require('jsdom');
const dom = new JSDOM(`<!DOCTYPE html><input id="topicInput" value="water"><button id="generateBtn"></button><p id="statusMsg"></p><div id="errorMsg"></div><div id="briefBox"></div><span id="briefDate"></span><h2 id="briefTitle"></h2><p id="briefSummary"></p><p id="briefContext"></p><ul id="briefChallenges"></ul><ul id="briefRecs"></ul>`);
global.document = dom.window.document;
global.fetch = async (url) => { return { json: async () => ({ articles: [] }) }; };

const topic = document.getElementById('topicInput').value.trim();
const btn = document.getElementById('generateBtn');
const statusMsg = document.getElementById('statusMsg');
const errorMsg = document.getElementById('errorMsg');
const briefBox = document.getElementById('briefBox');

async function test() {
    try {
        const url = `https://gnews.io/api/v4/search`;
        let articles = [];
        try {
            const response = await fetch(url);
            const data = await response.json();
            if(data.articles && data.articles.length > 0) {
                articles = data.articles;
            }
        } catch(e) {
            console.log("News API limit reached or failed");
        }
        
        const dateOptions = { year: 'numeric', month: 'long', day: 'numeric' };
        document.getElementById('briefDate').textContent = new Date().toLocaleDateString('en-IN', dateOptions);
        document.getElementById('briefTitle').textContent = `Policy Brief: ${topic}`;
        
        if(articles.length > 0) {
            document.getElementById('briefSummary').textContent = "Real";
        } else {
            document.getElementById('briefSummary').textContent = `The issue of ${topic}`;
            document.getElementById('briefContext').textContent = `Recent legislative sessions ${topic}`;
            const challenges = [`Misalignment ${topic}`, "Absence", "Regulatory"];
            document.getElementById('briefChallenges').innerHTML = challenges.map(c => `<li>${c}</li>`).join('');
            const recs = ["Mandate", "Incentivize", `Draft ${topic}`];
            document.getElementById('briefRecs').innerHTML = recs.map(c => `<li>${c}</li>`).join('');
        }
        
        statusMsg.textContent = "Brief generated successfully.";
        console.log("Success! Summary:", document.getElementById('briefSummary').textContent);
    } catch (error) {
        console.log("Outer Catch:", error);
    }
}
test();
