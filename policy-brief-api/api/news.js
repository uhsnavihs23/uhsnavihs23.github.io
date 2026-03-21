export default async function handler(req, res) {
  const { topic } = req.query;
  if (!topic) {
    return res.status(400).json({ error: 'topic is required' });
  }

  const API_KEY = process.env.NEWS_API_KEY;
  const url = `https://newsdata.io/api/1/news?apikey=${API_KEY}&q=${encodeURIComponent(topic + ' India')}&country=in&language=en&category=politics,business,top`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    res.setHeader('Access-Control-Allow-Origin', 'https://uhsnavihs23.github.io');
    res.status(200).json(data);
  } catch (e) {
    res.status(500).json({ error: 'Failed to fetch news' });
  }
}
