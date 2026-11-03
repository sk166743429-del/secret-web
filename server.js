const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const upload = multer({ dest: 'public/uploads/' });

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

let activeBannerLink = '#';

app.use((req, res, next) => {
  res.locals.bannerLink = activeBannerLink;
  next();
});

app.get('/', (req, res) => {
  res.render('index');
});

app.get('/login', (req, res) => {
  res.render('login');
});

app.post('/admin/update-dash-photo', upload.single('bannerImage'), (req, res) => {
  if (req.body.bannerLink) {
    activeBannerLink = req.body.bannerLink.trim();
  }
  if (!req.file) return res.redirect('back');
  fs.rename(req.file.path, __dirname + '/public/banner.png', (err) => {
    res.redirect('back');
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
