const axios = require('axios');
const cheerio = require('cheerio');

const videoUrl = "https://www.youtube.com/watch?v=9qqs8rWSrhc"; // Example video URL

axios.get(videoUrl)
  .then(response => {
    const $ = cheerio.load(response.data);
    const title = $('title').text();
    console.log(title.replace(' - YouTube', '')); // YouTube adds " - YouTube" to the end of each video title
  })
  .catch(error => console.error('Error fetching page:', error));
